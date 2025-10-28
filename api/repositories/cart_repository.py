from pymongo import ReturnDocument

from model.cart_model import Cart
from bson import ObjectId
from repositories.base_repository import BaseRepository
from typing import List, Dict, Any

class CartRepository(BaseRepository[Cart]):
    def __init__(self, db):
        super().__init__(db, "carts")  # collection name = "carts"

    async def get_by_user(self, user_id: str) -> Dict:
        """
        Lấy cart của 1 user (giả định mỗi user có 1 cart duy nhất)
        """
        # Hỗ trợ cả key cũ (userId) và mới (user_id)
        cart = await self.collection.find_one({"$or": [{"user_id": user_id}, {"userId": user_id}]})
        return self._convert_id(cart) if cart else None

    def _convert_id(self, cart: Dict) -> Dict:
        """Chuyển ObjectId thành string để trả về API"""
        if cart and "_id" in cart:
            cart["_id"] = str(cart["_id"])
        return cart

    async def add_item_to_cart(self, user_id: str, item: Dict[str, Any]) -> Dict:
        """
        Thêm 1 sản phẩm vào cart của user, gộp item trùng (product/size/color)
        Chuẩn hoá:
        - Chỉ dùng trường quality (nếu nhận quantity thì map sang quality)
        - Luôn có user_id trong document
        - Giữ product đã join để hiển thị
        """
        product_id = item.get("product_id") or item.get("productId")
        if not product_id:
            raise ValueError("product_id is required")
        try:
            obj_id = ObjectId(product_id)
        except Exception:
            raise ValueError("Invalid product_id")

        product_doc = await self.db["products"].find_one({"_id": obj_id})
        if not product_doc:
            raise ValueError("Product not found")

        product_serialized = self._convert_id(product_doc)

        # Hỗ trợ cả "quantity" và "quality"; ưu tiên quality
        qty = int(item.get("quality") or item.get("quantity") or 1)
        size = item.get("size")
        color = item.get("color")

        item_data = {
            "product": product_serialized,
            "size": size,
            "color": color,
            "quality": qty
        }

        # Lấy cart hiện tại
        cart = await self.collection.find_one({"$or": [{"user_id": user_id}, {"userId": user_id}]})
        if not cart:
            # Tạo cart mới
            new_cart = {
                "user_id": user_id,
                "items": [item_data],
                "totalPrice": (product_serialized.get("price", 0) - product_serialized.get("discount", 0)) * qty,
                "createdAt": self._get_current_timestamp(),
                "updatedAt": self._get_current_timestamp()
            }
            result = await self.collection.insert_one(new_cart)
            new_cart["_id"] = result.inserted_id

            return self._convert_id(new_cart)

        # Nếu đã có cart, thêm item
        items = cart.get("items", [])
        # Gộp item trùng khóa (product.id + size + color)
        merged = False
        for i in items:
            prod = i.get("product") or {}
            pid = prod.get("id") or prod.get("_id")
            if pid == product_serialized.get("id") and i.get("size") == size and i.get("color") == color:
                # Chuẩn hoá về quality; nếu có quantity cũ thì cộng dồn và xoá
                existed_q = i.get("quality") or i.get("quantity") or 0
                try:
                    existed_q = int(existed_q)
                except Exception:
                    existed_q = 0
                i["quality"] = existed_q + qty
                if "quantity" in i:
                    del i["quantity"]
                merged = True
                break
        if not merged:
            items.append(item_data)

        # Tính lại tổng giá
        def item_total(i: Dict[str, Any]) -> float:
            prod = i.get("product") or {}
            price = prod.get("price", 0)
            discount = prod.get("discount", 0)
            q = i.get("quality") or i.get("quantity") or 0
            try:
                q = int(q)
            except Exception:
                q = 0
            return (price - discount) * q

        total = sum(item_total(i) for i in items)

        # Bổ sung user_id nếu cart cũ chưa có (chuẩn hoá khoá)
        set_fields = {
            "items": items,
            "totalPrice": total,
            "updatedAt": self._get_current_timestamp()
        }
        if not cart.get("user_id"):
            set_fields["user_id"] = user_id

        updated_cart = await self.collection.find_one_and_update(
            {"_id": cart["_id"]},
            {"$set": set_fields},
            return_document=ReturnDocument.AFTER
        )

        # Đảm bảo _id được convert sang id (str) cho toàn bộ document
        return self._convert_id(updated_cart)

    async def remove_item_from_cart(self, user_id: str, product_id: str, size: Any, color: str) -> Dict:
        """
        Xoá 1 item (product/size/color) khỏi cart của user và tính lại totalPrice
        """
        # Tìm cart theo user
        cart = await self.collection.find_one({"$or": [{"user_id": user_id}, {"userId": user_id}]})
        if not cart:
            return None

        items = cart.get("items", [])
        new_items: List[Dict[str, Any]] = []

        def product_matches(item: Dict[str, Any]) -> bool:
            prod = item.get("product") or {}
            pid = prod.get("id") or prod.get("_id")
            return pid == product_id and item.get("size") == size and item.get("color") == color

        removed = False
        for i in items:
            if product_matches(i):
                removed = True
                continue
            new_items.append(i)

        if not removed:
            return self._convert_id(cart)

        def item_total(i: Dict[str, Any]) -> float:
            prod = i.get("product") or {}
            price = prod.get("price", 0)
            discount = prod.get("discount", 0)
            q = i.get("quality") or i.get("quantity") or 0
            try:
                q = int(q)
            except Exception:
                q = 0
            return (price - discount) * q

        total = sum(item_total(i) for i in new_items)

        updated_cart = await self.collection.find_one_and_update(
            {"_id": cart["_id"]},
            {"$set": {"items": new_items, "totalPrice": total, "updatedAt": self._get_current_timestamp()}},
            return_document=ReturnDocument.AFTER
        )

        return self._convert_id(updated_cart)