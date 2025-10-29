from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from model.product_model import Product

class OrderCreateSchema(BaseModel):
    user_id: str
    status: Optional[str] = "pending"
    items: List[Dict[str, Any]] = []  
    fullName: str
    phone: str
    email: str
    address: str
    city: str
    district: str
    ward: str
    shippingFee: float
    shippingMethod: str
    note: Optional[str] = None
    total: float
    paymentMethod: Optional[str] = None
    estimatedDelivery: Optional[str] = None

class OrderResponseSchema(BaseModel):
    id: str
    uuid: Optional[str] = None
    user_id: str
    status: str = "pending"
    items: List[Dict[str, Any]] = []
    fullName: str
    phone: str
    email: str
    address: str
    city: str
    district: str
    ward: str
    shippingFee: float
    shippingMethod: str
    note: Optional[str] = None
    total: float
    paymentMethod: Optional[str] = None
    estimatedDelivery: Optional[str] = None
    created_at: str
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

class OrderUpdateStatusSchema(BaseModel):
    order_id: str = Field(..., description="ID đơn hàng")
    status: str = Field(..., description="Trạng thái mới của đơn hàng")

