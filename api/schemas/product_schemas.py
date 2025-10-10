from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID
class Image(BaseModel):
    name: str
    url: List[str]

class SizeItem(BaseModel):
    size: int
    stock: int = 0

class ProductCreate(BaseModel):
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

class ProductResponse(ProductCreate):
    id: str
    rating: Optional[float] = 0.0
    total_reviews: Optional[int] = Field(0, alias="totalReviews")
    is_active: bool = True

class ProductUpdate(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    category: Optional[str]
    description: Optional[str]
    price: Optional[float]
    discount: Optional[float]
    stock: Optional[int]
    sizes: Optional[List[SizeItem]]
    images: Optional[List[str]]
    colors: Optional[List[str]]
