from typing import Optional, Dict, Any, List
from bson import ObjectId
from fastapi import HTTPException

from model.comment_product_model import CommentProduct
from repositories.base_repository import BaseRepository


class CommentRepository(BaseRepository[CommentProduct]):
    def __init__(self, db):
        super().__init__(db, 'comments')

    async def get_comments_by_product(self, product_id: str, skip: int = 0, limit: int = 10):
        """
        Lấy tất cả comment của một sản phẩm
        """
        try:
            cursor = self.collection.find({"product_id": product_id}) \
                .sort("created_at", -1) \
                .skip(skip) \
                .limit(limit)
            
            documents = await cursor.to_list(length=limit)
            return [self._convert_id(doc) for doc in documents]
        except Exception as e:
            raise Exception(f"Failed to get comments by product: {str(e)}")

    async def get_comments_by_user(self, user_id: str, skip: int = 0, limit: int = 10):
        """
        Lấy tất cả comment của một user
        """
        try:
            cursor = self.collection.find({"user_id": user_id}) \
                .sort("created_at", -1) \
                .skip(skip) \
                .limit(limit)
            
            documents = await cursor.to_list(length=limit)
            return [self._convert_id(doc) for doc in documents]
        except Exception as e:
            raise Exception(f"Failed to get comments by user: {str(e)}")

    async def get_average_rating(self, product_id: str) -> float:
        """
        Tính điểm đánh giá trung bình của sản phẩm
        """
        try:
            pipeline = [
                {"$match": {"product_id": product_id}},
                {
                    "$group": {
                        "_id": None,
                        "average": {"$avg": "$rating"},
                        "count": {"$sum": 1}
                    }
                }
            ]
            
            cursor = self.collection.aggregate(pipeline)
            result = await cursor.to_list(length=1)
            
            if result and result[0]:
                return {
                    "average": round(result[0]["average"], 1),
                    "count": result[0]["count"]
                }
            return {"average": 0.0, "count": 0}
        except Exception as e:
            raise Exception(f"Failed to get average rating: {str(e)}")

    async def count_comments_by_product(self, product_id: str) -> int:
        """
        Đếm số lượng comment của một sản phẩm
        """
        return await self.count({"product_id": product_id})

    async def get_comments_with_users_by_product(self, product_id: str, skip: int = 0, limit: int = 10):
        """
        Lấy comments của sản phẩm kèm thông tin user (JOIN với users collection)
        """
        try:
            # Pipeline aggregation để join với users
            pipeline = [
                {"$match": {"product_id": product_id}},
                {
                    "$lookup": {
                        "from": "users",
                        "localField": "user_id",
                        "foreignField": "_id",
                        "as": "user_info"
                    }
                },
                {"$unwind": {"path": "$user_info", "preserveNullAndEmptyArrays": True}},
                {"$sort": {"created_at": -1}},
                {"$skip": skip},
                {"$limit": limit},
                {
                    "$project": {
                        "id": {"$toString": "$_id"},
                        "product_id": 1,
                        "user_id": 1,
                        "user_name": "$user_info.full_name",
                        "user_avatar": "$user_info.avatar",
                        "rating": 1,
                        "comment": 1,
                        "images": 1,
                        "verified": 1,
                        "created_at": 1,
                        "updated_at": 1
                    }
                }
            ]
            
            cursor = self.collection.aggregate(pipeline)
            documents = await cursor.to_list(length=limit)
            
            # Convert _id to id
            for doc in documents:
                if '_id' in doc:
                    doc['id'] = str(doc['_id'])
                    del doc['_id']
            
            return documents
        except Exception as e:
            raise Exception(f"Failed to get comments with users by product: {str(e)}")

