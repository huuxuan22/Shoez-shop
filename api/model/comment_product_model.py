from typing import Optional
from pydantic import Field
from bson import ObjectId
from datetime import datetime

from model.mongodb_base_model import BaseMongoModel



class CommentProduct(BaseMongoModel):
    """
    Model cho comment/đánh giá sản phẩm
    """
    product_id: str = Field(..., description="ID của sản phẩm")
    user_id: str = Field(..., description="ID của người dùng")
    rating: float = Field(..., ge=0, le=5, description="Đánh giá từ 0-5 sao")
    comment: str = Field(..., min_length=1, description="Nội dung đánh giá")
    images: Optional[list[str]] = Field(default=[], description="Danh sách ảnh đi kèm")
    verified: bool = Field(default=False, description="Đã xác thực mua hàng chưa")
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "product_id": "507f1f77bcf86cd799439011",
                "user_id": "507f191e810c19729de860ea",
                "rating": 5.0,
                "comment": "Sản phẩm rất tốt, chất lượng cao, giao hàng nhanh",
                "images": [
                    "https://example.com/image1.jpg"
                ],
                "verified": True
            }
        }
        json_encoders = {
            ObjectId: lambda v: str(v),
            datetime: lambda v: v.isoformat()
        }
