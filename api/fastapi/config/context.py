import uuid
from contextvars import ContextVar
from typing import Optional

from urllib3 import request

request_id: ContextVar[uuid.UUID] = ContextVar(
    "request_id", default=uuid.UUID("00000000-0000-0000-0000-000000000000")
)

current_email: ContextVar[Optional[str]] = ContextVar("current_email", default=None)

lang_var: ContextVar[str] = ContextVar("lang", default="en")

def get_current_lang() -> str:
    return lang_var.get()