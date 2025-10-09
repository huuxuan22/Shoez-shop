import uuid
from datetime import datetime, timedelta
from typing import Optional, Any

from jose import jwt, JWTError

from config.config import get_settings
from pydantic import BaseModel

from config.enum import MessageKey
from exceptions.exception import AuthTokenMissingException, AuthException


class TokenData(BaseModel):
    email: Optional[str] = None

setting = get_settings()

# đây là để tạo token
from datetime import datetime, timedelta, timezone  # Thêm timezone
from typing import Any, Optional
from jose import jwt


# ... import setting của bạn

def generate_token(data: dict[str, Any], exprices_delta: Optional[int] = None) -> str:
    # Sao chép và làm sạch dữ liệu
    to_encode = {}
    for key, value in data.items():
        if isinstance(value, datetime):
            to_encode[key] = value.isoformat()
        else:
            to_encode[key] = value
    exprice = datetime.now(timezone.utc) + timedelta(
        seconds=exprices_delta if exprices_delta else setting.access_token_expire_seconds
    )
    to_encode.update({"exp": int(exprice.timestamp())})
    encode_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)
    return encode_jwt

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta = timedelta(days=7)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire, "scope": "refresh_token"})
    encoded_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)
    return encoded_jwt
# giải mã token
def extract_all_claims(token: str) -> dict[str,Any]:
    try:
        print("nhìn cháo gì")
        payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
        return payload
    except JWTError as e:
        raise AuthTokenMissingException(MessageKey.TOKEN_INVALID)

# lấy email từ token
def extract_email(token: str) -> str:
    claims = extract_all_claims(token)
    email = str = claims.get("email")
    if not email:
        raise AuthTokenMissingException(MessageKey.NOT_FOUND_USER_IN_TOKEN)

    return email

def extract_role(token: str) -> str:
    claims = extract_all_claims(token)
    role = str = claims.get("role")
    if not role:
        raise AuthTokenMissingException(MessageKey.NOT_FOUND_USER_IN_TOKEN)

    return role

# kiểm tra token hết hạn
def is_token_expired(token: str) -> bool:
    claims = extract_all_claims(token)
    ex_timestamp = claims.get("exp")
    if ex_timestamp is None:
        return True
    expiration = datetime.utcfromtimestamp(ex_timestamp)
    return datetime.utcnow() > expiration

# xác thực token
def validate_token(token: str) -> dict[str,Any]:
    claims = extract_all_claims(token)
    email = extract_email(token)
    role = extract_role(token)
    if not email:
        raise AuthTokenMissingException(MessageKey.USER_NOT_FOUND)
    if not role:
        raise AuthTokenMissingException(MessageKey.USER_NOT_FOUND)
    return {"email": email, "role": role}



