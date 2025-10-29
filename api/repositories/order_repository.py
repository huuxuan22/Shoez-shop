from model import Order
from repositories.base_repository import BaseRepository
from bson import ObjectId
from pymongo import ReturnDocument
from typing import List, Dict, Any

class OrderRepository(BaseRepository[Order]):
    def __init__(self, db):
        super().__init__(db, "orders")  # collection name = "orders"

    async def get_by_user(self, user_id: str) -> Dict:
        """
        Lấy tất cả đơn hàng của 1 user
        """
        orders_cursor = self.collection.find({"user_id": user_id}).sort("created_at", -1)
        orders = await orders_cursor.to_list(length=100)
        return [self._convert_id(order) for order in orders]

    async def count_orders(self) -> int:
        """Đếm tổng số đơn hàng"""
        return await self.db.count({})

    async def add_product_to_order(self, order_id: str, product: Dict[str, Any]) -> Dict:
        """
        Thêm sản phẩm vào đơn hàng
        """
        order = await self.collection.find_one({"_id": ObjectId(order_id)})
        if not order:
            return None

        items = order.get("items", [])
        items.append(product)

        updated_order = await self.collection.find_one_and_update(
            {"_id": ObjectId(order_id)},
            {"$set": {"items": items, "updated_at": self._get_current_timestamp()}},
            return_document=ReturnDocument.AFTER
        )
        return self._convert_id(updated_order)
