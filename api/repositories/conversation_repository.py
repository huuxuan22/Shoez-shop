from config.database import get_database
from model.conversation_model import Conversation
from repositories.base_repository import BaseRepository
from typing import List, Dict, Any, Optional
from bson import ObjectId
from datetime import datetime 


class ConversationRepository(BaseRepository[Conversation]):
    def __init__(self, db):
        super().__init__(db, 'conversations')

    async def get_conversations_with_admin(self) -> List[Dict[str, Any]]:
        """
        Lấy tất cả conversations có participant là ADMIN
        """
        query = {
            "participants.role": "ADMIN"
        }
        conversations = await self.get_all(query=query)
        return conversations

    async def get_conversation_by_participants(self, user_id: str, admin_id: str) -> Optional[Dict[str, Any]]:
        """
        Tìm conversation theo user_id và admin_id
        """
        query = {
            "participants": {
                "$all": [
                    {"$elemMatch": {"userId": user_id, "role": "USER"}},
                    {"$elemMatch": {"userId": admin_id, "role": "ADMIN"}}
                ]
            }
        }
        return await self.find_one(query)

    async def create_or_get_conversation(self, user_id: str, admin_id: str) -> Dict[str, Any]:
        """
        Tạo mới hoặc lấy conversation giữa user và admin
        """
        existing = await self.get_conversation_by_participants(user_id, admin_id)
        if existing:
            return existing
        
        conversation_data = {
            "participants": [
                {"userId": user_id, "role": "USER"},
                {"userId": admin_id, "role": "ADMIN"}
            ],
            "unread": {
                admin_id: 0,
                user_id: 0
            },
            "updatedAt": None
        }
        return await self.create(conversation_data)

    async def update_last_message(self, conversation_id: str, last_message: Dict[str, Any]):
        """
        Cập nhật lastMessage và updatedAt của conversation
        """
        update_data = {
            "lastMessage": last_message,
            "updatedAt": datetime.now()
        }
        try:
            oid = ObjectId(conversation_id)
            await self.update_by_id(conversation_id, update_data)
        except Exception:
            pass

    async def increment_unread(self, conversation_id: str, user_id: str):
        """
        Tăng số lượng unread cho user_id trong conversation
        """
        try:
            oid = ObjectId(conversation_id)
            await self.collection.update_one(
                {"_id": oid},
                {"$inc": {f"unread.{user_id}": 1}}
            )
        except Exception:
            pass

    async def reset_unread(self, conversation_id: str, user_id: str):
        """
        Reset số lượng unread về 0 cho user_id trong conversation
        """
        try:
            oid = ObjectId(conversation_id)
            await self.collection.update_one(
                {"_id": oid},
                {"$set": {f"unread.{user_id}": 0}}
            )
        except Exception:
            pass

