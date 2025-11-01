from typing import List
from fastapi import Form, HTTPException, Query, UploadFile, File
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from dependences.permissions import require_roles
from schemas.user_schemas import ResetPasswordRequest, UserCreate, UserUpdate, LockUsersRequest, RestoreUsersRequest
from fastapi import APIRouter, Depends
from repositories.user_repository import UserRepository
from services.user_service import UserService
from dependences.dependencies import get_user_repo
user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/get-all")
@require_roles("ADMIN")
async def get_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = UserService(user_repo)
    user_list = await service.list_users(page=page, page_size=page_size)
    return (JSONResponse(status_code=200, content={"user_list": user_list}))

@user_router.post("/")
async def create_user(user: UserCreate, user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    user_create = service.create_user(user)
    return (JSONResponse(status_code=200, content={"user_create": user_create}))

@user_router.put("/")
async def update_user(user: UserUpdate, user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    user_update = await service.update_user(user)

    return (JSONResponse(status_code=200, content={"user_update": jsonable_encoder(user_update)}))


@user_router.put("/reset-password", summary="Đổi mật khẩu người dùng")
async def reset_password(
    payload: ResetPasswordRequest,
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    API đổi mật khẩu người dùng.
    - Nhận vào: id, current_password, new_password
    - Kiểm tra mật khẩu hiện tại
    - Hash mật khẩu mới và cập nhật vào DB
    """
    service = UserService(user_repo)

    try:
        result = await service.reset_password(
            user_id=payload.id,
            current_pw=payload.current_password,
            new_pw=payload.new_password
        )
        return JSONResponse(
            status_code=200,
            content={
                "message": "Đổi mật khẩu thành công.",
                "data": result
            }
        )

    except HTTPException as e:
        raise e

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ, vui lòng thử lại sau.")


@user_router.post("/avatar")
async def upload_avatar(
    user_id: str = Form(...),  
    file: UploadFile = File(..., alias="avatar"),
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = UserService(user_repo)
    avatar_url = await service.upload_avatar(user_id=user_id, file=file)
    return JSONResponse(status_code=200, content={"avatar_url": avatar_url})

@user_router.delete("/")
@require_roles("ADMIN")
async def delete_user(ids: List[str], user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    deleted = await service.delete_user(ids)
    return JSONResponse(status_code=200, content={"deleted": deleted})

@user_router.patch("/admin/lock")
@require_roles("ADMIN")
async def lock_users(payload: LockUsersRequest, user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    modified = await service.lock_users(payload.ids, payload.is_active)
    return JSONResponse(status_code=200, content={"modified": modified})

@user_router.patch("/admin/restore")
@require_roles("ADMIN")
async def restore_users(payload: RestoreUsersRequest, user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    modified = await service.restore_users(payload.ids)
    return JSONResponse(status_code=200, content={"modified": modified})

