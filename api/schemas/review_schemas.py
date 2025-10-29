from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ReviewCreateSchema(BaseModel):
    """Schema để tạo review mới"""
    product_id: str
    order_id: str
    rating: int = Field(..., ge=1, le=5, description="Điểm đánh giá từ 1-5")
    comment: str = Field(..., min_length=10, description="Nội dung đánh giá (tối thiểu 10 ký tự)")
    images: Optional[List[str]] = []


class ReviewUpdateSchema(BaseModel):
    """Schema để update review"""
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = Field(None, min_length=10)
    images: Optional[List[str]] = None


class ReviewResponseSchema(BaseModel):
    """Schema để trả về review"""
    id: str
    user_id: str
    product_id: str
    order_id: str
    rating: int
    comment: str
    images: List[str]
    status: str
    helpful_count: int
    user_name: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ReviewListResponseSchema(BaseModel):
    """Schema để trả về danh sách reviews với pagination"""
    reviews: List[ReviewResponseSchema]
    total: int
    page: int
    limit: int

