from fastapi import APIRouter, Body, Depends
from starlette import status
from starlette.responses import JSONResponse, RedirectResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dependences.dependencies import get_user_repo
from exceptions import UserNotFoundException
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.user_service import UserService
from utils import auth
from fastapi import Request, Response
from schemas.auth_schemas import UserCreate, LoginRequest, TokenResponse, UserPrincipal
from i18n.translator import translate
from config.enum import MessageKey
from config.config import get_settings

settings = get_settings()

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
    hashed = auth.hash_password(password)
    return hashed

@auth_router.post("/logout")
async def logout(request: Request, response: Response):
    """
    đăng xuất thêm token vào danh sách đen redis
    """
    token = request.cookies.get("token_access")
    
    if token:
        try:
            expire_seconds = 3600
            auth.add_to_blacklist(token, expire_seconds)
        except Exception as e:
            print(f"Warning: Could not blacklist token: {e}")
    
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
async def Google(
    request: Request,
    response: Response,
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = AuthService(user_repo)
    result: TokenResponse = await service.handle_google_callback(request)

    redirect_url = f"{settings.frontend_url}/oauth/callback?oauth=google&status=success"
    redirect_response = RedirectResponse(url=redirect_url)
    redirect_response.set_cookie(key="token_access", value=result.access_token, httponly=True, secure=True, samesite="none")
    redirect_response.set_cookie(key="token_refresh", value=result.refresh_token, httponly=True, secure=True, samesite="none")
    redirect_response.set_cookie(key="current_user", value=result.user_principal.email, httponly=False, secure=True, samesite="none")
    return redirect_response

@auth_router.get("/facebook/login")
async def facebook(request: Request):
    return await AuthService.get_facebook_redirect_uri(request)

@auth_router.get("/facebook/callback")
async def Facebook(
    request: Request,
    response: Response,
    user_repo: UserRepository = Depends(get_user_repo)
):
    service = AuthService(user_repo)
    result: TokenResponse = await service.handle_facebook_callback(request)

    redirect_url = f"{settings.frontend_url}/oauth/callback?oauth=facebook&status=success"
    redirect_response = RedirectResponse(url=redirect_url)
    redirect_response.set_cookie(key="token_access", value=result.access_token, httponly=True, secure=True, samesite="none")
    redirect_response.set_cookie(key="token_refresh", value=result.refresh_token, httponly=True, secure=True, samesite="none")
    current_user_cookie = result.user_principal.email or str(result.user_principal.id)
    redirect_response.set_cookie(key="current_user", value=current_user_cookie, httponly=False, secure=True, samesite="none")
    return redirect_response

@auth_router.get("/session", response_model=TokenResponse)
async def get_session(
    request: Request,
    user_repo: UserRepository = Depends(get_user_repo)
):
    access_token = request.cookies.get("token_access")
    refresh_token = request.cookies.get("token_refresh")
    if not access_token or not refresh_token:
        return JSONResponse(status_code=401, content={"message": "Missing session cookies"})

    try:
        decoded = auth.validate_token(access_token)
        email = decoded.get("email")
        user_id = decoded.get("id")

        user_dict = None
        
        # Ưu tiên tìm bằng email nếu có (Google/NORMAL login)
        if email:
            user_dict = await user_repo.get_user_principal(email)
        
        # Nếu không có email hoặc không tìm thấy bằng email, tìm bằng id (Facebook login)
        if not user_dict and user_id:
            user_dict = await user_repo.get_by_id_str(str(user_id))
        
        if not user_dict:
            return JSONResponse(status_code=404, content={"message": "User not found"})

        user_principal = UserPrincipal(**user_dict)

        return TokenResponse(
            message=translate(MessageKey.LOGIN_SUCCESS),
            access_token=access_token,
            refresh_token=refresh_token,
            user_principal=user_principal
        )
    except Exception as e:
        print(f"Session error: {str(e)}")
        return JSONResponse(status_code=401, content={"message": "Invalid or expired session"})