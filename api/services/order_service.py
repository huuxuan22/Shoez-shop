from typing import List, Dict, Any, Optional
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from bson import ObjectId
from repositories.order_repository import OrderRepository
from schemas.order_schemas import OrderCreateSchema, OrderResponseSchema
from interfaces.order_service_interface import IOrderService


class OrderService(IOrderService):
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def _serialize_for_json(self, data: Any) -> Any:
        """
        Convert ObjectId và datetime để có thể serialize thành JSON
        """
        if isinstance(data, ObjectId):
            return str(data)
        elif isinstance(data, datetime):
            return data.isoformat()
        elif isinstance(data, dict):
            return {key: self._serialize_for_json(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self._serialize_for_json(item) for item in data]
        else:
            return data

    async def create_order(self, order_data: OrderCreateSchema) -> Dict[str, Any]:
        """
        Tạo đơn hàng mới
        """
        order_dict = jsonable_encoder(order_data)
        order_dict["created_at"] = order_dict["updated_at"] = datetime.utcnow()
        created_order = await self.order_repo.create(order_dict)
        return created_order

    async def get_orders_by_user(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Lấy tất cả đơn hàng theo user
        """
        orders = await self.order_repo.get_by_user(user_id)
        return self._serialize_for_json(orders)

    async def delete_multiple_orders(self, ids: List[str]) -> List[Dict]:
        """
        Xóa mềm nhiều đơn hàng
        """
        deleted_orders = await self.order_repo.soft_delete_by_ids(ids)
        return deleted_orders

    async def count_orders(self) -> int:
        """Đếm tổng số đơn hàng"""
        return await self.order_repo.count({})

    async def get_orders_paginated(self, skip: int = 0, limit: int = 20):
        """Lấy danh sách orders theo phân trang, sắp xếp theo created_at DESC"""
        orders = await self.order_repo.get_all(
            skip=skip,
            limit=limit,
            filter_query={},
        )
        # Sắp xếp gần nhất trước
        orders.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return self._serialize_for_json(orders)

    async def count_orders_with_filter(self, filter_query: Dict[str, Any]) -> int:
        """Đếm tổng số đơn hàng với filter"""
        return await self.order_repo.count(filter_query)

    async def get_orders_paginated_with_filter(self, skip: int = 0, limit: int = 20, filter_query: Dict[str, Any] = None):
        """Lấy danh sách orders theo phân trang với filter, sắp xếp theo created_at DESC"""
        if filter_query is None:
            filter_query = {}
            
        orders = await self.order_repo.get_all(
            skip=skip,
            limit=limit,
            filter_query=filter_query,
        )
        # Sắp xếp gần nhất trước
        orders.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return self._serialize_for_json(orders)

    async def update_order_status(self, order_id: str, status: str) -> Optional[Dict[str, Any]]:
        """
        Cập nhật trạng thái đơn hàng
        """
        # Lấy order hiện tại
        order = await self.order_repo.get_by_id(order_id)
        if not order:
            return None

        # Kiểm tra chuyển trạng thái hợp lệ
        current_status = order.get("status")
        if current_status == "pending" and status.lower() == "complete":
            updated_order = await self.order_repo.update(order_id, {"status": "complete"})
            return updated_order
        return None

