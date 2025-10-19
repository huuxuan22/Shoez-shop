from uuid import UUID
from urllib.parse import urlparse
from sqlalchemy.testing.suite.test_reflection import users
from passlib.context import CryptContext
from minio import Minio
from minio.error import S3Error
import os
import uuid
from datetime import timedelta
from fastapi import UploadFile, HTTPException

# Tạo context bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
def convert_uuid_to_str(data):
    if isinstance(data, dict):
        return {k: convert_uuid_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_uuid_to_str(i) for i in data]
    elif isinstance(data, UUID):
        return str(data)
    else:
        return data

async def replace_avatar(
    minio_client: Minio,
    bucket_name: str,
    old_avatar_url: str,  # URL avatar cũ, nếu có
    new_file: UploadFile
) -> str:
    """
    Xóa avatar cũ (nếu có), upload file mới lên MinIO, trả về URL mới
    """
    try:
        # Tạo bucket nếu chưa tồn tại
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Xóa avatar cũ
        if old_avatar_url:
            # Lấy object_name từ URL, loại bỏ query string
            parsed_url = urlparse(old_avatar_url)
            object_name = os.path.basename(parsed_url.path)
            try:
                minio_client.remove_object(bucket_name, object_name)
            except S3Error:
                # Nếu object không tồn tại thì bỏ qua
                pass

        # Tạo tên file mới duy nhất
        file_extension = os.path.splitext(new_file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"

        # Upload file mới
        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=unique_filename,
            data=new_file.file,
            length=-1,  
            part_size=10*1024*1024
        )

        new_avatar_url = minio_client.get_presigned_url(
            "GET",
            bucket_name=bucket_name,
            object_name=unique_filename,
            expires=timedelta(days=7)
        )

        return new_avatar_url

    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Upload avatar thất bại: {str(e)}")