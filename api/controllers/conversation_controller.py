from typing import List
from fastapi import APIRouter, Depends, Query
from starlette.responses import JSONResponse

from dependences.permissions import require_roles
from repositories.conversation_repository import ConversationRepository
from repositories.user_repository import UserRepository
from repositories.message_repository import MessageRepository
from services.conversation_service import ConversationService
from dependences.dependencies import (
    get_conversation_repo,
    get_user_repo,
    get_message_repo
)

conversation_router = APIRouter(prefix="/conversations", tags=["Conversations"])


@conversation_router.get("/users", summary="Lấy danh sách users đã nhắn tin đến admin")
@require_roles("ADMIN")
async def get_users_chatting_with_admin(
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo),
    message_repo: MessageRepository = Depends(get_message_repo)
):
    """
    API lấy tất cả danh sách users đã nhắn tin đến admin
    Trả về: danh sách users với thông tin avatar, tên, số tin nhắn chưa đọc, last message
    """
    service = ConversationService(conversation_repo, user_repo, message_repo)
    users = await service.get_all_users_chatting_with_admin()
    return JSONResponse(
        status_code=200,
        content={"users": users}
    )


@conversation_router.get("/search-users", summary="Tìm kiếm users theo email hoặc số điện thoại")
@require_roles("ADMIN")
async def search_users(
    q: str = Query(..., description="Từ khóa tìm kiếm (email hoặc số điện thoại)"),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API tìm kiếm users theo email hoặc số điện thoại
    Trả về: danh sách users khớp với từ khóa tìm kiếm
    """
    if not q or len(q.strip()) < 2:
        return JSONResponse(
            status_code=200,
            content={"users": []}
        )
    
    users = await user_repo.search_users_by_email_or_phone(q.strip(), limit=20)
    
    # Format response để phù hợp với frontend
    formatted_users = []
    for user in users:
        formatted_users.append({
            "id": user.get("id", ""),
            "userId": user.get("id", ""),
            "name": user.get("full_name", "Unknown"),
            "email": user.get("email", ""),
            "phone": user.get("numberphone", ""),
            "avatar": user.get("avatar", ""),
            "unread": 0,
            "lastMessage": "",
            "lastMessageTime": None,
            "conversationId": None,
            "isNewConversation": True  # Flag để biết đây là user mới, chưa có conversation
        })
    
    return JSONResponse(
        status_code=200,
        content={"users": formatted_users}
    )

