from minio.error import S3Error
from typing import BinaryIO

from config.config import get_settings
from config.minio_client import minio_client

settings = get_settings()

class ImageRepository:
    def upload(self, file: BinaryIO, filename: str, content_type: str) -> str:
        """Upload vào bucket mặc định (cho backward compatibility)"""
        return self.upload_to_bucket(file, filename, content_type, settings.minio_bucket)
    
    def upload_to_bucket(self, file: BinaryIO, filename: str, content_type: str, bucket_name: str) -> str:
        """Upload vào bucket chỉ định"""
        try:
            file.seek(0)
            
            if not minio_client.bucket_exists(bucket_name):
                minio_client.make_bucket(bucket_name)
            
            minio_client.put_object(
                bucket_name=bucket_name,
                object_name=filename,
                data=file,
                length=-1,
                part_size=10*1024*1024,
                content_type=content_type,
            )
            
            return f"{bucket_name}/{filename}"
        except S3Error as e:
            error_msg = f"MinIO error: {str(e)}"
            raise Exception(error_msg)
        except Exception as e:
            error_msg = f"Upload error: {str(e)}"
            raise Exception(error_msg)
