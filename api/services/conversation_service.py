from fastapi.encoders import jsonable_encoder
from repositories.conversation_repository import ConversationRepository
from repositories.user_repository import UserRepository
from repositories.message_repository import MessageRepository
from typing import List, Dict, Any
from bson import ObjectId


class ConversationService:
    def __init__(
        self,
        conversation_repository: ConversationRepository,
        user_repository: UserRepository,
        message_repository: MessageRepository
    ):
        self.conversation_repository = conversation_repository
        self.user_repository = user_repository
        self.message_repository = message_repository

    async def get_all_users_chatting_with_admin(self) -> List[Dict[str, Any]]:
        """
        Lấy tất cả danh sách users đã nhắn tin đến admin
        """
        # Lấy tất cả conversations có ADMIN
        conversations = await self.conversation_repository.get_conversations_with_admin()
        
        result = []
        for conv in conversations:
            # Tìm participant có role là USER
            user_participant = None
            admin_participant = None
            
            for participant in conv.get("participants", []):
                if participant.get("role") == "USER":
                    user_participant = participant
                elif participant.get("role") == "ADMIN":
                    admin_participant = participant
            
            if not user_participant:
                continue
            
            user_id = user_participant.get("userId")
            if not user_id:
                continue
            
            # Lấy thông tin user
            user = await self.user_repository.get_by_id_str(user_id)
            if not user:
                continue
            
            # Lấy số tin nhắn chưa đọc cho admin
            admin_id = admin_participant.get("userId") if admin_participant else None
            unread_count = 0
            if admin_id and conv.get("unread"):
                unread_count = conv.get("unread", {}).get(admin_id, 0)
            
            # Lấy last message
            last_message = conv.get("lastMessage", {})
            
            result.append({
                "id": str(conv.get("_id", "")),
                "userId": user_id,
                "name": user.get("full_name", "Unknown"),
                "avatar": user.get("avatar", ""),
                "unread": unread_count,
                "lastMessage": last_message.get("content", "") if last_message else "",
                "lastMessageTime": last_message.get("createdAt") if last_message else None,
                "conversationId": str(conv.get("_id", ""))
            })
        
        # Sắp xếp theo thời gian lastMessage mới nhất
        result.sort(
            key=lambda x: x.get("lastMessageTime") or "",
            reverse=True
        )
        
        return jsonable_encoder(result)

