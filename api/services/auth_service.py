from http.client import HTTPException

import httpx
from alembic.util import status
from sqlalchemy.orm import Session

from config.config import Settings
from config.enum import MessageKey
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

    async def login(self, email: str, password: str) -> "TokenResponse":
        # Lấy user principal từ repo
        user_dict = await self.user_repository.get_user_principal(email)
        if not user_dict:
            raise HTTPException(status_code=404, detail="User not found")

        # Kiểm tra password
        if password != user_dict.get("password"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

        user_principal = UserPrincipal(**user_dict)
        to_encode = convert_uuid_to_str(user_principal.dict())
        # Tạo token
        token_access = auth.generate_token(to_encode, exprices_delta=30 * 24 * 3600)
        token_refresh = auth.generate_token(to_encode, exprices_delta=7 * 24 * 3600)

        return TokenResponse(
            message="Login successful",
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







