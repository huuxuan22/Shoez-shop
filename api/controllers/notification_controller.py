"""
Notification Controller
Giải thích: API endpoints để quản lý notifications (lấy từ database)
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import List, Dict, Any
from config.context import get_current_user
from dependences.dependencies import get_notification_repo

notification_router = APIRouter(prefix="/notifications", tags=["Notifications"])


@notification_router.get("")
async def get_user_notifications(
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Lấy tất cả notifications của user hiện tại
    - Sorted by created_at DESC
    - Limit: 50 notifications
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    notifications = await repo.get_by_user(user_id)
    return JSONResponse(content=jsonable_encoder(notifications), status_code=200)


@notification_router.get("/unread")
async def get_unread_notifications(
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Lấy unread notifications của user
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    notifications = await repo.get_unread_by_user(user_id)
    return JSONResponse(content=jsonable_encoder(notifications), status_code=200)


@notification_router.get("/count")
async def get_unread_count(
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Lấy số lượng unread notifications
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    count = await repo.count_unread(user_id)
    return JSONResponse(content={"unread_count": count}, status_code=200)


@notification_router.patch("/{notification_id}/read")
async def mark_as_read(
    notification_id: str,
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Đánh dấu notification là đã đọc
    """
    updated = await repo.mark_as_read(notification_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    return JSONResponse(content=jsonable_encoder(updated), status_code=200)


@notification_router.patch("/read-all")
async def mark_all_as_read(
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Đánh dấu tất cả notifications là đã đọc
    """
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    count = await repo.mark_all_as_read(user_id)
    return JSONResponse(content={"updated": count}, status_code=200)


@notification_router.delete("/{notification_id}")
async def delete_notification(
    notification_id: str,
    current_user: dict = Depends(get_current_user),
    repo = Depends(get_notification_repo)
):
    """
    Xóa notification
    """
    deleted = await repo.delete_notification(notification_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    return JSONResponse(content={"deleted": True}, status_code=200)

