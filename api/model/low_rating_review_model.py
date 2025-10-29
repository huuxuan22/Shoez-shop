from datetime import datetime
from typing import Optional
from model.mongodb_base_model import BaseMongoModel


class LowRatingReview(BaseMongoModel):
    review_id: str
    product_id: str
    user_id: str
    user_name: Optional[str] = None
    rating: int  # 1, 2, hoặc 3
    comment: str
    status: str = "pending"  # pending, responded, resolved
    admin_response: bool = False  # Admin đã phản hồi hay chưa
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

