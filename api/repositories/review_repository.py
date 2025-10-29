from repositories.base_repository import BaseRepository
from model.review_model import Review
from bson import ObjectId
from typing import List, Dict, Any, Optional


class ReviewRepository(BaseRepository[Review]):
    def __init__(self, db):
        super().__init__(db, "reviews")  # collection name = "reviews"

    async def get_by_product(self, product_id: str, skip: int = 0, limit: int = 20) -> List[Dict]:
        """Lấy reviews theo product_id, chỉ lấy approved"""
        cursor = self.collection.find({
            "product_id": product_id,
            "status": "approved"
        }).sort("created_at", -1).skip(skip).limit(limit)
        
        reviews = await cursor.to_list(length=limit)
        return [self._convert_id(review) for review in reviews]

    async def count_by_product(self, product_id: str) -> int:
        """Đếm số reviews của sản phẩm"""
        return await self.collection.count_documents({
            "product_id": product_id,
            "status": "approved"
        })

    async def get_by_user(self, user_id: str) -> List[Dict]:
        """Lấy reviews của 1 user"""
        cursor = self.collection.find({"user_id": user_id}).sort("created_at", -1)
        reviews = await cursor.to_list(length=100)
        return [self._convert_id(review) for review in reviews]

    async def get_by_order(self, order_id: str) -> List[Dict]:
        """Lấy reviews theo order_id"""
        cursor = self.collection.find({"order_id": order_id})
        reviews = await cursor.to_list(length=100)
        return [self._convert_id(review) for review in reviews]

    async def check_user_reviewed(self, user_id: str, product_id: str, order_id: str):
        """Kiểm tra user đã review sản phẩm này trong đơn hàng này chưa
        Returns: Review object nếu có, None nếu không có"""
        existing = await self.collection.find_one({
            "user_id": user_id,
            "product_id": product_id,
            "order_id": order_id
        })
        return self._convert_id(existing) if existing else None

    async def update_helpful_count(self, review_id: str, increment: int = 1) -> Dict:
        """Tăng/giảm số lượt hữu ích"""
        from pymongo import ReturnDocument
        
        if not ObjectId.is_valid(review_id):
            return None
            
        updated = await self.collection.find_one_and_update(
            {"_id": ObjectId(review_id)},
            {"$inc": {"helpful_count": increment}},
            return_document=ReturnDocument.AFTER
        )
        return self._convert_id(updated) if updated else None

