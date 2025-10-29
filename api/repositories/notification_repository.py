"""
Notification Repository
Giải thích: CRUD operations cho notifications trong MongoDB
"""
from repositories.base_repository import BaseRepository
from model.notification_model import Notification
from bson import ObjectId
from typing import List, Dict, Any, Optional


class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, db):
        super().__init__(db, "notifications")  

    async def get_by_user(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        cursor = self.collection.find({"user_id": user_id}).sort("created_at", -1).limit(limit)
        notifications = await cursor.to_list(length=limit)
        return [self._convert_id(notification) for notification in notifications]

    async def get_unread_by_user(self, user_id: str) -> List[Dict[str, Any]]:
        cursor = self.collection.find({"user_id": user_id, "is_read": False}).sort("created_at", -1)
        notifications = await cursor.to_list(length=50)
        return [self._convert_id(notification) for notification in notifications]

    async def count_unread(self, user_id: str) -> int:
        return await self.collection.count_documents({"user_id": user_id, "is_read": False})

    async def mark_as_read(self, notification_id: str) -> Dict[str, Any]:
        notification = await self.collection.find_one_and_update(
            {"_id": ObjectId(notification_id)},
            {"$set": {"is_read": True, "updated_at": self._get_current_timestamp()}},
            return_document=True
        )
        return self._convert_id(notification) if notification else None

    async def mark_all_as_read(self, user_id: str) -> int:
        """
        Đánh dấu tất cả notifications của user là đã đọc
        - Returns: Số lượng đã update
        """
        result = await self.collection.update_many(
            {"user_id": user_id, "is_read": False},
            {"$set": {"is_read": True, "updated_at": self._get_current_timestamp()}}
        )
        return result.modified_count

    async def create_notification(
        self,
        user_id: str,
        order_id: Optional[str],
        title: str,
        message: str,
        type: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Tạo notification mới và lưu vào DB
        """
        notification_data = {
            "user_id": user_id,
            "order_id": order_id,
            "title": title,
            "message": message,
            "type": type,
            "is_read": False,
            "metadata": metadata or {},
            "created_at": self._get_current_timestamp(),
            "updated_at": self._get_current_timestamp()
        }

        result = await self.collection.insert_one(notification_data)
        notification_data["_id"] = result.inserted_id
        return self._convert_id(notification_data)

    async def delete_notification(self, notification_id: str) -> bool:
        """
        Xóa notification
        """
        result = await self.collection.delete_one({"_id": ObjectId(notification_id)})
        return result.deleted_count > 0

