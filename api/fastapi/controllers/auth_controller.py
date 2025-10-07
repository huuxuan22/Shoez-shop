from fastapi import APIRouter, Depends
from config.enum import MessageKey
from response.response import response_success
from dependences.user_validator import validate_unique_user
from services.auth_service import AuthService
from services.user_service import UserService
from utils import auth
from datetime import timedelta
from fastapi import Request, Response
from i18n.translator import _
from schemas.auth_schemas import UserCreate, LoginRequest
from fastapi.responses import RedirectResponse
auth_router = APIRouter(tags=["Auth"], prefix="/auth")
# @auth_router.post("/register")
# async def register(request: Request, response: Response = None, user_data: UserCreate = Depends(UserCreate)):
#     db = request.state.db
#     user = User(db).create_account(userCreate)
#     token_access = auth.generate_token(user,exprices_delta=30*24*3600)
#     token_refresh = auth.generate_token(user, exprices_delta=7*24*3600)
#     response.set_cookie("token_access", value=token_access, httponly=True, max_age=86400)
#     response.set_cookie("token_refresh", value=token_refresh, httponly=True, max_age=86400)
#     return response_success(_(MessageKey.USER_CREATED))

@auth_router.post("/login")
async def login(login: LoginRequest = None):
    print("")

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