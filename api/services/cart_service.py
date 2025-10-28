from fastapi.encoders import jsonable_encoder
from typing import Dict, Any,List
from datetime import datetime
from model.cart_model import Cart
from repositories.cart_repository import CartRepository
from schemas.cart_schemas import CartCreateSchema, CartResponseSchema

class CartService:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    async def create_cart(self, cart_data: CartCreateSchema) -> Dict[str, Any]:
        """
        Tạo cart mới dựa trên CartCreateSchema
        """
        cart_dict = jsonable_encoder(cart_data)
        # Tính tổng tiền
        total = 0
        for item in cart_dict["items"]:
            price = item["product"]["price"]
            discount = item["product"].get("discount", 0)
            total += (price - discount) * item["quantity"]
        cart_dict["totalPrice"] = total
        cart_dict["createdAt"] = cart_dict["updatedAt"] = datetime.utcnow().isoformat()

        created_cart = await self.cart_repository.create(cart_dict)
        return created_cart

    async def add_item(self, user_id: str, item: Dict[str, Any]) -> CartResponseSchema:
        """
        Thêm item vào cart của user
        """
        updated_cart = await self.cart_repository.add_item_to_cart(user_id, item)
        if not updated_cart:
            return None
        return updated_cart

    async def get_cart_by_user(self, user_id: str):
        """
        Lấy cart theo user_id
        """
        cart = await self.cart_repository.get_by_user(user_id)
        if not cart:
            return None
        return cart

    async def delete_multiple_carts(self, ids: List[str]) -> List[dict]:
        # Trả về danh sách cart đã xóa
        deleted_carts = await self.cart_repository.delete_many_and_return(ids)
        return deleted_carts
