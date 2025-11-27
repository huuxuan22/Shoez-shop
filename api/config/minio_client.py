from config.config import get_settings
from minio import Minio
settings = get_settings()

class MinioClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = Minio(
                endpoint=settings.minio_url,
                access_key=settings.minio_access_key,
                secret_key=settings.minio_secret_key,
                secure=settings.minio_secure,
            )
        return cls._instance

minio_client = MinioClient()
