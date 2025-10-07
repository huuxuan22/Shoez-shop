from openai import responses
from starlette.middleware.base import BaseHTTPMiddleware

from dependences.dependencies import set_language_dependency


class LocaleMiddlewave(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        lang = request.headers.get("Accept-Language","vi")
        await set_language_dependency(request)
        responses = await call_next(request)
        return responses