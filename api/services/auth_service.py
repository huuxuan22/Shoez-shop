
from fastapi import HTTPException
import httpx
from alembic.util import status
from sqlalchemy.orm import Session

from config.config import Settings
from config.enum import ErrorCode, MessageKey
from exceptions.exception import UserExistException, UserNotFoundException
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from schemas.auth_schemas import UserCreate, LoginRequest, UserPrincipal, TokenResponse
from utils.utils import hash_password, verify_password, convert_uuid_to_str
from config.enum import RoleEnum
from authlib.integrations.starlette_client import OAuth
from utils import auth
from fastapi.responses import RedirectResponse
from model.user_model import User
from i18n.translator import translate
settings = Settings()

oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url=settings.server_metadata_url,
    client_id=settings.google_client_id,
    client_secret=settings.google_client_secret,
    client_kwargs=settings.client_kwargs
)

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register(self, user_data: UserCreate) -> "TokenResponse":
        """
        Đăng ký user mới
        
        Args:
            user_data: Thông tin user cần đăng ký (email, password, full_name, numberphone, etc.)
            
        Returns:
            TokenResponse: Access token, refresh token và thông tin user
            
        Raises:
            HTTPException: Nếu email đã tồn tại hoặc có lỗi validation
        """
        # Kiểm tra email đã tồn tại chưa
        existing_user = await self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=ErrorCode.CONFLICT, 
                detail=translate(MessageKey.USER_EXIST)
            )
        
        # Hash password trước khi lưu
        hashed_password = hash_password(user_data.password)
        
        # Tạo user mới
        user_dict = user_data.dict()
        user_dict['password'] = hashed_password
        user_dict['role'] = "USER"
        # Don't add id field here, it will be set after creation
        
        # Lưu user vào database
        created_user = await self.user_repository.create(user_dict)
        
        # Set id = _id after creation
        if created_user and '_id' in created_user:
            created_user['id'] = str(created_user['_id'])
            # Update the document to add id field
            await self.user_repository.db["users"].update_one(
                {"_id": created_user['_id']},
                {"$set": {"id": created_user['id']}}
            )
        
        # Tạo user principal để trả về
        user_principal = UserPrincipal(
            id=created_user.get('id'),
            email=created_user.get('email'),
            full_name=created_user.get('full_name'),
            numberphone=created_user.get('numberphone'),
            avatar=created_user.get('avatar'),
            is_active=created_user.get('is_active', True),
            role=created_user.get('role')
        )
        
        # Tạo token
        to_encode = convert_uuid_to_str(user_principal.dict())
        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)
        
        return TokenResponse(
            message=translate(MessageKey.USER_CREATED),
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )

    async def login(self, email: str, password: str) -> "TokenResponse":
        user_dict = await self.user_repository.get_user_principal(email)
        if not user_dict:
            raise HTTPException(status_code=ErrorCode.NOT_FOUND, detail="Không tìm thấy người dùng")

        # Verify password using bcrypt
        hashed_password = user_dict.get("password")
        if not auth.verify_password(password, hashed_password):
            raise HTTPException(status_code=ErrorCode.BAD_REQUEST, detail="Sai mật khẩu")

        user_principal = UserPrincipal(**user_dict)
        to_encode = convert_uuid_to_str(user_principal.dict())

        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)

        return TokenResponse(
            message=translate(MessageKey.LOGIN_SUCCESS),
            access_token=token_access,
            refresh_token=token_refresh,
            user_principal=user_principal
        )

    @staticmethod
    async def get_google_redirect_uri(request):
        redirect_uri = f"{settings.backend_url}/auth/google/callback"
        return await oauth.google.authorize_redirect(request, redirect_uri)

    @staticmethod
    async def get_facebook_redirect_uri(request):
        # Redirect người dùng tới Facebook OAuth
        fb_auth_url = (
            f"https://www.facebook.com/v16.0/dialog/oauth?"
            f"client_id={settings.facebook_app_id}&"
            f"redirect_uri={settings.backend_url}/auth/facebook/callback&"
            f"response_type=code&"
            f"scope=email"  # Đảm bảo scope được truyền đúng
            f"auth_type=rerequest"
        )
        return RedirectResponse(fb_auth_url)

    @staticmethod
    async def handle_google_callback(request):
        token = await oauth.google.authorize_access_token(request)
        user = token.get("userinfo")

        payload = {"sub": user["email"], "name": user["name"]}
        jwt_token = auth.generate_token(payload)

        access_token = auth.create_access_token(user)
        refresh_token = auth.create_refresh_token(user)

        redirect_url = f"{settings.frontend_url}/home"
        response = RedirectResponse(url=redirect_url)
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,  # FE không đọc được
            secure=True,  # bật khi chạy HTTPS
            samesite="lax",  # hoặc "strict" nếu cần
            max_age=7 * 24 * 60 * 60  # 7 ngày
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,  # FE không đọc được
            secure=True,  # bật khi chạy HTTPS
            samesite="lax",  # hoặc "strict" nếu cần
            max_age=7 * 24 * 60 * 60  # 7 ngày
        )
        return response

    @staticmethod
    async def handle_facebook_callback(request):
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(status_code=400, detail="No code provided by Facebook")

        # 1. Đổi code lấy access_token từ Facebook (KHÔNG thêm scope=email)
        token_url = (
            f"https://graph.facebook.com/v16.0/oauth/access_token?"
            f"client_id={settings.facebook_app_id}&"
            f"redirect_uri={settings.backend_url}/auth/facebook/callback&"
            f"client_secret={settings.facebook_app_secret}&"
            f"code={code}"
        )

        async with httpx.AsyncClient() as client:
            token_res = await client.get(token_url)
            token_data = token_res.json()
            fb_access_token = token_data.get("access_token")
            if not fb_access_token:
                raise HTTPException(status_code=400, detail="Cannot get Facebook access token")

            # 2. Lấy user info từ Facebook (id, name, email)
            profile_url = "https://graph.facebook.com/me"
            params = {"fields": "id,name,email", "access_token": fb_access_token}
            profile_res = await client.get(profile_url, params=params)
            user_info = profile_res.json()

        # 3. Tạo payload chuẩn cho JWT
        payload = {"sub": user_info["id"], "name": user_info.get("name"), "email": user_info.get("email")}
        access_token = auth.create_access_token(payload)
        refresh_token = auth.create_refresh_token(payload)

        # 4. Redirect về FE + set cookie refresh_token
        redirect_url = f"{settings.frontend_url}/home"
        response = RedirectResponse(url=redirect_url)

        # Refresh token -> httponly cookie (BE đọc)
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,  # bật khi chạy HTTPS
            samesite="lax",
            max_age=7 * 24 * 60 * 60
        )

        # Access token -> cookie FE có thể đọc (hoặc localStorage)
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=False,  # FE có thể đọc
            secure=True,
            samesite="lax",
            max_age=15 * 60  # ví dụ 15 phút
        )

        return response







