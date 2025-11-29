from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from starlette.responses import JSONResponse
from pydantic import BaseModel, Field

from dependences.permissions import require_roles
from repositories.message_repository import MessageRepository
from repositories.conversation_repository import ConversationRepository
from repositories.user_repository import UserRepository
from services.message_service import MessageService
from dependences.dependencies import (
    get_message_repo,
    get_conversation_repo,
    get_user_repo
)
from config.context import get_current_user

message_router = APIRouter(prefix="/messages", tags=["Messages"])


class AdminSendMessageRequest(BaseModel):
    receiverId: str = Field(..., description="ID của user nhận tin nhắn")
    content: str = Field(..., min_length=1, description="Nội dung tin nhắn")
    conversationId: Optional[str] = Field(None, description="ID của conversation (nếu có)")


class UserSendMessageRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Nội dung tin nhắn")
    conversationId: Optional[str] = Field(None, description="ID của conversation (nếu có)")


@message_router.post("/admin-send", summary="Admin gửi tin nhắn cho user")
@require_roles("ADMIN")
async def admin_send_message(
    request: AdminSendMessageRequest,
    current_user: dict = Depends(get_current_user),
    message_repo: MessageRepository = Depends(get_message_repo),
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API để admin gửi tin nhắn cho user
    - Tự động tạo conversation nếu chưa có
    - Lưu message vào database
    - Emit realtime cho user
    """
    # Lấy admin_id từ current_user
    admin_id = str(current_user.get("_id") or current_user.get("id"))
    if not admin_id:
        raise HTTPException(status_code=401, detail="Admin not authenticated")

    service = MessageService(message_repo, conversation_repo, user_repo)
    
    try:
        result = await service.admin_send_message(
            admin_id=admin_id,
            receiver_id=request.receiverId,
            content=request.content,
            conversation_id=request.conversationId
        )
        return JSONResponse(
            status_code=200,
            content=result
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")


@message_router.get("/{conversation_id}", summary="Lấy danh sách messages theo conversation")
async def get_messages(
    conversation_id: str,
    limit: int = Query(100, ge=1, le=500, description="Số lượng messages tối đa"),
    current_user: dict = Depends(get_current_user),
    message_repo: MessageRepository = Depends(get_message_repo),
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API lấy danh sách messages trong một conversation
    - User hoặc Admin đều có thể xem messages của conversation họ tham gia
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    user_role = current_user.get("role", "USER")

    # Kiểm tra user có quyền xem conversation này không
    try:
        conversation = await conversation_repo.get_by_id(conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")

        # Kiểm tra user có trong participants không
        participants = conversation.get("participants", [])
        is_participant = any(
            p.get("userId") == user_id for p in participants
        )

        # Admin có thể xem tất cả conversations
        if not is_participant and user_role != "ADMIN":
            raise HTTPException(status_code=403, detail="Access denied")

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=404, detail="Conversation not found")

    service = MessageService(message_repo, conversation_repo, user_repo)
    messages = await service.get_messages_by_conversation(conversation_id, limit)

    return JSONResponse(
        status_code=200,
        content={"messages": messages}
    )


@message_router.post("/user-send", summary="User gửi tin nhắn cho admin")
async def user_send_message(
    request: UserSendMessageRequest,
    current_user: dict = Depends(get_current_user),
    message_repo: MessageRepository = Depends(get_message_repo),
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API để user gửi tin nhắn cho admin
    - Tự động tạo conversation nếu chưa có
    - Lưu message vào database
    - Emit realtime cho admin
    """
    # Lấy user_id từ current_user
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")

    # Kiểm tra không phải admin
    user_role = current_user.get("role", "USER")
    if user_role == "ADMIN":
        raise HTTPException(status_code=403, detail="Admins should use /messages/admin-send endpoint")

    service = MessageService(message_repo, conversation_repo, user_repo)
    
    try:
        result = await service.user_send_message(
            user_id=user_id,
            content=request.content,
            conversation_id=request.conversationId
        )
        return JSONResponse(
            status_code=200,
            content=result
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")


@message_router.get("/user/my-messages", summary="Lấy toàn bộ messages của user hiện tại")
async def get_user_messages(
    limit: int = Query(1000, ge=1, le=5000, description="Số lượng messages tối đa"),
    current_user: dict = Depends(get_current_user),
    message_repo: MessageRepository = Depends(get_message_repo),
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API lấy toàn bộ messages của user hiện tại
    - Tự động tìm conversation của user
    - Trả về conversationId và danh sách messages
    """
    # Get user_id - handle both _id (ObjectId) and id (string) formats
    user_id = None
    if current_user.get("_id"):
        user_id = str(current_user.get("_id"))
    elif current_user.get("id"):
        user_id = str(current_user.get("id"))
    
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")

    service = MessageService(message_repo, conversation_repo, user_repo)
    result = await service.get_user_messages(user_id, limit)

    return JSONResponse(
        status_code=200,
        content=result
    )


@message_router.post("/{conversation_id}/mark-read", summary="Đánh dấu messages là đã đọc")
async def mark_messages_as_read(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
    message_repo: MessageRepository = Depends(get_message_repo),
    conversation_repo: ConversationRepository = Depends(get_conversation_repo),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API đánh dấu tất cả messages trong conversation là đã đọc
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")

    service = MessageService(message_repo, conversation_repo, user_repo)
    await service.mark_messages_as_read(conversation_id, user_id)

    return JSONResponse(
        status_code=200,
        content={"message": "Messages marked as read"}
    )

