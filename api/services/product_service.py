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
    def __init__(self, image_repo: ImageRepository = None, product_repo: ProductRepository = None, comment_repo=None):
        self.image_repo = image_repo
        self.product_repo = product_repo
        self.comment_repo = comment_repo

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

    async def create_product(self, product_create: ProductCreate) -> Dict:
        product_dict = product_create.model_dump()
        product_dict["rating"] = 0.0
        product_dict["totalReviews"] = 0  
        product_dict["is_active"] = True

        created_doc = await self.product_repo.create(product_dict)
        # Trả về dữ liệu thô từ database
        return created_doc

    async def list_products(
        self,
        skip: int = 0,
        limit: int = 10,
        name: Optional[str] = None,
        brand: Optional[str] = None,
        category: Optional[str] = None,
        min_rating: Optional[float] = None,
        max_rating: Optional[float] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        color: Optional[str] = None,
        size: Optional[int] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"
    ) -> Dict:
        filters = {}
        if name:
            filters["name"] = {"$regex": name, "$options": "i"}  
        if brand:
            filters["brand"] = {"$regex": brand, "$options": "i"}
        if category:
            filters["category"] = {"$regex": category, "$options": "i"}
        
        # Filter theo rating
        if min_rating is not None or max_rating is not None:
            rating_filter = {}
            if min_rating is not None:
                rating_filter["$gte"] = min_rating
            if max_rating is not None:
                rating_filter["$lte"] = max_rating
            filters["rating"] = rating_filter
        
        # Filter theo giá
        if min_price is not None or max_price is not None:
            price_filter = {}
            if min_price is not None:
                price_filter["$gte"] = min_price
            if max_price is not None:
                price_filter["$lte"] = max_price
            filters["price"] = price_filter
        
        # Filter theo màu sắc
        if color:
            filters["colors"] = {"$regex": color, "$options": "i"}
        
        # Filter theo size - vì sizes là array of objects {size: int, stock: int}
        if size is not None:
            filters["sizes.size"] = size

        # Lấy tổng số sản phẩm
        total = await self.product_repo.count(filters)
        
        # Tạo sort criteria
        sort_direction = -1 if sort_order == "desc" else 1
        sort_criteria = [(sort_by, sort_direction)]
        
        # Lấy danh sách sản phẩm với sort
        products = await self.product_repo.get_products(
            filters=filters, skip=skip, limit=limit, sort=sort_criteria
        )

        # Trả về dữ liệu thô từ database
        converted_products = []
        for p in products:
            p_dict = dict(p)
            if "_id" in p_dict:
                p_dict["id"] = str(p_dict["_id"])
                del p_dict["_id"]
            converted_products.append(p_dict)

        # Tính toán phân trang
        total_pages = (total + limit - 1) // limit  # Ceiling division

        return {
            "products": converted_products,
            "total": total,
            "page": (skip // limit) + 1,
            "limit": limit,
            "total_pages": total_pages
        }


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

    async def get_product_detail(self, product_id: str, include_comments: bool = False):
        """
        Lấy chi tiết sản phẩm
        
        Args:
            product_id: ID của sản phẩm
            include_comments: Có bao gồm comments với user info không
        """
        product = await self.product_repo.get_by_id(product_id)
        
        if include_comments and self.comment_repo:
            # Lấy comments với user info
            comments = await self.comment_repo.get_comments_with_users_by_product(
                product_id=product_id,
                skip=0,
                limit=50
            )
            
            # Tính rating trung bình
            rating_info = await self.comment_repo.get_average_rating(product_id)
            
            # Thêm comments và rating vào product
            if product:
                product['comments'] = comments
                product['rating_info'] = rating_info
        
        return product

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


    async def get_active_products(self) -> List[Dict]:
        products = await self.product_repo.get_active_products()
        formatted_products = []
        for product in products:
            product_dict = dict(product)
            if "_id" in product_dict:
                product_dict["id"] = str(product_dict["_id"])
                product_dict.pop("_id", None)
            formatted_products.append(product_dict)
        return formatted_products




