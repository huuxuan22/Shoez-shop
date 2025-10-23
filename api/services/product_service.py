import uuid
from typing import List, Optional, Dict

from bson import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from multipart import p
from starlette.concurrency import run_in_threadpool

from repositories.image_repository import ImageRepository
from repositories.product_repository import ProductRepository
from schemas.product_schemas import ProductCreate, ProductResponse, ProductUpdate


class ProductService:
    def __init__(self, image_repo: ImageRepository = None, product_repo: ProductRepository = None):
        self.image_repo = image_repo
        self.product_repo = product_repo

    async def upload_product_images(self, product_id: str, files: List):
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        uploaded_urls = []

        for upload_file in files:
            fileobj = upload_file.file
            fileobj.seek(0, 2)
            length = fileobj.tell()
            fileobj.seek(0)

            filename = f"{uuid.uuid4().hex}_{upload_file.filename}"

            url = await run_in_threadpool(
                self.image_repo.upload,
                fileobj,
                filename,
                upload_file.content_type
            )

            uploaded_urls.append(url)

        # Gộp ảnh cũ và mới
        existing_images = product.get("images", [])
        all_images = existing_images + uploaded_urls

        await self.product_repo.update_images(product_id, all_images)

        return {"product_id": product_id, "images": all_images}

    async def create_product(self, product_create: ProductCreate) -> ProductResponse:
        product_dict = product_create.model_dump()
        # Set default fields
        product_dict["rating"] = 0.0
        product_dict["total_reviews"] = 0
        product_dict["is_active"] = True

        created_doc = await self.product_repo.create(product_dict)
        # Chuyển về schema response
        return ProductResponse(**created_doc)

    async def list_products(
        self,
        skip: int = 0,
        limit: int = 10,
        name: Optional[str] = None,
        brand: Optional[str] = None,
        category: Optional[str] = None
    ) -> List[ProductResponse]:
        # --- 1️⃣ Tạo bộ lọc ---
        filters = {}
        if name:
            filters["name"] = {"$regex": name, "$options": "i"}  # i = ignore case
        if brand:
            filters["brand"] = {"$regex": brand, "$options": "i"}
        if category:
            filters["category"] = {"$regex": category, "$options": "i"}

        products = await self.product_repo.get_products(
            filters=filters, skip=skip, limit=limit
        )

        converted_products = []
        for p in products:
            p_dict = dict(p)
            if "_id" in p_dict:
                p_dict["id"] = str(p_dict["_id"])
                del p_dict["_id"]
            converted_products.append(p_dict)

        return [ProductResponse(**p) for p in converted_products]


    async def get_top_rated_products(self, limit: int = 8) -> List[ProductResponse]:
        products = await self.product_repo.get_products(
            filters={},
            skip=0,
            limit=limit,
            sort=[("rating", -1), ("totalReviews", -1)]
        )
        products_dicts = [
            {**product, "id": str(product["_id"])}  # convert _id → id
            for product in products
        ]
        return [ProductResponse(**product) for product in products_dicts]

    async def get_top_rated_by_brand(self, brand: str, limit: int = 8) -> List[ProductResponse]:
        filters = {"brand": brand}
        products = await self.product_repo.get_products(
            filters=filters,
            skip=0,
            limit=limit,
            sort=[("rating", -1), ("totalReviews", -1)]
        )
        products_dicts = [
            {**product, "id": str(product["_id"])}  # convert _id → id
            for product in products
        ]
        return [ProductResponse(**p) for p in products_dicts]

    async def delete_product(self, product_id: str) -> bool:
        return await self.product_repo.delete_product(product_id)

    async def get_product_detail(self, product_id: str):
        return await self.product_repo.get_by_id(product_id)

    async def update_product(self, product_id: str, data: dict):
        try:
            obj_id = ObjectId(product_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid product ID")

        update_data = jsonable_encoder(data)
        result = await self.product_repo.collection.update_one(
            {"_id": obj_id},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")
        updated_product = await self.product_repo.collection.find_one({"_id": obj_id})
        if not updated_product:
            raise HTTPException(status_code=404, detail="Product not found after update")
        # Convert _id ObjectId to string and rename key to `id`
        updated_product["id"] = str(updated_product["_id"])
        updated_product.pop("_id")

        return updated_product





