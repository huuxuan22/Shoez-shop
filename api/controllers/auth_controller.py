from fastapi import APIRouter, Body, Depends
from starlette import status
from starlette.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dependences.dependencies import get_user_repo
from exceptions import UserNotFoundException
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.user_service import UserService
from utils import auth
from fastapi import Request, Response
from schemas.auth_schemas import UserCreate, LoginRequest, TokenResponse
from i18n.translator import translate
from config.enum import MessageKey

security = HTTPBearer()
auth_router = APIRouter(tags=["Auth"], prefix="/auth")

@auth_router.post("/register", response_model=TokenResponse)
async def register(
    user: UserCreate,
    response: Response,
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = AuthService(user_repo)
    result: TokenResponse = await service.register(user)
    
    # Set cookies
    response.set_cookie(key="token_access", value=result.access_token, httponly=True)
    response.set_cookie(key="token_refresh", value=result.refresh_token, httponly=True)
    response.set_cookie(key="current_user", value=result.user_principal.email, httponly=False)
    
    return result

@auth_router.post("/login", response_model=TokenResponse)
async def login(
    response: Response,
    login: LoginRequest,
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = AuthService(user_repo)
    result: TokenResponse = await service.login(login.email, login.password)

    # ✅ Set cookies
    response.set_cookie(key="token_access", value=result.access_token, httponly=True)
    response.set_cookie(key="token_refresh", value=result.refresh_token, httponly=True)
    response.set_cookie(key="current_user", value=result.user_principal.email, httponly=False)

    return result

@auth_router.post("/pwd")
async def hash_password(password: str = Body(..., embed=True)):
    """
    Nhận password string, trả về hash
    Body JSON ví dụ: { "password": "123" }
    """
    hashed = auth.pwd_context.hash(password)
    return hashed

@auth_router.post("/logout")
async def logout(request: Request, response: Response):
    """
    Logout user by clearing cookies and optionally blacklisting token
    """
    # Get token from cookie
    token = request.cookies.get("token_access")
    
    # Try to blacklist token if Redis is available
    if token:
        try:
            expire_seconds = 3600
            auth.add_to_blacklist(token, expire_seconds)
        except Exception as e:
            # Redis might not be available, just log and continue
            print(f"Warning: Could not blacklist token: {e}")
    
    # Clear all auth cookies
    response.delete_cookie(key="token_access")
    response.delete_cookie(key="token_refresh")
    response.delete_cookie(key="current_user")
    
    return JSONResponse({
        "success": True, 
        "message": translate(MessageKey.LOGOUT_SUCCESS)
    })

@auth_router.get("/google/login")
async def facebook(request: Request):
    return await AuthService.get_google_redirect_uri(request)

@auth_router.get("/google/callback")
async def Google(request: Request):
    return await AuthService.handle_google_callback(request)

@auth_router.get("/facebook/login")
async def facebook(request: Request):
    return await AuthService.get_facebook_redirect_uri(request)

@auth_router.get("/facebook/callback")
async def Google(request: Request):
    return await AuthService.handle_facebook_callback(request)