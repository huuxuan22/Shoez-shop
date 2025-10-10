from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from config.config import get_settings
from config.enum import MessageKey
from dependences.dependencies import set_language_dependency, get_user_repo
from exceptions.exception import AuthTokenMissingException, SystemException, AppException,UnauthorizedException
from repositories.user_repository import UserRepository
from utils.auth import validate_token
from exceptions.exception import AuthTokenMissingException,AuthException
from config.logging_conf import logger
from response.response import response_fail
from i18n.translator import _
from fastapi.responses import JSONResponse
from config.context import current_user
settings = get_settings()


async def _authenticate_user(self, request: Request):
    token = request.cookies.get("token_access")
    if not token:
        raise AuthTokenMissingException(MessageKey.TOKEN_INVALID)

    decoded_token = validate_token(token)
    email = decoded_token["email"]

    db = request.state.db
    user_repo = UserRepository(db)

    user = await user_repo.get_user_principal(email)
    if not user:
        raise AuthTokenMissingException(MessageKey.USER_NOT_FOUND)
    current_user.set(user)
    request.state.user = user


class AuthMiddlewave(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.__exact_path_rules = self.__process_path_rules(self.__disable_auth_paths, add_prefix=True)
        self.__prefix_path_rules = self.__process_path_rules(self.__prefix_paths)

        # Luôn bypass swagger paths, không thêm prefix
        for path in self.__swagger_paths:
            self.__exact_path_rules[path] = None

    __disable_auth_paths = [
        "/auth/login",
        "/auth/register",
        "auth/logout",
        "auth/logout-user",
        "auth/login-user",
        "auth/register-user",
        "/info",
        "/user/reset-password",
        "/user/forgot-password",
        "/auth/verify-otp",
        "/auth/resend-otp",
        "/auth/google/login",
        "/auth/google/callback",
        "/auth/facebook/login",
        "/auth/facebook/callback",
        "pwd",
        "/test",
        "/users/",
        "/products/",
    ]

    __prefix_paths = [
        "/users/verify-reset-token/",
        ("/sys-err-mngmnt", ["POST"]),
        ("/invitations/", ["GET"]),
        ("/image", ["POST", "GET"]),
        ("/auth/google/login", ["GET"]),
        ("/auth/google/callback", ["GET"]),
    ]

    # Swagger mặc định của FastAPI
    __swagger_paths = ["/docs", "/redoc", "/openapi.json"]

    @staticmethod
    def __process_path_rules(paths, add_prefix=True):
        rules = {}
        for item in paths:
            if isinstance(item, str):
                path_str = settings.api_prefix + item if add_prefix else item
                rules[path_str] = None
            elif isinstance(item, tuple) and len(item) == 2:
                path_str, method = item
                if add_prefix:
                    path_str = settings.api_prefix + path_str
                rules[path_str] = set(method) if method else None
        return rules

    def _should_bypass_auth(self, path: str, method: str):
        if path in self.__exact_path_rules:
            methods = self.__exact_path_rules[path]
            bypass = methods is None or method in methods
            if bypass:
                return True

        for prefix, methods in self.__prefix_path_rules.items():
            if path.rstrip("/").startswith(prefix.rstrip("/")):
                if methods is None or method in methods:
                    return True

        return False

    async def dispatch(self, request: Request, call_next):
        try:
            lang = request.headers.get("accept-language")
            await set_language_dependency(request)
            path = request.url.path
            method = request.method
            by_pass = self._should_bypass_auth(path, method)

            if not by_pass:
                await _authenticate_user(self, request)

            response = await call_next(request)
            return response

        except (AuthException, AuthTokenMissingException) as e:
            return response_fail(_(e.message))
        except AppException as e:
            return response_fail(_(e.message))
        except SystemException as e:
            logger.exception(f"Unexpected error in auth middleware: {e}")
            return response_fail(_(e.message))
        finally:
            logger.info(">>>>>> End auth")


