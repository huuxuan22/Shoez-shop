from fastapi.encoders import jsonable_encoder
from fastapi import UploadFile
from minio import S3Error
from config.config import get_settings
from utils.utils import hash_password, replace_avatar, verify_password
from repositories.user_repository import UserRepository
from datetime import datetime, timedelta
from typing import Dict, Any, Optional,List
from schemas.auth_schemas import UserCreate
from schemas.user_schemas import UserUpdate
from model.user_model import User
import asyncio
import uuid
import os
from bson import ObjectId
from fastapi import HTTPException
from passlib.context import CryptContext
from config.minio_client import minio_client  # import instance MinioClient của bạn

settings = get_settings()

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def list_users(self, page: int = 1, page_size: int = 10):
        users = await self.user_repository.get_all(page=page, page_size=page_size)
        return jsonable_encoder(users)

    async def create_user(self, user: UserCreate):
        user_dict = user.dict()
        user_dict['created_at'] = user_dict['updated_at'] = datetime.now()
        user_dict["role"] = "USER"
        return await self.user_repository.create(user_dict)

    async def update_user(self, user_update: UserUpdate) -> Optional[User]:
        user_dict: Dict[str, Any] = user_update.dict(exclude_unset=True, exclude={"id"})
        updated_user = await self.user_repository.update_by_id(
            user_id=user_update.id,
            data=user_dict
        )
        return updated_user

    async def reset_password(self, user_id: str, current_pw: str, new_pw: str):
        try:
            user_oid = ObjectId(user_id)
        except Exception:
            raise HTTPException(status_code=400, detail="ID không hợp lệ")
        user = await self.user_repository.find_one({"_id": user_oid})
        if not user:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")

        if not verify_password(current_pw, user["password"]):
            raise HTTPException(status_code=400, detail="Mật khẩu hiện tại không đúng")

        hashed_password = hash_password(new_pw)

        await self.user_repository.update_by_id(user_id=user_id, data={"password": hashed_password})
        return {"message": "Cập nhật mật khẩu thành công!"}

    async def delete_user(self, ids: List[str]) -> int:
        # Soft delete users by _id
        return await self.user_repository.soft_delete_by_ids(ids, id_key="_id")

    async def lock_users(self, ids: List[str], is_active: bool) -> int:
        # bulk update is_active
        from bson import ObjectId
        object_ids = [ObjectId(i) for i in ids if ObjectId.is_valid(i)]
        return await self.user_repository.update_all(
            {"_id": {"$in": object_ids}},
            {"is_active": is_active}
        )

    async def restore_users(self, ids: List[str]) -> int:
        from bson import ObjectId
        object_ids = [ObjectId(i) for i in ids if ObjectId.is_valid(i)]
        return await self.user_repository.update_all(
            {"_id": {"$in": object_ids}},
            {"is_deleted": False}
        )

    async def upload_avatar(self, file: UploadFile, user_id: int) -> str:
        user = await self.user_repository.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
        old_avatar_url = user.get("avatar")  # avatar cũ nếu có
        bucket_name = "avatars"
        new_avatar_url = await replace_avatar(minio_client, bucket_name, old_avatar_url, file)
        await self.user_repository.update_by_id(user_id=user_id, data={"avatar": new_avatar_url})
        return new_avatar_url

