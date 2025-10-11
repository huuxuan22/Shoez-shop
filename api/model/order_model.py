# from typing import List, Optional
# from pydantic import BaseModel, Field
# from bson import ObjectId
#
# from model import Product
# from model.mongodb_base_model import BaseMongoModel
#
# class CartItem(BaseModel):
#     product: Product   # Toàn bộ thông tin Product
#     quantity: int
#
# class Cart(BaseMongoModel):
#     userId: str
#     items: List[CartItem] = []
#     totalPrice: float = 0.0
