import uuid
from typing import List

from starlette.concurrency import run_in_threadpool

from repositories.image_repository import ImageRepository
from repositories.product_repository import ProductRepository



class ProductService:
    def __init__(self, image_repo: ImageRepository, product_repo: ProductRepository):
        self.image_repo = image_repo
        self.product_repo = product_repo

    async def upload_product_images(self, product_id: str, files: List):
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        uploaded_urls = []

        for upload_file in files:
            fileobj = upload_file.file
            fileobj.seek(0, 2)
            length = fileobj.tell()
            fileobj.seek(0)

            filename = f"{uuid.uuid4().hex}_{upload_file.filename}"

            url = await run_in_threadpool(
                self.image_repo.upload,
                fileobj,
                filename,
                upload_file.content_type
            )

            uploaded_urls.append(url)

        # Gộp ảnh cũ và mới
        existing_images = product.get("images", [])
        all_images = existing_images + uploaded_urls

        await self.product_repo.update_images(product_id, all_images)

        return {"product_id": product_id, "images": all_images}



