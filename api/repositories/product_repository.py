from idlelib.iomenu import errors
from typing import Optional, Dict, Any, Union, List

from bson import ObjectId
from fastapi import HTTPException

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
        try:
            obj_id = ObjectId(product_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid product ID")

        doc = await self.find_one({"_id": obj_id})
        if not doc:
            raise HTTPException(status_code=404, detail="Product not found")

        # Convert ObjectId sang str và đổi key từ "_id" -> "id"
        doc["id"] = str(doc["_id"])
        doc.pop("_id", None)

        return doc

    async def get_products(
        self,
        filters: Optional[Dict[str, Any]] = None,
        skip: int = 0,
        limit: int = 10,
        sort: Optional[Union[str, List[tuple]]] = None  # thêm tham số sort
    ):
        query = filters or {}

        # Nếu sort được cung cấp
        sort_criteria = None
        if sort:
            if isinstance(sort, str):
                # mặc định giảm dần
                sort_criteria = [(sort, -1)]
            elif isinstance(sort, list):
                sort_criteria = sort  # danh sách tuple (field, direction)

        # Gọi hàm get_all (giả sử get_all có hỗ trợ sort)
        return await self.get_all(skip=skip, limit=limit, filter_query=query, sort=sort_criteria)

    # ví dụ get_all hỗ trợ sort
    async def get_all(
        self,
        skip: int = 0,
        limit: int = 10,
        filter_query: Optional[Dict[str, Any]] = None,
        sort: Optional[List[tuple]] = None
    ):
        cursor = self.collection.find(filter_query or {}).skip(skip).limit(limit)
        if sort:
            cursor = cursor.sort(sort)
        return await cursor.to_list(length=limit)

    async def get_distinct_categories(self) -> list[str]:
        """Return distinct category names from products collection."""
        categories = await self.collection.distinct("category")
        # Filter out falsy values and ensure str
        return [str(c).strip() for c in categories if c]

    async def delete_product(self, product_id: str) -> bool:
        try:
            obj_id = ObjectId(product_id)  # Chuyển string sang ObjectId
        except Exception:
            return False  # Nếu không phải ObjectId hợp lệ
        result = await self.collection.delete_one({"_id": obj_id})
        return result.deleted_count > 0

    async def get_product_by_id(self, product_id: str):
        try:
            obj_id = ObjectId(product_id)  # Chuyển string sang ObjectId
        except Exception:
            return None
        product = await self.collection.find_one({"_id": obj_id})
        return product

