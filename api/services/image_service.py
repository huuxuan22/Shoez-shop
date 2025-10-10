from config.config import get_settings
from config.minio_client import minio_client
from repositories.image_repository import ImageRepository

settings = get_settings()

class ImageService:
    def __init__(self, repository: ImageRepository):
        self.repository = repository
        self.client = minio_client

    def upload(self, fileobj, length: int, filename: str, content_type: str) -> str:
        self.client.put_object(
            bucket_name=settings.minio_bucket,
            object_name=filename,
            data=fileobj,
            length=length,
            content_type=content_type
        )
        return f"{settings.port_image}/{settings.minio_bucket}/{filename}"
