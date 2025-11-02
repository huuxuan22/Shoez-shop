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
            # Đảm bảo file ở đầu
            file.seek(0)
            
            # Đảm bảo bucket tồn tại
            if not minio_client.bucket_exists(bucket_name):
                minio_client.make_bucket(bucket_name)
            
            # Upload file
            minio_client.put_object(
                bucket_name=bucket_name,
                object_name=filename,
                data=file,
                length=-1,
                part_size=10*1024*1024,
                content_type=content_type,
            )
            
            # Tạo URL - ưu tiên dùng backend API endpoint để proxy images
            # Nếu là bucket "trademark" thì dùng brand logo endpoint
            if bucket_name == "trademark":
                backend_base = settings.backend_url.rstrip('/')
                api_prefix = settings.api_prefix
                url = f"{backend_base}{api_prefix}/brands/logo/{filename}"
            elif hasattr(settings, 'port_image') and settings.port_image:
                url = f"{settings.port_image}/{bucket_name}/{filename}"
            else:
                url = f"http://{settings.minio_url}/{bucket_name}/{filename}"
            
            return url
        except S3Error as e:
            error_msg = f"MinIO error: {str(e)}"
            raise Exception(error_msg)
        except Exception as e:
            error_msg = f"Upload error: {str(e)}"
            raise Exception(error_msg)
