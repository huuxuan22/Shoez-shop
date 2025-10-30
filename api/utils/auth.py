import uuid
from datetime import datetime, timedelta
from typing import Optional, Any
import redis
import bcrypt
from jose import jwt, JWTError
from config.config import get_settings
from pydantic import BaseModel
from config.enum import MessageKey
from exceptions.exception import AuthTokenMissingException, AuthException
from datetime import datetime, timedelta, timezone  # Thêm timezone
from typing import Any, Optional
from jose import jwt

class TokenData(BaseModel):
    email: Optional[str] = None

setting = get_settings()

def generate_token(data: dict[str, Any], exprices_delta: Optional[int] = None) -> str:
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
        payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
        return payload
    except JWTError as e:
        raise AuthTokenMissingException(MessageKey.TOKEN_INVALID)

def extract_email(token: str) -> Optional[str]:
    claims = extract_all_claims(token)
    email = claims.get("email")
    return email

def extract_id(token: str) -> Optional[str]:
    claims = extract_all_claims(token)
    user_id = claims.get("id")
    if not user_id:
        user_id = claims.get("sub")  
    return str(user_id) if user_id else None

def extract_role(token: str) -> str:
    claims = extract_all_claims(token)
    role = claims.get("role")
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

# xác thực token - hỗ trợ cả case có email và không có email (Facebook)
def validate_token(token: str) -> dict[str,Any]:
    """
    Validate token và trả về thông tin user.
    Hỗ trợ cả token có email (Google/NORMAL) và token không có email (Facebook).
    
    Returns:
        dict với keys: email (optional), id (required), role (required)
    """
    claims = extract_all_claims(token)
    email = extract_email(token)
    user_id = extract_id(token)
    role = extract_role(token)
    
    # Phải có ít nhất id hoặc email, và phải có role
    if not user_id and not email:
        raise AuthTokenMissingException(MessageKey.USER_NOT_FOUND)
    if not role:
        raise AuthTokenMissingException(MessageKey.USER_NOT_FOUND)
    
    result = {"role": role}
    if user_id:
        result["id"] = user_id
    if email:
        result["email"] = email
    
    return result

# Hash password
def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash"""
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return False

try:
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True, socket_connect_timeout=1)
    r.ping()
    REDIS_AVAILABLE = True
except Exception:
    r = None
    REDIS_AVAILABLE = False
    print("Warning: Redis not available. Token blacklist will be disabled.")

def add_to_blacklist(token: str, expire_seconds: int):
    """Add token to blacklist. Does nothing if Redis is not available."""
    if REDIS_AVAILABLE and r:
        try:
            r.set(token, "blacklisted", ex=expire_seconds)
        except Exception as e:
            print(f"Warning: Could not add token to blacklist: {e}")

def is_blacklisted(token: str) -> bool:
    """Check if token is blacklisted. Returns False if Redis is not available."""
    if not REDIS_AVAILABLE or not r:
        return False
    try:
        return r.exists(token) == 1
    except Exception:
        return False



