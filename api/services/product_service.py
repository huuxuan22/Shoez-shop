import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from model import ProductImages
from services.s3_client import s3, settings

from repositories.product_image_repository import ProductImagesRepository


class ProductService:
    def __init__(self, db: Session):
        self.db = db
        self.product_images_repository = ProductImagesRepository(db)

    def upload_files(self, files: list[UploadFile] = None):
        if files is None:
            files = []

        for file in files:
            file_name = file.filename
            object_key = f"/Streetwear/{uuid.UUID}-{file_name}"

            s3.upload_fileobj(file.file, settings.bucket_name, object_key)

            file_url = f"http://localhost:9000/{settings.bucket_name}/{object_key}"

            new_product_image = ProductImages(
                ile_name=file_name,
                file_url = file_url,
                object_key = object_key
            )

            self.product_images_repository.session.add(new_product_image)
            self.product_images_repository.session.commit()

    def get_all_object_by_object_key(self):
        product_images = self.product_images_repository.session.query(ProductImages).all()
        result = []

        for image in product_images:
            # Lấy object_key từ DB
            object_key = image.object_key

            # Lấy metadata từ MinIO bằng boto3
            try:
                response = s3.head_object(
                    Bucket=settings.bucket_name,
                    Key=object_key
                )
                size = response["ContentLength"]  # bytes
            except Exception as e:
                size = None  # Nếu file không tồn tại hoặc lỗi

            result.append({
                "id": image.id,
                "ile_name": image.file_name,
                "object_key": object_key,
                "file_url": image.file_url,
                "size": size
            })

        return result
