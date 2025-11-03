import uuid
import os
import re
from urllib.parse import urlparse
from typing import Optional, Dict
from fastapi import HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from starlette.concurrency import run_in_threadpool
from minio.error import S3Error

from config.config import get_settings
from config.minio_client import minio_client
from repositories.brand_repository import BrandRepository
from repositories.image_repository import ImageRepository
from schemas.brand_schemas import BrandCreate, BrandUpdate

settings = get_settings()


class BrandService:
    def __init__(self, brand_repo: BrandRepository = None, image_repo: ImageRepository = None):
        self.brand_repo = brand_repo
        self.image_repo = image_repo

    async def upload_logo(self, logo_file: UploadFile) -> str:
        """Upload logo lên MinIO bucket 'trademark' và trả về URL MinIO đầy đủ"""
        try:
            if not logo_file.content_type or not logo_file.content_type.startswith('image/'):
                raise HTTPException(status_code=400, detail="File phải là hình ảnh")

            file_content = await logo_file.read()
            
            if len(file_content) == 0:
                raise HTTPException(status_code=400, detail="File rỗng")
            
            if len(file_content) > 5 * 1024 * 1024:
                raise HTTPException(status_code=400, detail="Kích thước file không được vượt quá 5MB")

            brand_bucket = "trademark"
            
            try:
                if not minio_client.bucket_exists(brand_bucket):
                    minio_client.make_bucket(brand_bucket)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Không thể truy cập bucket MinIO: {str(e)}")

            file_extension = os.path.splitext(logo_file.filename)[1] if logo_file.filename else '.jpg'
            if not file_extension or file_extension == '':
                file_extension = '.jpg'
            unique_filename = f"{uuid.uuid4().hex}{file_extension}"

            try:
                from io import BytesIO
                file_obj = BytesIO(file_content)
                
                # Upload vào MinIO
                await run_in_threadpool(
                    self.image_repo.upload_to_bucket,
                    file_obj,
                    unique_filename,
                    logo_file.content_type,
                    brand_bucket
                )
                
                # Tạo URL MinIO đầy đủ: http://localhost:9000/trademark/filename.jpg
                minio_base_url = settings.port_image if hasattr(settings, 'port_image') and settings.port_image else f"http://{settings.minio_url}"
                minio_url = f"{minio_base_url.rstrip('/')}/{brand_bucket}/{unique_filename}"
                
                # Trả về URL MinIO đầy đủ để lưu vào database
                return minio_url
            except Exception as e:
                raise HTTPException(
                    status_code=500, 
                    detail=f"Upload logo thất bại: {str(e)}. Vui lòng kiểm tra kết nối MinIO."
                )
        except HTTPException:
            raise
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Lỗi MinIO: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Lỗi không xác định khi upload logo: {str(e)}")

    async def delete_logo(self, logo_url: Optional[str]) -> bool:
        """Xóa logo từ MinIO (chỉ xóa nếu là file từ MinIO, không xóa URL external)"""
        if not logo_url:
            return True

        try:
            # Nếu là URL external (không phải MinIO) thì không xóa
            if logo_url.startswith('http://') or logo_url.startswith('https://'):
                # Kiểm tra xem có phải là URL của MinIO không (có chứa trademark)
                if '/trademark/' not in logo_url:
                    # External URL - không xóa
                    return True
            
            brand_bucket = "trademark"
            object_name = None
            
            # Xử lý URL MinIO đầy đủ: http://localhost:9000/trademark/filename.jpg
            if logo_url.startswith('http://') or logo_url.startswith('https://'):
                # URL MinIO - extract filename
                parsed_url = urlparse(logo_url)
                path = parsed_url.path.lstrip('/')
                
                # Extract filename từ path: trademark/filename.jpg
                if path.startswith('trademark/'):
                    object_name = path.replace('trademark/', '')
            # Xử lý path dạng "trademark/filename"
            elif logo_url.startswith('trademark/'):
                object_name = logo_url.replace('trademark/', '')
            # Format cũ: chỉ filename
            elif '/' not in logo_url and not logo_url.startswith('http'):
                object_name = logo_url

            # Xóa file từ MinIO nếu có object_name
            if object_name:
                try:
                    minio_client.remove_object(brand_bucket, object_name)
                except:
                    pass
            
            return True
        except S3Error:
            # Nếu object không tồn tại thì bỏ qua
            return True

    async def create_brand(self, brand_data: BrandCreate, logo_file: Optional[UploadFile] = None) -> Dict:
        """Tạo thương hiệu mới"""
        try:
            # Validate tên thương hiệu
            if not brand_data.name or not brand_data.name.strip():
                raise HTTPException(status_code=400, detail="Tên thương hiệu là bắt buộc")
            
            brand_name = brand_data.name.strip()
            
            # Kiểm tra tên thương hiệu đã tồn tại chưa
            try:
                exists = await self.brand_repo.check_name_exists(brand_name)
                if exists:
                    raise HTTPException(status_code=400, detail=f"Thương hiệu '{brand_name}' đã tồn tại")
            except Exception as e:
                if isinstance(e, HTTPException):
                    raise
                raise HTTPException(status_code=500, detail=f"Lỗi khi kiểm tra tên thương hiệu: {str(e)}")

            # Xử lý logo: ƯU TIÊN file upload vào MinIO
            # Nếu có cả file và URL → chỉ dùng file (bỏ qua URL)
            # Nếu không có file → mới dùng URL (external hoặc MinIO path)
            logo_url = None
            if logo_file:
                # ƯU TIÊN: Có file thì upload vào MinIO bucket brand_logo
                # Bỏ qua URL nếu có (không cần xử lý brand_data.logo)
                try:
                    logo_url = await self.upload_logo(logo_file)
                except Exception as e:
                    if isinstance(e, HTTPException):
                        raise
                    raise HTTPException(status_code=500, detail=f"Lỗi khi upload logo: {str(e)}")
            elif brand_data.logo:
                # Xử lý URL được cung cấp
                provided_logo = brand_data.logo.strip() if brand_data.logo and brand_data.logo.strip() else None
                
                if provided_logo:
                    # Nếu là URL external hoặc URL MinIO đầy đủ → lưu trực tiếp
                    if provided_logo.startswith('http://') or provided_logo.startswith('https://'):
                        logo_url = provided_logo
                    # Nếu là path dạng "trademark/filename", chuyển sang URL MinIO đầy đủ
                    elif provided_logo.startswith('trademark/'):
                        filename = provided_logo.replace('trademark/', '')
                        minio_base_url = settings.port_image if hasattr(settings, 'port_image') and settings.port_image else f"http://{settings.minio_url}"
                        logo_url = f"{minio_base_url.rstrip('/')}/trademark/{filename}"
                    else:
                        # Các format khác → giữ nguyên hoặc chuyển sang URL MinIO
                        logo_url = provided_logo

            # Tạo brand dict
            brand_dict = {
                "name": brand_name,
                "logo": logo_url,
                "description": brand_data.description.strip() if brand_data.description and brand_data.description.strip() else None,
                "is_active": brand_data.is_active if brand_data.is_active is not None else True,
                "is_deleted": False  # Đảm bảo set is_deleted = False khi tạo mới
            }

            # Lưu vào database
            try:
                created_brand = await self.brand_repo.create(brand_dict)
                return jsonable_encoder(created_brand)
            except Exception as e:
                # Nếu lỗi khi tạo, xóa logo đã upload (nếu có)
                if logo_file and logo_url:
                    try:
                        await self.delete_logo(logo_url)
                    except Exception:
                        pass
                raise HTTPException(
                    status_code=500, 
                    detail=f"Lỗi khi tạo thương hiệu trong database: {str(e)}"
                )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Lỗi không xác định khi tạo thương hiệu: {str(e)}"
            )

    async def update_brand(
        self,
        brand_id: str,
        brand_data: BrandUpdate,
        logo_file: Optional[UploadFile] = None
    ) -> Dict:
        """Cập nhật thương hiệu"""
        # Kiểm tra brand có tồn tại không
        existing_brand = await self.brand_repo.get_by_id(brand_id)
        if not existing_brand:
            raise HTTPException(status_code=404, detail="Thương hiệu không tồn tại")

        # Kiểm tra tên mới có trùng với brand khác không
        if brand_data.name and brand_data.name != existing_brand.get("name"):
            if await self.brand_repo.check_name_exists(brand_data.name, exclude_id=brand_id):
                raise HTTPException(
                    status_code=400,
                    detail=f"Thương hiệu '{brand_data.name}' đã tồn tại"
                )

        logo_url = existing_brand.get("logo")
        
        if logo_file:
            if existing_brand.get("logo"):
                await self.delete_logo(existing_brand.get("logo"))
            
            # Upload logo mới - trả về URL MinIO đầy đủ
            logo_url = await self.upload_logo(logo_file)
        elif brand_data.logo is not None:
            # Xử lý URL được cung cấp
            provided_logo = brand_data.logo.strip() if brand_data.logo else None
            
            if provided_logo:
                # Nếu là URL external hoặc URL MinIO đầy đủ → lưu trực tiếp
                if provided_logo.startswith('http://') or provided_logo.startswith('https://'):
                    logo_url = provided_logo
                # Nếu là path dạng "trademark/filename", chuyển sang URL MinIO đầy đủ
                elif provided_logo.startswith('trademark/'):
                    filename = provided_logo.replace('trademark/', '')
                    minio_base_url = settings.port_image if hasattr(settings, 'port_image') and settings.port_image else f"http://{settings.minio_url}"
                    logo_url = f"{minio_base_url.rstrip('/')}/trademark/{filename}"
                else:
                    # Các format khác → giữ nguyên
                    logo_url = provided_logo
                
                # Xóa logo cũ nếu có và khác logo mới (chỉ xóa nếu là file MinIO)
                if existing_brand.get("logo") and existing_brand.get("logo") != logo_url:
                    await self.delete_logo(existing_brand.get("logo"))

        # Cập nhật brand dict
        update_dict = {}
        if brand_data.name:
            update_dict["name"] = brand_data.name.strip()
        if logo_url is not None:
            update_dict["logo"] = logo_url
        if brand_data.description is not None:
            update_dict["description"] = brand_data.description.strip() if brand_data.description else None
        if brand_data.is_active is not None:
            update_dict["is_active"] = brand_data.is_active

        # Cập nhật vào database
        updated_brand = await self.brand_repo.update(brand_id, update_dict)
        # Convert sang JSON serializable format
        return jsonable_encoder(updated_brand)

    def _convert_to_proxy_url(self, logo_url: Optional[str], brand_name: Optional[str] = None) -> Optional[str]:
        """Trả về logo URL nguyên vẹn (không convert nữa, lưu trực tiếp URL MinIO hoặc external)"""
        # Không cần convert nữa - logo_url đã là URL đầy đủ (MinIO hoặc external)
        return logo_url

    async def get_all_brands(self, is_active: Optional[bool] = None):
        """Lấy danh sách tất cả thương hiệu - trả về array trực tiếp giống Categories"""
        # Lấy tất cả brands (không limit để giống Categories)
        brands = await self.brand_repo.get_all_brands(
            skip=0, 
            limit=1000,  # Giới hạn lớn để lấy tất cả
            search=None,
            is_active=is_active
        )
        
        # Trả về logo URL nguyên vẹn (đã là URL MinIO đầy đủ hoặc external URL)
        result = []
        for brand in brands:
            brand_dict = brand if isinstance(brand, dict) else brand.dict()
            result.append(brand_dict)
        
        return jsonable_encoder(result)

    async def get_brand_by_id(self, brand_id: str) -> Dict:
        """Lấy thương hiệu theo ID"""
        brand = await self.brand_repo.get_by_id(brand_id)
        # Trả về logo URL nguyên vẹn (đã là URL MinIO đầy đủ hoặc external URL)
        # Convert sang JSON serializable format
        return jsonable_encoder(brand)
    
    def _generate_logo_url(self, filename: str) -> str:
        """Tạo URL cho logo từ filename trên MinIO
        Sử dụng backend API endpoint để proxy images
        """
        # Sử dụng backend URL để proxy images thông qua API
        # Format: {backend_url}/api/v1/brands/logo/{filename}
        backend_base = settings.backend_url.rstrip('/')
        api_prefix = settings.api_prefix
        return f"{backend_base}{api_prefix}/brands/logo/{filename}"
    
    async def sync_logos_from_minio(self) -> Dict:
        """Đồng bộ logos từ MinIO bucket 'trademark' vào database"""
        try:
            brand_bucket = "trademark"
            
            # Kiểm tra bucket tồn tại
            if not minio_client.bucket_exists(brand_bucket):
                raise HTTPException(status_code=404, detail=f"Bucket 'trademark' không tồn tại")
            
            # Lấy danh sách tất cả objects trong bucket
            objects = minio_client.list_objects(brand_bucket, recursive=True)
            
            # Tạo URL MinIO đầy đủ
            minio_base_url = settings.port_image if hasattr(settings, 'port_image') and settings.port_image else f"http://{settings.minio_url}"
            
            # Map filename -> brand name (từ các file logo đã có)
            logo_files = {}
            for obj in objects:
                filename = obj.object_name
                # Tạo URL MinIO đầy đủ: http://localhost:9000/trademark/filename.jpg
                logo_url = f"{minio_base_url.rstrip('/')}/{brand_bucket}/{filename}"
                
                # Chỉ xử lý các file logo có tên brand (bỏ qua UUID files)
                if '-' in filename and filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    # Extract brand name từ filename (ví dụ: "nike-logo.png" -> "nike")
                    parts = filename.split('-')
                    if len(parts) >= 2:
                        brand_name = parts[0].lower()
                        # Lưu URL MinIO đầy đủ để update vào DB
                        logo_files[brand_name] = {
                            'logo_url': logo_url
                        }
                        
                        # Handle "newbalance" -> "new balance" hoặc "New Balance"
                        if brand_name == 'new':
                            logo_files['new balance'] = {
                                'logo_url': logo_url
                            }
                        if brand_name == 'newbalance':
                            logo_files['new balance'] = {
                                'logo_url': logo_url
                            }
            
            # Lấy tất cả brands để match
            all_brands = await self.brand_repo.get_all_brands(skip=0, limit=1000)
            
            # Cập nhật brands trong database
            updated_count = 0
            updated_brands = []
            for brand_name, logo_info in logo_files.items():
                # Tìm brand theo tên (case insensitive)
                brand = None
                for b in all_brands:
                    if b.get('name', '').lower() == brand_name.lower():
                        brand = b
                        break
                
                # Nếu không tìm thấy, thử tìm exact match
                if not brand:
                    brand = await self.brand_repo.get_by_name(brand_name)
                
                if brand:
                    # Cập nhật logo URL MinIO đầy đủ vào DB
                    await self.brand_repo.update(brand['id'], {'logo': logo_info['logo_url']})
                    updated_count += 1
                    updated_brands.append(brand.get('name', brand_name))
            
            return {
                "message": f"Đã đồng bộ {updated_count} logo từ MinIO bucket '{brand_bucket}'",
                "updated": updated_count,
                "updated_brands": updated_brands,
                "found_files": len(logo_files)
            }
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Lỗi khi đồng bộ logos: {str(e)}")

    async def delete_brand(self, brand_id: str) -> bool:
        """Xóa thương hiệu (soft delete)"""
        brand = await self.brand_repo.get_by_id(brand_id)
        if not brand:
            raise HTTPException(status_code=404, detail="Thương hiệu không tồn tại")

        # Xóa logo từ MinIO
        if brand.get("logo"):
            await self.delete_logo(brand.get("logo"))

        # Soft delete
        return await self.brand_repo.delete_brand(brand_id)

