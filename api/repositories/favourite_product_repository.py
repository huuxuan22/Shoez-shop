
from schemas.favourite_product_schemas import FavouriteProductCreateSchema, FavouriteProductResponseSchema
from config.database import get_database
from utils.logger import logger


class FavouriteProductRepository:
    @property
    def collection(self):
        database = get_database()
        if database is None:
            raise RuntimeError("Database is not initialized. Ensure startup connected to MongoDB.")
        return database["favourite_products"]

    async def get_by_user(self, user_id: str):
        document = await self.collection.find_one({"user_id": user_id})
        if document:
            product_count = len(document.get("product", []))
            logger.info(f"Found {product_count} favourite products for user {user_id}")
        else:
            logger.info(f"No favourites found for user {user_id}")
        return document

    async def add_product(self, user_id: str, product_id: str):
        logger.info(f"[FavouriteProductRepository] add_product: user_id={user_id}, product_id={product_id}")
        existing = await self.collection.find_one({"user_id": user_id})
        if existing:
            products = existing.get("product") or []
            if product_id in products:
                logger.info(f"Product {product_id} already in favourites")
                return False
            # Sử dụng $addToSet để tránh trùng lặp (optional thêm an toàn)
            await self.collection.update_one(
                {"user_id": user_id}, 
                {"$addToSet": {"product": product_id}}
            )
            logger.info(f"Added product {product_id} to favourites. Total: {len(products) + 1}")
        else:
            await self.collection.insert_one({"user_id": user_id, "product": [product_id]})
            logger.info(f"Created new favourite list for user {user_id}")
        return True

    async def remove_product(self, user_id: str, product_id: str):
        result = await self.collection.update_one({"user_id": user_id}, {"$pull": {"product": product_id}})
        if result.modified_count > 0:
            logger.info(f"Removed product {product_id} from user {user_id} favourites")
        else:
            logger.info(f"Product {product_id} not found in user {user_id} favourites")
        return True
