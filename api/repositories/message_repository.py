from config.database import get_database
from model.message_model import Message
from repositories.base_repository import BaseRepository
from typing import List, Dict, Any, Optional
from bson import ObjectId


class MessageRepository(BaseRepository[Message]):
    def __init__(self, db):
        super().__init__(db, 'messages')

    async def get_messages_by_conversation(self, conversation_id: str, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Lấy danh sách messages theo conversation_id
        """
        try:
            oid = ObjectId(conversation_id)
            query = {"conversationId": oid}
            messages = await self.find_all(query, sort=[("createdAt", -1)], limit=limit)
            # Reverse để có thứ tự từ cũ đến mới
            return list(reversed(messages)) if messages else []
        except Exception:
            return []

    async def create_message(self, message_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Tạo message mới
        """
        from datetime import datetime
        message_data["createdAt"] = datetime.now()
        return await self.create(message_data)

    async def mark_as_read(self, conversation_id: str, receiver_id: str):
        """
        Đánh dấu tất cả messages trong conversation là đã đọc cho receiver_id
        """
        try:
            oid = ObjectId(conversation_id)
            await self.collection.update_many(
                {
                    "conversationId": oid,
                    "receiverId": receiver_id,
                    "isRead": False
                },
                {"$set": {"isRead": True}}
            )
        except Exception:
            pass

    async def count_unread(self, conversation_id: str, receiver_id: str) -> int:
        """
        Đếm số messages chưa đọc trong conversation cho receiver_id
        """
        try:
            oid = ObjectId(conversation_id)
            count = await self.collection.count_documents({
                "conversationId": oid,
                "receiverId": receiver_id,
                "isRead": False
            })
            return count
        except Exception:
            return 0

