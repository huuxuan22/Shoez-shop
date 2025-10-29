"""
Notification Model
Giải thích: Model để lưu notifications vào database
"""
from typing import Optional, Dict, Any
from pydantic import Field
from datetime import datetime

from model.mongodb_base_model import BaseMongoModel


class Notification(BaseMongoModel):
    """
    Notification Model
    - user_id: ID của user nhận notification
    - order_id: ID của đơn hàng liên quan
    - title: Tiêu đề notification
    - message: Nội dung notification
    - type: Loại notification (order_placed, order_confirmed, order_shipped, v.v.)
    - is_read: Đã đọc chưa
    - metadata: Dữ liệu bổ sung (JSON)
    """
    user_id: str
    order_id: Optional[str] = None
    title: str
    message: str
    type: str  
    is_read: bool = False
    metadata: Optional[Dict[str, Any]] = None

