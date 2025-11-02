from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from typing import Optional, Annotated
from fastapi.responses import JSONResponse

from dependences.dependencies import get_brand_repo, get_image_repo
from repositories.brand_repository import BrandRepository
from repositories.image_repository import ImageRepository
from schemas.brand_schemas import BrandCreate, BrandUpdate
from services.brand_service import BrandService
from config.minio_client import minio_client

brand_router = APIRouter(prefix="/brands", tags=["Brands"])


@brand_router.get("", summary="Lấy danh sách tất cả thương hiệu")
async def get_all_brands(
    is_active: Optional[bool] = Query(None, description="Lọc theo trạng thái hoạt động"),
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """
    Lấy danh sách tất cả thương hiệu
    - Có thể filter theo is_active (true/false)
    """
    try:
        service = BrandService(brand_repo, image_repo)
        brands = await service.get_all_brands(is_active=is_active)
        return JSONResponse(status_code=200, content=brands)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting brands: {str(e)}")


@brand_router.get("/{brand_id}")
async def get_brand_by_id(
    brand_id: str,
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """Lấy thông tin thương hiệu theo ID"""
    service = BrandService(brand_repo, image_repo)
    brand = await service.get_brand_by_id(brand_id)
    return JSONResponse(content=brand, status_code=200)


@brand_router.post("/create", status_code=201)
async def create_brand(
    name: Annotated[str, Form(...)],
    description: Annotated[Optional[str], Form()] = None,
    logo_url: Annotated[Optional[str], Form()] = None,
    logo_file: Annotated[Optional[UploadFile], File()] = None,
    is_active: Annotated[Optional[bool], Form()] = True,
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """
    Tạo thương hiệu mới
    - name: Tên thương hiệu (bắt buộc)
    - description: Mô tả (tùy chọn)
    - logo_file: File logo để upload (tùy chọn, ưu tiên hơn logo_url)
    - logo_url: URL logo (tùy chọn)
    - is_active: Trạng thái hoạt động (mặc định: true)
    
    Logo có thể để trống hoặc cung cấp file/URL
    """
    try:
        # Validate
        if not name or not name.strip():
            raise HTTPException(status_code=400, detail="Tên thương hiệu là bắt buộc")
        
        service = BrandService(brand_repo, image_repo)
        
        # Tạo brand data
        brand_data = BrandCreate(
            name=name.strip(),
            logo=logo_url.strip() if logo_url and logo_url.strip() else None,
            description=description.strip() if description and description.strip() else None,
            is_active=is_active if is_active is not None else True
        )
        
        # Tạo brand với logo file nếu có
        created_brand = await service.create_brand(brand_data, logo_file)
        return JSONResponse(content={
            "message": "Tạo thương hiệu thành công",
            "data": created_brand
        }, status_code=201)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Lỗi khi tạo thương hiệu: {str(e)}"
        )


@brand_router.put("/update/{brand_id}")
async def update_brand_by_id(
    brand_id: str,
    name: Annotated[Optional[str], Form()] = None,
    description: Annotated[Optional[str], Form()] = None,
    logo_url: Annotated[Optional[str], Form()] = None,
    logo_file: Annotated[Optional[UploadFile], File()] = None,
    is_active: Annotated[Optional[bool], Form()] = None,
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """
    Cập nhật thương hiệu theo ID
    Có thể upload logo từ file hoặc cung cấp URL
    """
    try:
        service = BrandService(brand_repo, image_repo)
        
        # Tạo brand update data
        brand_data = BrandUpdate(
            name=name.strip() if name else None,
            logo=logo_url.strip() if logo_url and logo_url.strip() else None,
            description=description.strip() if description and description.strip() else None,
            is_active=is_active
        )
        
        # Cập nhật brand
        updated_brand = await service.update_brand(brand_id, brand_data, logo_file)
        return JSONResponse(content={
            "message": "Cập nhật thương hiệu thành công",
            "data": updated_brand
        }, status_code=200)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Lỗi khi cập nhật thương hiệu: {str(e)}"
        )


@brand_router.delete("/delete/{brand_id}")
async def delete_brand_by_id(
    brand_id: str,
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """Xóa thương hiệu theo ID"""
    service = BrandService(brand_repo, image_repo)
    deleted = await service.delete_brand(brand_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Thương hiệu không tồn tại")
    return JSONResponse(content={"message": "Xóa thương hiệu thành công"}, status_code=200)


@brand_router.post("/sync-logos", summary="Đồng bộ logos từ MinIO vào database")
async def sync_logos_from_minio(
    brand_repo: BrandRepository = Depends(get_brand_repo),
    image_repo: ImageRepository = Depends(get_image_repo)
):
    """
    Đồng bộ logos từ MinIO bucket 'trademark' vào database
    Tìm các file logo đã có trên MinIO và cập nhật URL vào brands tương ứng
    """
    try:
        service = BrandService(brand_repo, image_repo)
        result = await service.sync_logos_from_minio()
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi đồng bộ logos: {str(e)}")


@brand_router.get("/logo/{filename}", summary="Lấy logo thương hiệu")
async def get_brand_logo(
    filename: str
):
    """
    Proxy endpoint để serve logo từ MinIO bucket 'trademark'
    """
    from fastapi.responses import StreamingResponse
    from io import BytesIO
    from minio.error import S3Error
    
    try:
        bucket_name = "trademark"
        
        # URL decode filename nếu cần
        from urllib.parse import unquote
        filename = unquote(filename)
        
        # Kiểm tra bucket tồn tại
        if not minio_client.bucket_exists(bucket_name):
            raise HTTPException(status_code=404, detail=f"Bucket '{bucket_name}' không tồn tại")
        
        # Kiểm tra file có tồn tại không (list objects để verify)
        try:
            # List objects với prefix
            objects = minio_client.list_objects(bucket_name, prefix=filename, recursive=False)
            file_exists = False
            actual_filename = filename
            
            for obj in objects:
                if obj.object_name == filename:
                    file_exists = True
                    actual_filename = obj.object_name
                    break
            
            if not file_exists:
                raise HTTPException(status_code=404, detail=f"Logo '{filename}' không tìm thấy trong bucket")
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Lỗi khi kiểm tra file: {str(e)}")
        
        # Lấy object từ MinIO
        try:
            response = minio_client.get_object(bucket_name, actual_filename)
            data = response.read()
            response.close()
            response.release_conn()
        except S3Error as e:
            raise HTTPException(status_code=404, detail=f"Không thể lấy logo: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Lỗi khi đọc logo: {str(e)}")
        
        # Xác định content type
        content_type = "image/png"
        if filename.lower().endswith(('.jpg', '.jpeg')):
            content_type = "image/jpeg"
        elif filename.lower().endswith('.gif'):
            content_type = "image/gif"
        elif filename.lower().endswith('.svg'):
            content_type = "image/svg+xml"
        elif filename.lower().endswith('.webp'):
            content_type = "image/webp"
        
        # Trả về image
        return StreamingResponse(
            BytesIO(data),
            media_type=content_type,
            headers={
                "Cache-Control": "public, max-age=3600",
                "Content-Disposition": f'inline; filename="{filename}"'
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi lấy logo: {str(e)}")

