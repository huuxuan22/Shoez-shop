from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.exception import ForbiddenException, UnauthorizedException, SystemException, AuthTokenMissingException, \
    AuthException, AppException, UserExistException, UserNotFoundException
from exceptions.register_handlers import exception_handler
from i18n.translator import _


@exception_handler(UnauthorizedException)
async def unauthorized_handler(request: Request, exc: UnauthorizedException):
    return JSONResponse(
        status_code=401,
        content={"message": exc.message},
    )


@exception_handler(SystemException)
async def system_exception_handler(request: Request, exc: SystemException):
    # Dùng exc.message (string), hoặc translate nếu muốn
    return JSONResponse(
        status_code=500,
        # hoặc content={"message": exc.message}
        content={"message": _(exc.message)}
    )


@exception_handler(AuthTokenMissingException)
async def auth_token_exception_handler(request: Request, exc: AuthTokenMissingException):
    return JSONResponse(
        status_code=401,
        content={"message": _(exc.message)}
    )


@exception_handler(ForbiddenException)
async def forbidden_exception_handler(request: Request, exc: ForbiddenException):
    return JSONResponse(
        status_code=403,
        content={"message": _(exc.message)}
    )


@exception_handler(AuthException)
async def register_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(
        status_code=401,
        content={"message": _(exc.message)}
    )


@exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=500,
        content={"message": _(exc.message)}
    )


@exception_handler(UserExistException)
async def user_exist_exception_handler(request: Request, exc: UserExistException):
    return JSONResponse(
        status_code=404,
        content={"message": _(exc.message)}
    )


@exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": _(exc.message)}
    )
