from config.database import get_database
from model.user_model import User
from repositories.base_repository import BaseRepository
from typing import List, Dict, Any, Optional
from pymongo import ReturnDocument
from pymongo.errors import PyMongoError
from bson import ObjectId

class UserRepository(BaseRepository[User]):
    def __init__(self, db):
        super().__init__(db, 'users')

    async def get_by_email(self, email: str) -> User | None:
        return await self.find_one({"email": email})

    async def get_all(self, page: int = 1, page_size: int = 10) -> List[dict]:
        users = []
        skip = (page - 1) * page_size
        cursor = self.db["users"].find({}).skip(skip).limit(page_size)
        async for user in cursor:
            # Ensure id field exists - use _id as id
            if 'id' not in user and '_id' in user:
                user['id'] = str(user['_id'])
            # Remove _id from response
            if '_id' in user:
                del user['_id']
            users.append(user)
        return users
    

    # async def get_user_principal(self, email: str):
    #     user = await self.db["users"].find_one({"email": email})
    #     if user:
    #         # Ensure id field exists - use _id as id
    #         if 'id' not in user and '_id' in user:
    #             user['id'] = str(user['_id'])
    #             # Update the document to add id field
    #             await self.db["users"].update_one(
    #                 {"_id": user['_id']},
    #                 {"$set": {"id": user['id']}}
    #             )
    #         # Remove _id from response
    #         if '_id' in user:
    #             del user['_id']
    #     return user

    async def get_user_principal(self, email: str):
        user = await self.db["users"].find_one({"email": email})

        if user:
            # Đổi _id thành id (nếu có)
            if "_id" in user:
                user["id"] = str(user["_id"])
                del user["_id"]

        return user  


    async def update_by_id(self, user_id: str, data: Dict[str, Any]) -> Optional[Dict]:
        """
        Update user by id (id field = _id as string)
        """
        try:
            # Add updated_at timestamp
            from datetime import datetime
            data['updated_at'] = datetime.now()
            
            # Update by id field
            updated_doc = await self.collection.find_one_and_update(
                {"_id": ObjectId(user_id)},  # dùng ObjectId thay vì string
                {"$set": data},
                return_document=ReturnDocument.AFTER
            )
            
            if updated_doc:
                # Convert _id to id for consistency
                if '_id' in updated_doc:
                    updated_doc['id'] = str(updated_doc['_id'])
                    del updated_doc['_id']
                return updated_doc
            return None
        except PyMongoError as e:
            raise Exception(f"Failed to update user by ID: {str(e)}")



