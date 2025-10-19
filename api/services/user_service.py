from fastapi.encoders import jsonable_encoder
from fastapi import UploadFile

from utils.utils import hash_password, verify_password
from repositories.user_repository import UserRepository
from datetime import datetime
from typing import Dict, Any, Optional,List
from schemas.auth_schemas import UserCreate
from schemas.user_schemas import UserUpdate
from model.user_model import User
import asyncio
import uuid
import os
import shutil
from bson import ObjectId
from fastapi import HTTPException
from passlib.context import CryptContext

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
        # Chuyển object UserUpdate thành dict và loại bỏ id ra khỏi dữ liệu update
        user_dict: Dict[str, Any] = user_update.dict(exclude_unset=True, exclude={"id"})
        # Không cần thêm updated_at vì update_by_id sẽ tự động thêm
        
        # Gọi repository update theo _id (ObjectId)
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

        # Lấy user từ DB
        user = await self.user_repository.find_one({"_id": user_oid})
        if not user:
            raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")

        # Kiểm tra mật khẩu cũ
        if not verify_password(current_pw, user["password"]):
            raise HTTPException(status_code=400, detail="Mật khẩu hiện tại không đúng")

        # Hash mật khẩu mới
        hashed_password = hash_password(new_pw)

        # Cập nhật vào DB
        await self.user_repository.update_by_id(user_id=user_id, data={"password": hashed_password})

        return {"message": "Cập nhật mật khẩu thành công!"}

    async def delete_user(self, ids: List[str]) -> None:
        # Xóa theo trường 'id' trong document
        await asyncio.gather(
            *(self.user_repository.delete(entity_id=id, id_key="id") for id in ids)
        )

    async def upload_avatar(self, file: UploadFile) -> str:
        """
        Upload avatar file and return the URL
        """
        # Create uploads directory if not exists
        upload_dir = "uploads/avatars"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Generate unique filename
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(upload_dir, unique_filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Return the URL (you can customize this based on your static file serving setup)
        avatar_url = f"/uploads/avatars/{unique_filename}"
        return avatar_url
