from pymongo import ReturnDocument

from model.cart_model import Cart
from repositories.base_repository import BaseRepository
from typing import List, Dict, Any

class CartRepository(BaseRepository[Cart]):
    def __init__(self, db):
        super().__init__(db, "carts")  # collection name = "carts"

    async def get_by_user(self, user_id: str) -> Dict:
        """
        Lấy cart của 1 user (giả định mỗi user có 1 cart duy nhất)
        """
        cart = await self.collection.find_one({"userId": user_id})
        return self._convert_id(cart) if cart else None

    def _convert_id(self, cart: Dict) -> Dict:
        """Chuyển ObjectId thành string để trả về API"""
        if cart and "_id" in cart:
            cart["_id"] = str(cart["_id"])
        return cart

    async def add_item_to_cart(self, user_id: str, item: Dict[str, Any]) -> Dict:
        """
        Thêm 1 sản phẩm vào cart của user, tính toán lại totalPrice
        Nếu chưa có cart, tạo mới
        Lưu price và discount trực tiếp trong item thay vì lấy từ product
        """
        # Chuẩn bị dữ liệu item
        item_data = {
            "productId": item["product"]["_id"],
            "name": item["product"]["name"],
            "price": item["product"]["price"],
            "discount": item["product"].get("discount", 0),
            "quantity": item["quantity"]
        }

        # Lấy cart hiện tại
        cart = await self.collection.find_one({"userId": user_id})
        if not cart:
            # Tạo cart mới
            new_cart = {
                "userId": user_id,
                "items": [item_data],
                "totalPrice": (item_data["price"] - item_data["discount"]) * item_data["quantity"],
                "createdAt": self._get_current_timestamp(),
                "updatedAt": self._get_current_timestamp()
            }
            result = await self.collection.insert_one(new_cart)
            new_cart["_id"] = result.inserted_id
            return self._convert_id(new_cart)

        # Nếu đã có cart, thêm item
        items = cart.get("items", [])
        items.append(item_data)

        # Tính lại tổng giá
        total = sum((i["price"] - i.get("discount", 0)) * i["quantity"] for i in items)

        updated_cart = await self.collection.find_one_and_update(
            {"_id": cart["_id"]},
            {
                "$set": {
                    "items": items,
                    "totalPrice": total,
                    "updatedAt": self._get_current_timestamp()
                }
            },
            return_document=ReturnDocument.AFTER
        )

        return self._convert_id(updated_cart)
