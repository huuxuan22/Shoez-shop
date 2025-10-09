from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from dependences.dependencies import get_user_repo
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.user_service import UserService
from utils import auth
from fastapi import Request, Response
from schemas.auth_schemas import UserCreate, LoginRequest
auth_router = APIRouter(tags=["Auth"], prefix="/auth")
@auth_router.post("/register")
async def register(user: UserCreate,response : Response ,user_repo: UserRepository = Depends(get_user_repo)):
    service = UserService(user_repo)
    user_create =await service.create_user(user)
    token_access = auth.generate_token(user_create,exprices_delta=30*24*3600)
    token_refresh = auth.generate_token(user_create, exprices_delta=7*24*3600)
    response = JSONResponse(content={"message": "USER_CREATED"})
    response.set_cookie("token_access", token_access, httponly=True, max_age=86400)
    response.set_cookie("token_refresh", token_refresh, httponly=True, max_age=86400)
    return response

@auth_router.post("/login")
async def login(response: Response,login: LoginRequest = None,user_repo: UserRepository = Depends(get_user_repo)):
    user = await user_repo.get_user_principal(login.email)
    token_access = auth.generate_token(user, exprices_delta=30 * 24 * 3600)
    token_refresh = auth.generate_token(user, exprices_delta=7 * 24 * 3600)

    # 4️⃣ (Tùy chọn) Lưu token vào cookie
    response.set_cookie(key="token_access", value=token_access, httponly=True)
    response.set_cookie(key="token_refresh", value=token_refresh, httponly=True)
    response.set_cookie(key="current_user", value=user["email"], httponly=False)

    # 5️⃣ Trả response
    return {
        "message": "Login successful",
        "access_token": token_access,
        "refresh_token": token_refresh,
        "user": {
            "email": user["email"],
            "role": user["role"],
            "full_name": user.get("full_name"),
        },
    }

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