from typing import Optional
from pydantic import Field
from datetime import datetime
from model.mongodb_base_model import BaseMongoModel


class Review(BaseMongoModel):
    user_id: str
    product_id: str
    order_id: str
    rating: int = Field(ge=1, le=5)  # Điểm từ 1-5
    comment: str
    images: Optional[list] = []
    status: str = "pending"  # pending, approved, rejected
    helpful_count: int = 0
    user_name: Optional[str] = None  # Tên user để hiển thị
    admin_comments: Optional[list] = []  # Comments từ admin
    needs_attention: bool = False  # True nếu rating <= 3
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

