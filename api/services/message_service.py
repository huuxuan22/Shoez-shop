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
        receiver = await self.user_repository.get_by_id(receiver_id)
        if not receiver:
            raise ValueError("Receiver not found")

        # Tạo hoặc lấy conversation
        if conversation_id and conversation_id.strip() != '':
            try:
                conversation = await self.conversation_repository.get_by_id(conversation_id)
                if not conversation:
                    conversation = None
            except Exception:
                conversation = None
        else:
            conversation = None

        # Nếu chưa có conversation, tạo mới (quan trọng: luôn tạo nếu chưa có)
        if not conversation:
            conversation = await self.conversation_repository.create_or_get_conversation(
                user_id=receiver_id,
                admin_id=admin_id
            )
            conversation_id = str(conversation.get("_id", ""))
        
        # Đảm bảo conversation_id đã được set
        if not conversation_id or conversation_id.strip() == '':
            raise ValueError("Conversation ID is required but not found")

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

        # Tăng unread cho receiver (user)
        await self.conversation_repository.increment_unread(conversation_id, receiver_id)
        
        # Reset unread cho admin (vì admin đã reply, không còn unread nữa)
        await self.conversation_repository.reset_unread(conversation_id, admin_id)

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
        
        # Normalize receiver_id to string for consistency
        normalized_receiver_id = str(receiver_id).strip()
        normalized_admin_id = str(admin_id).strip()
        
        await sio.emit(
            'new_message',
            {
                "conversationId": conversation_id,
                "senderId": normalized_admin_id,
                "receiverId": normalized_receiver_id,
                "content": content,
                "type": "text",
                "createdAt": created_at,
                "isRead": False,
                "id": message_dict.get("id")
            },
            room=f"user_{normalized_receiver_id}",
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

    async def user_send_message(
        self,
        user_id: str,
        content: str,
        conversation_id: str = None
    ) -> Dict[str, Any]:
        """
        User gửi tin nhắn cho admin
        - Tạo hoặc lấy conversation
        - Lưu message vào database
        - Cập nhật lastMessage và unread của conversation
        - Emit realtime cho admin
        """
        # Kiểm tra user_id có tồn tại không
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        admin_id = None
        conversation = None

        # Tạo hoặc lấy conversation
        if conversation_id and conversation_id.strip() != '':
            try:
                conversation = await self.conversation_repository.get_by_id(conversation_id)
                if conversation:
                    # Tìm admin_id từ participants
                    participants = conversation.get("participants", [])
                    for p in participants:
                        if p.get("role") == "ADMIN":
                            admin_id_raw = p.get("userId")
                            # Normalize admin_id - convert ObjectId to string if needed
                            if admin_id_raw:
                                admin_id = str(admin_id_raw).strip()
                            break
            except Exception as e:
                conversation = None

        # Nếu chưa có conversation hoặc không tìm thấy admin, tìm admin đầu tiên
        if not admin_id:
            # Tìm admin đầu tiên trong hệ thống
            admin = await self.user_repository.find_one({"role": "ADMIN"})
            if not admin:
                raise ValueError("Admin not found in system")
            
            # Format admin_id - đảm bảo convert ObjectId thành string
            admin_id = None
            if "_id" in admin:
                # Convert ObjectId to string
                admin_id = str(admin["_id"])
            elif "id" in admin:
                # Use existing id field
                admin_id = str(admin["id"])
            else:
                raise ValueError("Admin ID not found")
            
            # Normalize admin_id to ensure it's a string
            if admin_id:
                admin_id = str(admin_id).strip()
            else:
                raise ValueError("Admin ID is empty after conversion")

        # Nếu chưa có conversation, tạo mới (quan trọng: luôn tạo nếu chưa có)
        if not conversation:
            conversation = await self.conversation_repository.create_or_get_conversation(
                user_id=user_id,
                admin_id=admin_id
            )
            conversation_id = str(conversation.get("id", ""))

        # Đảm bảo conversation_id đã được set
        if not conversation_id or conversation_id.strip() == '':
            raise ValueError("Conversation ID is required but not found")

        # Tạo message
        message_data = {
            "conversationId": ObjectId(conversation_id),
            "senderId": user_id,
            "receiverId": admin_id,
            "content": content,
            "type": "text",
            "isRead": False,
            "createdAt": datetime.now()
        }

        created_message = await self.message_repository.create_message(message_data)

        # Cập nhật lastMessage của conversation
        last_message = {
            "content": content,
            "senderId": user_id,
            "createdAt": datetime.now()
        }
        await self.conversation_repository.update_last_message(conversation_id, last_message)

        # Tăng unread cho admin
        await self.conversation_repository.increment_unread(conversation_id, admin_id)
        
        # Reset unread cho user (vì user đã reply, không còn unread nữa)
        await self.conversation_repository.reset_unread(conversation_id, user_id)

        # Format message để trả về
        message_dict = jsonable_encoder(created_message)
        if "_id" in message_dict:
            message_dict["id"] = str(message_dict["_id"])
            del message_dict["_id"]
        if "conversationId" in message_dict:
            message_dict["conversationId"] = str(message_dict["conversationId"])

        # Emit realtime cho admin
        sio = get_sio()
        # Format createdAt to ISO string
        created_at = message_dict.get("createdAt")
        if isinstance(created_at, datetime):
            created_at = created_at.isoformat()
        elif created_at and not isinstance(created_at, str):
            created_at = str(created_at)
        
        # Emit vào room admin và room cụ thể của admin
        await sio.emit(
            'new_message',
            {
                "conversationId": conversation_id,
                "senderId": user_id,
                "receiverId": admin_id,
                "content": content,
                "type": "text",
                "createdAt": created_at,
                "isRead": False,
                "id": message_dict.get("id")
            },
            room="admin",
            namespace="/notifications"
        )
        
        # Cũng emit vào room cụ thể của admin nếu có
        await sio.emit(
            'new_message',
            {
                "conversationId": conversation_id,
                "senderId": user_id,
                "receiverId": admin_id,
                "content": content,
                "type": "text",
                "createdAt": created_at,
                "isRead": False,
                "id": message_dict.get("id")
            },
            room=f"admin_{admin_id}",
            namespace="/notifications"
        )

        return {
            "message": message_dict,
            "conversationId": conversation_id
        }

    async def get_user_messages(
        self,
        user_id: str,
        limit: int = 1000
    ) -> Dict[str, Any]:
        """
        Lấy toàn bộ messages của user (cả gửi và nhận)
        - Tìm conversation của user
        - Lấy tất cả messages trong conversation đó
        """
        if not user_id:
            return {
                "conversationId": None,
                "messages": []
            }
        
        # Normalize user_id - ensure it's a string
        user_id_str = str(user_id).strip()
        if not user_id_str:
            return {
                "conversationId": None,
                "messages": []
            }
        
        # Tìm conversation của user
        conversation = await self.conversation_repository.get_conversation_by_user_id(user_id_str)
        
        if not conversation:
            # No conversation found for this user
            return {
                "conversationId": None,
                "messages": []
            }
        
        conversation_id = str(conversation.get("_id", ""))
        
        if not conversation_id:
            return {
                "conversationId": None,
                "messages": [],
                "unread": 0
            }
        
        # Lấy unread count cho user
        unread_data = conversation.get("unread", {})
        unread_count = unread_data.get(user_id_str, 0) if isinstance(unread_data, dict) else 0
        
        # Lấy messages từ conversation
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
        
        return {
            "conversationId": conversation_id,
            "messages": formatted_messages,
            "unread": unread_count
        }

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

