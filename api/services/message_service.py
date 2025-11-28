from fastapi.encoders import jsonable_encoder
from repositories.conversation_repository import ConversationRepository
from repositories.message_repository import MessageRepository
from repositories.user_repository import UserRepository
from typing import Dict, Any, List
from bson import ObjectId
from datetime import datetime
from config.socket import get_sio


class MessageService:
    def __init__(
        self,
        message_repository: MessageRepository,
        conversation_repository: ConversationRepository,
        user_repository: UserRepository
    ):
        self.message_repository = message_repository
        self.conversation_repository = conversation_repository
        self.user_repository = user_repository

    async def admin_send_message(
        self,
        admin_id: str,
        receiver_id: str,
        content: str,
        conversation_id: str = None
    ) -> Dict[str, Any]:
        """
        Admin gửi tin nhắn cho user
        - Tạo hoặc lấy conversation
        - Lưu message vào database
        - Cập nhật lastMessage và unread của conversation
        - Emit realtime cho user
        """
        # Kiểm tra receiver_id có tồn tại không
        receiver = await self.user_repository.get_by_id_str(receiver_id)
        if not receiver:
            raise ValueError("Receiver not found")

        # Tạo hoặc lấy conversation
        if conversation_id and conversation_id.strip() != '':
            try:
                conversation = await self.conversation_repository.get_by_id(conversation_id)
                if not conversation:
                    raise ValueError("Conversation not found")
            except Exception:
                conversation = None
        else:
            conversation = None

        # Nếu chưa có conversation, tạo mới
        if not conversation and conversation is not None:
            conversation = await self.conversation_repository.create_or_get_conversation(
                user_id=receiver_id,
                admin_id=admin_id
            )
            conversation_id = str(conversation.get("_id", ""))

        # Tạo message
        message_data = {
            "conversationId": ObjectId(conversation_id),
            "senderId": admin_id,
            "receiverId": receiver_id,
            "content": content,
            "type": "text",
            "isRead": False,
            "createdAt": datetime.now()
        }

        created_message = await self.message_repository.create_message(message_data)

        # Cập nhật lastMessage của conversation
        last_message = {
            "content": content,
            "senderId": admin_id,
            "createdAt": datetime.now()
        }
        await self.conversation_repository.update_last_message(conversation_id, last_message)

        # Tăng unread cho receiver
        await self.conversation_repository.increment_unread(conversation_id, receiver_id)

        # Format message để trả về
        message_dict = jsonable_encoder(created_message)
        if "_id" in message_dict:
            message_dict["id"] = str(message_dict["_id"])
            del message_dict["_id"]
        if "conversationId" in message_dict:
            message_dict["conversationId"] = str(message_dict["conversationId"])

        # Emit realtime cho user
        sio = get_sio()
        # Format createdAt to ISO string
        created_at = message_dict.get("createdAt")
        if isinstance(created_at, datetime):
            created_at = created_at.isoformat()
        elif created_at and not isinstance(created_at, str):
            created_at = str(created_at)
        
        await sio.emit(
            'new_message',
            {
                "conversationId": conversation_id,
                "senderId": admin_id,
                "receiverId": receiver_id,
                "content": content,
                "type": "text",
                "createdAt": created_at,
                "isRead": False,
                "id": message_dict.get("id")
            },
            room=f"user_{receiver_id}",
            namespace="/notifications"
        )

        return {
            "message": message_dict,
            "conversationId": conversation_id
        }

    async def get_messages_by_conversation(
        self,
        conversation_id: str,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Lấy danh sách messages theo conversation_id
        """
        messages = await self.message_repository.get_messages_by_conversation(
            conversation_id,
            limit
        )

        # Format messages
        formatted_messages = []
        for msg in messages:
            msg_dict = jsonable_encoder(msg)
            if "_id" in msg_dict:
                msg_dict["id"] = str(msg_dict["_id"])
                del msg_dict["_id"]
            if "conversationId" in msg_dict:
                msg_dict["conversationId"] = str(msg_dict["conversationId"])
            formatted_messages.append(msg_dict)

        return formatted_messages

    async def mark_messages_as_read(
        self,
        conversation_id: str,
        user_id: str
    ):
        """
        Đánh dấu tất cả messages trong conversation là đã đọc
        """
        await self.message_repository.mark_as_read(conversation_id, user_id)
        await self.conversation_repository.reset_unread(conversation_id, user_id)

