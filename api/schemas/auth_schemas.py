import uuid
from typing import Union, Optional

from pydantic import Field, EmailStr, BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email : EmailStr = Field(..., min_length=6, max_length=64, description="Email address")
    password : str = Field(..., min_length=6, max_length=64)
    full_name : str
    numberphone : str = Field(..., pattern=r"^(0|\+84)\d{9}$")
    avatar : str = None
    is_active : bool = True

    class Config:
        from_attributes = True

class UserPrincipal(BaseModel):
    id: Union[str, uuid.UUID] = Field(default_factory=uuid.uuid4)
    email: EmailStr
    full_name: Optional[str] = None
    numberphone: Optional[str] = None
    age: Optional[int] = None
    avatar: Optional[str] = None
    is_active: bool = True
    address: Optional[str] = None
    birthday: Optional[str] = None  # Format: YYYY-MM-DD
    gender: Optional[str] = None  # Values: male, female, other

    class Config:
        orm_mode = True  # Giúp chuyển từ dict/DB object sang schema

class TokenResponse(BaseModel):
    message: str
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    user_principal: UserPrincipal
