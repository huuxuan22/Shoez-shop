from typing import List, Optional, Union
from pydantic import BaseModel, Field
from bson import ObjectId
from uuid import UUID, uuid4

from model.mongodb_base_model import BaseMongoModel


class SizeItem(BaseModel):
    size: int
    stock: int


class Product(BaseMongoModel):
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    price: float
    discount: Optional[float] = 0.0
    stock: Optional[int] = 0
    sizes: Optional[List[SizeItem]] = []
    images: Optional[List[str]] = []
    colors: Optional[List[str]] = []
    rating: Optional[float] = 0.0
    total_reviews: Optional[int] = Field(0, alias="totalReviews")
    is_active: bool = True  # dễ filter sản phẩm đang còn bán

    class Config:
        validate_by_name = True  # tên mới trong Pydantic v2
        from_attributes = True  # nếu bạn dùng ORM (MongoDB, SQLAlchemy, v.v.)
        json_encoders = {
            ObjectId: lambda v: str(v),
            UUID: lambda v: str(v),
        }
        json_schema_extra = {  # thay schema_extra
            "example": {
                "name": "Giày Nike Air Force 1",
                "brand": "Nike",
                "category": "Sneaker",
                "description": "Giày sneaker cổ điển, da trắng",
                "price": 2200000,
                "discount": 10,
                "stock": 150,
                "sizes": [
                    {"size": 38, "stock": 30},
                    {"size": 39, "stock": 50},
                    {"size": 40, "stock": 70}
                ],
                "images": [
                    "https://cdn.shop.com/products/airforce1-1.jpg",
                    "https://cdn.shop.com/products/airforce1-2.jpg",
                    "https://cdn.shop.com/products/airforce1-3.jpg"
                ],
                "colors": ["white", "black"],
                "rating": 4.8,
                "totalReviews": 320
            }
        }

