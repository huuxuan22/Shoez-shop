from typing import Optional, Dict, Any
from bson import ObjectId
from fastapi import HTTPException

from model import Brand
from repositories.base_repository import BaseRepository


class BrandRepository(BaseRepository[Brand]):
    def __init__(self, db):
        super().__init__(db, 'brands')

    async def get_by_name(self, brand_name: str):
        """Lấy thương hiệu theo tên"""
        doc = await self.find_one({
            "name": brand_name,
            "$or": [
                {"is_deleted": False},
                {"is_deleted": {"$exists": False}}
            ]
        })
        if doc:
            converted = self._convert_id(doc)
            # Set default values nếu thiếu
            if 'is_active' not in converted:
                converted['is_active'] = True
            if 'is_deleted' not in converted:
                converted['is_deleted'] = False
            return converted
        return None

    async def get_by_id(self, brand_id: str):
        """Lấy thương hiệu theo ID"""
        try:
            obj_id = ObjectId(brand_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid brand ID")

        doc = await self.find_one({
            "_id": obj_id,
            "$or": [
                {"is_deleted": False},
                {"is_deleted": {"$exists": False}}
            ]
        })
        if not doc:
            raise HTTPException(status_code=404, detail="Brand not found")

        converted = self._convert_id(doc)
        # Set default values nếu thiếu
        if 'is_active' not in converted:
            converted['is_active'] = True
        if 'is_deleted' not in converted:
            converted['is_deleted'] = False
        return converted

    async def get_all_brands(
        self,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        is_active: Optional[bool] = None
    ):
        """Lấy danh sách tất cả thương hiệu"""
        # Lấy cả các document không có field is_deleted hoặc có is_deleted = False
        filter_query = {
            "$or": [
                {"is_deleted": False},
                {"is_deleted": {"$exists": False}}  # Không có field is_deleted
            ]
        }
        
        # Thêm các điều kiện filter khác
        and_conditions = []
        if search:
            and_conditions.append({"name": {"$regex": search, "$options": "i"}})
        
        if is_active is not None:
            and_conditions.append({"is_active": is_active})
        
        # Nếu có điều kiện bổ sung, dùng $and để kết hợp
        if and_conditions:
            filter_query = {
                "$and": [
                    {
                        "$or": [
                            {"is_deleted": False},
                            {"is_deleted": {"$exists": False}}
                        ]
                    }
                ] + and_conditions
            }

        cursor = self.collection.find(filter_query).skip(skip).limit(limit).sort("name", 1)
        documents = await cursor.to_list(length=limit)
        # Đảm bảo mỗi document có đủ các field cần thiết
        result = []
        for doc in documents:
            converted = self._convert_id(doc)
            # Set default values nếu thiếu
            if 'is_active' not in converted:
                converted['is_active'] = True
            if 'is_deleted' not in converted:
                converted['is_deleted'] = False
            result.append(converted)
        return result

    async def count_brands(self, filter_query: Optional[Dict[str, Any]] = None) -> int:
        """Đếm số lượng brand"""
        if filter_query is None:
            query = {
                "$or": [
                    {"is_deleted": False},
                    {"is_deleted": {"$exists": False}}
                ]
            }
        else:
            query = filter_query
        return await self.count(query)

    async def delete_brand(self, brand_id: str) -> bool:
        """Xóa thương hiệu (soft delete)"""
        try:
            obj_id = ObjectId(brand_id)
        except Exception:
            return False
        
        result = await self.update_one(
            {"_id": obj_id},
            {"$set": {"is_deleted": True}}
        )
        return result.modified_count > 0

    async def check_name_exists(self, name: str, exclude_id: Optional[str] = None) -> bool:
        """Kiểm tra tên thương hiệu đã tồn tại chưa"""
        query = {
            "name": name,
            "$or": [
                {"is_deleted": False},
                {"is_deleted": {"$exists": False}}
            ]
        }
        
        if exclude_id:
            try:
                obj_id = ObjectId(exclude_id)
                query["_id"] = {"$ne": obj_id}
            except Exception:
                pass
        
        doc = await self.find_one(query)
        return doc is not None

