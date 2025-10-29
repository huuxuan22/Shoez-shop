from typing import List, Dict, Any
from repositories.low_rating_review_repository import LowRatingReviewRepository
from config.database import get_database
from datetime import datetime


class LowRatingReviewService:
    def __init__(self, low_rating_repo: LowRatingReviewRepository):
        self.low_rating_repo = low_rating_repo

    async def create_low_rating_review(self, review: Dict[str, Any]) -> Dict[str, Any]:
        """Tạo low rating review record"""
        review_data = {
            "review_id": str(review.get("id") or review.get("_id")),
            "product_id": review.get("product_id"),
            "user_id": review.get("user_id"),
            "user_name": review.get("user_name"),
            "rating": review.get("rating"),
            "comment": review.get("comment"),
            "created_at": datetime.utcnow()
        }
        
        # Check xem đã có chưa (tránh duplicate)
        existing = await self.low_rating_repo.get_by_review_id(review_data["review_id"])
        if existing:
            return existing
        
        created = await self.low_rating_repo.create_low_rating_review(review_data)
        return created

    async def get_unresolved_reviews(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Lấy danh sách reviews chưa resolved"""
        reviews = await self.low_rating_repo.get_unresolved_reviews(limit)
        return self._serialize_for_json(reviews)

    async def mark_as_responded(self, review_id: str) -> bool:
        """Đánh dấu admin đã phản hồi"""
        return await self.low_rating_repo.mark_as_responded(review_id)

    def _serialize_for_json(self, data: Any) -> Any:
        """Convert MongoDB ObjectId và datetime thành string"""
        from bson import ObjectId
        from datetime import date
        
        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                if isinstance(value, ObjectId):
                    result[key] = str(value)
                elif isinstance(value, (datetime, date)):
                    result[key] = value.isoformat()
                elif isinstance(value, dict):
                    result[key] = self._serialize_for_json(value)
                elif isinstance(value, list):
                    result[key] = [self._serialize_for_json(item) for item in value]
                else:
                    result[key] = value
            return result
        elif isinstance(data, list):
            return [self._serialize_for_json(item) for item in data]
        else:
            return data


def get_low_rating_review_service() -> LowRatingReviewService:
    """Dependency injection cho LowRatingReviewService"""
    from repositories.low_rating_review_repository import LowRatingReviewRepository
    return LowRatingReviewService(LowRatingReviewRepository(get_database()))

