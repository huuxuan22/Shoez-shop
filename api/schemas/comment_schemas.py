from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class CommentCreate(BaseModel):
    """
    Schema để tạo comment mới
    """
    product_id: str
    rating: float = Field(..., ge=0, le=5, description="Đánh giá từ 0-5 sao")
    comment: str = Field(..., min_length=1, description="Nội dung đánh giá")
    images: Optional[list[str]] = Field(default=[], description="Danh sách ảnh đi kèm")

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": "507f1f77bcf86cd799439011",
                "rating": 5.0,
                "comment": "Sản phẩm rất tốt, chất lượng cao!",
                "images": ["https://example.com/image1.jpg"]
            }
        }


class CommentUpdate(BaseModel):
    """
    Schema để cập nhật comment
    """
    rating: Optional[float] = Field(None, ge=0, le=5)
    comment: Optional[str] = Field(None, min_length=1)
    images: Optional[list[str]] = None


class CommentResponse(BaseModel):
    """
    Schema trả về comment đầy đủ thông tin
    """
    id: str
    product_id: str
    user_id: str
    user_name: str
    user_avatar: Optional[str]
    rating: float
    comment: str
    images: list[str]
    verified: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "product_id": "507f191e810c19729de860ea",
                "user_id": "507f1f77bcf86cd799439012",
                "user_name": "Nguyễn Văn A",
                "user_avatar": "https://example.com/avatar.jpg",
                "rating": 5.0,
                "comment": "Sản phẩm rất tốt!",
                "images": ["https://example.com/image1.jpg"],
                "verified": True,
                "created_at": "2024-01-15T10:30:00",
                "updated_at": None
            }
        }


class CommentListResponse(BaseModel):
    """
    Schema trả về danh sách comments
    """
    comments: list[CommentResponse]
    total: int
    page: int
    limit: int
    total_pages: int

