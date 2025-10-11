from typing import List, Dict, Any, Optional
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from repositories.order_repository import OrderRepository
from schemas.order_schemas import OrderCreateSchema, OrderResponseSchema


class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

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

        # chuyển datetime sang isoformat
        for o in orders:
            o["created_at"] = o["created_at"].isoformat() if isinstance(o["created_at"], datetime) else o["created_at"]
            o["updated_at"] = o["updated_at"].isoformat() if isinstance(o["updated_at"], datetime) else o["updated_at"]

        return orders

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
        return orders

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

