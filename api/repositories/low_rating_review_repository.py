from repositories.base_repository import BaseRepository
from model.low_rating_review_model import LowRatingReview
from typing import List, Dict, Any, Optional
from datetime import datetime


class LowRatingReviewRepository(BaseRepository[LowRatingReview]):
    def __init__(self, db):
        super().__init__(db, "low_rating_reviews")

    async def get_unresolved_reviews(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Lấy danh sách reviews chưa resolved"""
        cursor = self.collection.find({"status": "pending"}).sort("created_at", -1).limit(limit)
        reviews = await cursor.to_list(length=limit)
        return [self._convert_id(review) for review in reviews]

    async def get_by_review_id(self, review_id: str) -> Optional[Dict[str, Any]]:
        """Tìm low rating review theo review_id"""
        review = await self.collection.find_one({"review_id": review_id})
        return self._convert_id(review) if review else None

    async def mark_as_responded(self, review_id: str) -> bool:
        """Đánh dấu admin đã phản hồi"""
        result = await self.collection.update_many(
            {"review_id": review_id},
            {"$set": {"status": "responded", "admin_response": True, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0

    async def create_low_rating_review(self, data: dict) -> Dict[str, Any]:
        """Tạo low rating review mới"""
        data["status"] = "pending"
        data["admin_response"] = False
        data["created_at"] = data.get("created_at") or datetime.utcnow()
        created = await self.collection.insert_one(data)
        data["_id"] = created.inserted_id
        return self._convert_id(data)

