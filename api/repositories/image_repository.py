from minio.error import S3Error
from typing import BinaryIO

from config.config import get_settings
from config.minio_client import minio_client

settings = get_settings()

class ImageRepository:
    def upload(self, file: BinaryIO, filename: str, content_type: str) -> str:
        try:
            minio_client.put_object(
                bucket_name=settings.minio_bucket,
                object_name=filename,
                data=file,
                length=-1,
                part_size=10*1024*1024,
                content_type=content_type,
            )
            return f"http://{settings.minio_url}/{settings.minio_bucket}/{filename}"
        except S3Error as e:
            raise Exception(f"Upload failed: {e}")
