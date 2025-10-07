from repositories.user_repository import UserRepository
from datetime import datetime
from typing import Dict, Any, Optional,List
from schemas.auth_schemas import UserCreate
from schemas.user_schemas import UserUpdate
from model.user_model import User
import asyncio
import uuid

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def list_users(self, page: int = 1, page_size: int = 10):
        return await self.user_repository.get_all(page=page, page_size=page_size)

    async def create_user(self, user: UserCreate):
        user_dict = user.dict()
        user_dict['created_at'] = user_dict['updated_at'] = datetime.now()

        return await self.user_repository.create(user_dict)

    async def update_user(self, user_update: UserUpdate) -> Optional[User]:
        # Chuyển object UserUpdate thành dict và loại bỏ id ra khỏi dữ liệu update
        user_dict: Dict[str, Any] = user_update.dict(exclude_unset=True, exclude={"id"})
        user_dict['updated_at'] = datetime.now()

        # Gọi repository update theo field id (UUID)
        updated_user = await self.user_repository.update(
            entity_id=user_update.id,
            data=user_dict,
            id_key="id"  # dùng id thay vì _id
        )

        return updated_user

    async def delete_user(self, ids: List[str]) -> None:
        # Xóa theo trường 'id' trong document
        await asyncio.gather(
            *(self.user_repository.delete(entity_id=id, id_key="id") for id in ids)
        )
