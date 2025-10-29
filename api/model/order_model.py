from typing import List, Optional, Dict, Any
from pydantic import Field
from datetime import datetime

from model import Product
from model.mongodb_base_model import BaseMongoModel


class Order(BaseMongoModel):
    user_id: str
    status: str = "pending"
    items: List[Dict[str, Any]] = []  # Danh sách sản phẩm với thông tin chi tiết
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
