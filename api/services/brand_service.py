import uuid
import os
import logging
import re
from urllib.parse import urlparse
from typing import Optional, Dict
from fastapi import HTTPException, UploadFile
from starlette.concurrency import run_in_threadpool
from minio.error import S3Error

from config.config import get_settings
from config.minio_client import minio_client
from repositories.brand_repository import BrandRepository
from repositories.image_repository import ImageRepository
from schemas.brand_schemas import BrandCreate, BrandUpdate

settings = get_settings()
logger = logging.getLogger(__name__)


class BrandService:
    def __init__(self, brand_repo: BrandRepository = None, image_repo: ImageRepository = None):
        self.brand_repo = brand_repo
        self.image_repo = image_repo

    async def upload_logo(self, logo_file: UploadFile) -> str:
        """Upload logo lên MinIO bucket 'trademark' và trả về URL"""
        try:
            # Validate file type
            if not logo_file.content_type or not logo_file.content_type.startswith('image/'):
                raise HTTPException(status_code=400, detail="File phải là hình ảnh")

            # Đọc toàn bộ file content vào memory vì file object có thể bị đóng
            file_content = await logo_file.read()
            
            if len(file_content) == 0:
                raise HTTPException(status_code=400, detail="File rỗng")
            
            # Validate file size (max 5MB)
            if len(file_content) > 5 * 1024 * 1024:
                raise HTTPException(status_code=400, detail="Kích thước file không được vượt quá 5MB")

            # Sử dụng bucket "trademark" cho logo thương hiệu
            brand_bucket = "trademark"
            
            # Đảm bảo bucket tồn tại
            try:
                if not minio_client.bucket_exists(brand_bucket):
                    minio_client.make_bucket(brand_bucket)
                    logger.info(f"Created bucket: {brand_bucket}")
            except Exception as e:
                logger.error(f"Error checking/creating bucket: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Không thể truy cập bucket MinIO: {str(e)}")

            # Generate unique filename (lưu trực tiếp trong bucket, không cần prefix)
            file_extension = os.path.splitext(logo_file.filename)[1] if logo_file.filename else '.jpg'
            if not file_extension or file_extension == '':
                file_extension = '.jpg'
            unique_filename = f"{uuid.uuid4().hex}{file_extension}"

            # Upload to MinIO vào bucket trademark
            try:
                # Sử dụng BytesIO để tạo file object mới từ content
                from io import BytesIO
                file_obj = BytesIO(file_content)
                
                url = await run_in_threadpool(
                    self.image_repo.upload_to_bucket,
                    file_obj,
                    unique_filename,
                    logo_file.content_type,
                    brand_bucket
                )
                logger.info(f"Uploaded logo successfully: {url}")
                
                # Đảm bảo URL sử dụng backend proxy endpoint
                if not url.startswith(settings.backend_url):
                    # Tạo URL qua proxy endpoint nếu chưa đúng
                    backend_base = settings.backend_url.rstrip('/')
                    api_prefix = settings.api_prefix
                    url = f"{backend_base}{api_prefix}/brands/logo/{unique_filename}"
                
                return url
            except Exception as e:
                import traceback
                error_detail = traceback.format_exc()
                logger.error(f"Upload error: {str(e)}\n{error_detail}")
                raise HTTPException(
                    status_code=500, 
                    detail=f"Upload logo thất bại: {str(e)}. Vui lòng kiểm tra kết nối MinIO."
                )
        except HTTPException:
            raise
        except S3Error as e:
            logger.error(f"MinIO S3Error: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Lỗi MinIO: {str(e)}")
        except Exception as e:
            import traceback
            error_detail = traceback.format_exc()
            logger.error(f"Unexpected error in upload_logo: {str(e)}\n{error_detail}")
            raise HTTPException(status_code=500, detail=f"Lỗi không xác định khi upload logo: {str(e)}")

    async def delete_logo(self, logo_url: Optional[str]) -> bool:
        """Xóa logo từ MinIO"""
        if not logo_url:
            return True

        try:
            # Parse URL để lấy object name
            parsed_url = urlparse(logo_url)
            object_name = parsed_url.path.lstrip('/')
            
            # Xác định bucket và object name
            brand_bucket = "trademark"
            
            # Remove bucket name prefix if present
            if object_name.startswith(f"{brand_bucket}/"):
                object_name = object_name[len(f"{brand_bucket}/"):]
            elif object_name.startswith(f"{settings.minio_bucket}/"):
                object_name = object_name[len(f"{settings.minio_bucket}/"):]

            # Delete from MinIO bucket trademark
            minio_client.remove_object(brand_bucket, object_name)
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
            logger.info(f"Creating brand: {brand_name}")
            
            # Kiểm tra tên thương hiệu đã tồn tại chưa
            try:
                exists = await self.brand_repo.check_name_exists(brand_name)
                if exists:
                    raise HTTPException(status_code=400, detail=f"Thương hiệu '{brand_name}' đã tồn tại")
            except Exception as e:
                logger.error(f"Error checking name exists: {str(e)}")
                if isinstance(e, HTTPException):
                    raise
                raise HTTPException(status_code=500, detail=f"Lỗi khi kiểm tra tên thương hiệu: {str(e)}")

            # Xử lý logo: ưu tiên file, sau đó là URL
            logo_url = None
            if logo_file:
                try:
                    # Upload file lên MinIO
                    logger.info(f"Uploading logo file: {logo_file.filename}")
                    logo_url = await self.upload_logo(logo_file)
                    logger.info(f"Logo uploaded successfully: {logo_url}")
                except Exception as e:
                    logger.error(f"Error uploading logo: {str(e)}")
                    if isinstance(e, HTTPException):
                        raise
                    raise HTTPException(status_code=500, detail=f"Lỗi khi upload logo: {str(e)}")
            elif brand_data.logo:
                # Sử dụng URL được cung cấp
                logo_url = brand_data.logo.strip() if brand_data.logo and brand_data.logo.strip() else None
                logger.info(f"Using provided logo URL: {logo_url}")

            # Tạo brand dict
            brand_dict = {
                "name": brand_name,
                "logo": logo_url,
                "description": brand_data.description.strip() if brand_data.description and brand_data.description.strip() else None,
                "is_active": brand_data.is_active if brand_data.is_active is not None else True,
                "is_deleted": False  # Đảm bảo set is_deleted = False khi tạo mới
            }

            # Lưu vào database
            logger.info(f"Creating brand in database with data: {brand_dict}")
            try:
                created_brand = await self.brand_repo.create(brand_dict)
                brand_id = created_brand.get('id') if created_brand else created_brand.get('_id') if created_brand else 'Unknown'
                logger.info(f"Brand created successfully with ID: {brand_id}")
                return created_brand
            except Exception as e:
                import traceback
                error_detail = traceback.format_exc()
                logger.error(f"Error creating brand in database: {str(e)}\n{error_detail}")
                
                # Nếu lỗi khi tạo, xóa logo đã upload (nếu có)
                if logo_file and logo_url:
                    try:
                        await self.delete_logo(logo_url)
                        logger.info(f"Deleted uploaded logo after database error: {logo_url}")
                    except Exception as delete_error:
                        logger.warning(f"Failed to delete logo after error: {str(delete_error)}")
                raise HTTPException(
                    status_code=500, 
                    detail=f"Lỗi khi tạo thương hiệu trong database: {str(e)}"
                )
        except HTTPException:
            raise
        except Exception as e:
            import traceback
            error_detail = traceback.format_exc()
            logger.error(f"Unexpected error in create_brand: {str(e)}\n{error_detail}")
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

        # Xử lý logo
        logo_url = brand_data.logo if brand_data.logo else existing_brand.get("logo")
        
        # Nếu có file mới, upload và xóa logo cũ
        if logo_file:
            # Xóa logo cũ nếu có
            if existing_brand.get("logo"):
                await self.delete_logo(existing_brand.get("logo"))
            
            # Upload logo mới
            logo_url = await self.upload_logo(logo_file)
        elif brand_data.logo is not None:
            # Nếu có URL mới và khác URL cũ, xóa logo cũ
            if brand_data.logo != existing_brand.get("logo") and existing_brand.get("logo"):
                await self.delete_logo(existing_brand.get("logo"))
            logo_url = brand_data.logo

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
        return updated_brand

    def _convert_to_proxy_url(self, logo_url: Optional[str], brand_name: Optional[str] = None) -> Optional[str]:
        """Chuyển đổi URL logo cũ (direct MinIO) sang proxy endpoint
        Tự động match với filename thực tế trong MinIO nếu có
        """
        if not logo_url:
            return None
        
        # Nếu đã là proxy URL thì không cần convert
        backend_base = settings.backend_url.rstrip('/')
        api_prefix = settings.api_prefix
        proxy_base = f"{backend_base}{api_prefix}/brands/logo/"
        if logo_url.startswith(proxy_base):
            return logo_url
        
        # Nếu là URL MinIO trực tiếp, extract filename và convert
        if 'trademark' in logo_url or settings.minio_url in logo_url or '127.0.0.1:9000' in logo_url or 'localhost:9000' in logo_url:
            # Tìm filename sau /trademark/
            match = re.search(r'/trademark/([^/?]+)', logo_url)
            if match:
                filename_from_url = match.group(1)
                
                # Thử tìm file thực tế trong MinIO với tên brand (không cần extension chính xác)
                # Nếu có brand_name, thử match với file trong bucket
                if brand_name:
                    try:
                        bucket_name = "trademark"
                        if minio_client.bucket_exists(bucket_name):
                            # Tìm file có tên brand trong đó (không quan tâm extension)
                            brand_lower = brand_name.lower().replace(' ', '')
                            objects = minio_client.list_objects(bucket_name, recursive=True)
                            
                            for obj in objects:
                                obj_name_lower = obj.object_name.lower()
                                # Match: adidas-logo.jpg hoặc adidas-logo.png hoặc nike-logo.jpg
                                if brand_lower in obj_name_lower and '-logo' in obj_name_lower:
                                    # Tìm thấy file match với brand
                                    return f"{proxy_base}{obj.object_name}"
                    except Exception as e:
                        logger.warning(f"Could not match filename for brand '{brand_name}': {str(e)}")
                
                # Fallback: dùng filename từ URL
                return f"{proxy_base}{filename_from_url}"
            else:
                # Thử extract từ path
                parsed = urlparse(logo_url)
                path_parts = parsed.path.strip('/').split('/')
                if len(path_parts) >= 2 and path_parts[0] == 'trademark':
                    filename = path_parts[1]
                    return f"{proxy_base}{filename}"
        
        # Nếu không match pattern nào, trả về nguyên URL
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
        
        # Convert logo URLs sang proxy endpoint
        from fastapi.encoders import jsonable_encoder
        result = []
        for brand in brands:
            brand_dict = brand if isinstance(brand, dict) else brand.dict()
            if 'logo' in brand_dict and brand_dict['logo']:
                brand_name = brand_dict.get('name', '')
                brand_dict['logo'] = self._convert_to_proxy_url(brand_dict['logo'], brand_name=brand_name)
            result.append(brand_dict)
        
        return jsonable_encoder(result)

    async def get_brand_by_id(self, brand_id: str) -> Dict:
        """Lấy thương hiệu theo ID"""
        brand = await self.brand_repo.get_by_id(brand_id)
        if isinstance(brand, dict):
            if 'logo' in brand and brand['logo']:
                brand_name = brand.get('name', '')
                brand['logo'] = self._convert_to_proxy_url(brand['logo'], brand_name=brand_name)
        return brand
    
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
                raise HTTPException(status_code=404, detail=f"Bucket '{brand_bucket}' không tồn tại")
            
            # Lấy danh sách tất cả objects trong bucket
            objects = minio_client.list_objects(brand_bucket, recursive=True)
            
            # Map filename -> brand name (từ các file logo đã có)
            logo_files = {}
            for obj in objects:
                filename = obj.object_name
                # Chỉ xử lý các file logo có tên brand (bỏ qua UUID files)
                if '-' in filename and filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    # Extract brand name từ filename (ví dụ: "nike-logo.png" -> "nike")
                    parts = filename.split('-')
                    if len(parts) >= 2:
                        brand_name = parts[0].lower()
                        # Map các tên brand từ filename -> tên trong DB (có thể khác case)
                        # Không cần map vì sẽ match case-insensitive
                        logo_url = self._generate_logo_url(filename)
                        logo_files[brand_name] = {
                            'filename': filename,
                            'url': logo_url
                        }
                        
                        # Handle "newbalance" -> "new balance" hoặc "New Balance"
                        if brand_name == 'new':
                            logo_files['new balance'] = {
                                'filename': filename,
                                'url': logo_url
                            }
                        if brand_name == 'newbalance':
                            logo_files['new balance'] = {
                                'filename': filename,
                                'url': logo_url
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
                    # Cập nhật logo URL (cả khi đã có để đảm bảo URL đúng)
                    await self.brand_repo.update(brand['id'], {'logo': logo_info['url']})
                    updated_count += 1
                    updated_brands.append(brand.get('name', brand_name))
                    logger.info(f"Updated logo for brand '{brand.get('name', brand_name)}': {logo_info['url']}")
            
            return {
                "message": f"Đã đồng bộ {updated_count} logo từ MinIO",
                "updated": updated_count,
                "updated_brands": updated_brands,
                "found_files": len(logo_files)
            }
        except HTTPException:
            raise
        except Exception as e:
            import traceback
            error_detail = traceback.format_exc()
            logger.error(f"Error syncing logos: {str(e)}\n{error_detail}")
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

