from model.category_model import Category
from repositories.base_repository import BaseRepository
from bson import ObjectId
from fastapi import HTTPException


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db):
        super().__init__(db, 'categories')

    async def get_by_id(self, category_id: str):
        """Get category by ID"""
        try:
            obj_id = ObjectId(category_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid category ID")

        doc = await self.find_one({"_id": obj_id})
        if not doc:
            raise HTTPException(status_code=404, detail="Category not found")

        # Convert ObjectId sang str và đổi key từ "_id" -> "id"
        doc["id"] = str(doc["_id"])
        doc.pop("_id", None)

        return doc

    async def get_by_name(self, name: str):
        """Get category by name"""
        return await self.find_one({"name": name})

    async def get_all_active(self):
        """Get all active categories"""
        return await self.get_all(filter_query={"is_active": True})

