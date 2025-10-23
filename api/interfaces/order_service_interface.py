from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from schemas.order_schemas import OrderCreateSchema


class IOrderService(ABC):
    """
    Interface cho OrderService
    Tuân thủ Dependency Inversion Principle
    """
    
    @abstractmethod
    async def create_order(self, order_data: OrderCreateSchema) -> Dict[str, Any]:
        """Tạo đơn hàng mới"""
        pass
    
    @abstractmethod
    async def get_orders_by_user(self, user_id: str) -> List[Dict[str, Any]]:
        """Lấy tất cả đơn hàng theo user"""
        pass
    
    @abstractmethod
    async def count_orders(self) -> int:
        """Đếm tổng số đơn hàng"""
        pass
    
    @abstractmethod
    async def count_orders_with_filter(self, filter_query: Dict[str, Any]) -> int:
        """Đếm tổng số đơn hàng với filter"""
        pass
    
    @abstractmethod
    async def get_orders_paginated(self, skip: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        """Lấy danh sách orders theo phân trang"""
        pass
    
    @abstractmethod
    async def get_orders_paginated_with_filter(
        self, 
        skip: int = 0, 
        limit: int = 20, 
        filter_query: Dict[str, Any] = None
    ) -> List[Dict[str, Any]]:
        """Lấy danh sách orders theo phân trang với filter"""
        pass
    
    @abstractmethod
    async def update_order_status(self, order_id: str, status: str) -> Optional[Dict[str, Any]]:
        """Cập nhật trạng thái đơn hàng"""
        pass
    
    @abstractmethod
    async def delete_multiple_orders(self, ids: List[str]) -> List[Dict]:
        """Xóa mềm nhiều đơn hàng"""
        pass
