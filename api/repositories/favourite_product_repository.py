from model.favourite_product_model import FavouriteProductModel
from schemas.favourite_product_schemas import FavouriteProductCreateSchema, FavouriteProductResponseSchema
from config.database import get_database
from bson import ObjectId

class FavouriteProductRepository:
    def __init__(self):
        self.collection = get_database()["favourite_products"]

    def get_by_user(self, user_id: str):
        doc = self.collection.find_one({"user_id": user_id})
        return doc

    def add_product(self, user_id: str, product_id: str):
        doc = self.collection.find_one({"user_id": user_id})
        if doc:
            if product_id in doc["product"]:
                return False  # Đã có trong danh sách
            self.collection.update_one({"user_id": user_id}, {"$push": {"product": product_id}})
        else:
            self.collection.insert_one({"user_id": user_id, "product": [product_id]})
        return True

    def remove_product(self, user_id: str, product_id: str):
        self.collection.update_one({"user_id": user_id}, {"$pull": {"product": product_id}})
        return True
