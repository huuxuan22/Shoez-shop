from bson import ObjectId

from model import Product
from repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository[Product]):
    def __init__(self, db):
        super().__init__(db, 'products')

    async def update_images(self, product_id: str, image_urls: list[str]):
        result = await self.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": {"images": image_urls}}
        )
        return result.modified_count > 0

    async def get_by_id(self, product_id: str):
        return await self.find_one({"_id": ObjectId(product_id)})
