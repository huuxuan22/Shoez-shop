from config.database import get_database
from model.user_model import User
from repositories.base_repository import BaseRepository
from typing import List

class UserRepository(BaseRepository[User]):
    def __init__(self, db):
        super().__init__(db, 'users')

    async def get_by_email(self, email: str) -> User | None:
        return await self.find_one({"email": email})

    async def get_all(self, page: int = 1, page_size: int = 10) -> List[dict]:
        users = []
        skip = (page - 1) * page_size
        cursor = self.db["users"].find({}, {"_id": 0}).skip(skip).limit(page_size)
        async for user in cursor:
            users.append(user)
        return users

    async def get_user_principal(self, email: str):
        return await self.db["users"].find_one({"email": email}, {"_id": 0})



