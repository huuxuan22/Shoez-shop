import uuid

from pydantic import Field, EmailStr, BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    email : EmailStr = Field(..., min_length=6, max_length=64, description="Email address")
    password : str = Field(..., min_length=6, max_length=64)
    full_name : str
    numberphone : str = Field(..., pattern=r"^(0|\+84)\d{9}$")
    avatar : str = None
    is_active : bool = True

    class Config:
        from_attributes = True

# class GoogleAuthRequest(BaseModel):
#     # token

