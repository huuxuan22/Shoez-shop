from uuid import UUID
from sqlalchemy.testing.suite.test_reflection import users
from passlib.context import CryptContext

# Tạo context bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
def convert_uuid_to_str(data):
    if isinstance(data, dict):
        return {k: convert_uuid_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_uuid_to_str(i) for i in data]
    elif isinstance(data, UUID):
        return str(data)
    else:
        return data