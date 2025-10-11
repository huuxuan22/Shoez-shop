from typing import List, Optional
from pydantic import BaseModel, Field
from model.product_model import Product

class OrderCreateSchema(BaseModel):
    user_id: str
    status: Optional[str] = "pending"
    products: List[Product] = []

class OrderResponseSchema(BaseModel):
    id: str
    uuid: str
    user_id: str
    status: bool = True
    products: List[Product]
    created_at: str
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

class OrderUpdateStatusSchema(BaseModel):
    order_id: str = Field(..., description="ID đơn hàng")
    status: str = Field(..., description="Trạng thái mới của đơn hàng")

