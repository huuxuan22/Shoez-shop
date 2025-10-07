import io
import uuid

from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi.responses import StreamingResponse,JSONResponse
from sqlalchemy.orm import Session, session

from services.product_service import ProductService
from services.s3_client import s3, calculate_prefix_size, settings

image_router = APIRouter(prefix='/image', tags=['/image'])

@image_router.post('')
async def upload_image(image: list[UploadFile] = File(...)):
    try:
        return JSONResponse(status_code=200, content={"url": "Đuợc của ló"})
    except ImportError:
        raise ImportError("Please install fastapi module")

@image_router.get('/download/{category}/{filename}')
async def download_image(category: str, filename: str):
    s3_key = f"{category}/{filename}"
    try:
        obj = s3.get_object(Bucket=settings.bucket_name, Key=s3_key)
        file_stream = io.BytesIO(obj["Body"].read())
        content_type = obj.get("ContentType","application/octet-stream")
        return StreamingResponse(content=file_stream, media_type=content_type)
    except Exception as e:
        return str(e)

@image_router.get('/prefix-size/{category}')
async def prefix_size(category: str):
    try:
        prefix = f"{category}/"
        # size = calculate_prefix_size(BUCKET_NAME, category)
        return JSONResponse(status_code=200, content={"prefix": prefix, "total_size_bytes": size})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})