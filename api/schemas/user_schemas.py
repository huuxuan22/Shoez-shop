from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from model.mongodb_base_model import PyObjectId
import uuid
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    password: Optional[str] = None
    age: Optional[int] = None
    numberphone: Optional[str] = None
    avatar: Optional[str] = None
    address: Optional[str] = None
    birthday: Optional[str] = None  # Format: YYYY-MM-DD
    gender: Optional[str] = None  # Values: male, female, other
    is_active: bool = True
    role_id: Optional[int] = None

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str

class IdUser(BaseModel):
    id: str

class UserUpdate(BaseModel):
    id: str
    full_name: Optional[str] = None
    numberphone: Optional[str] = None
    address: Optional[str] = None
    birthday: Optional[str] = None  # Format: YYYY-MM-DD
    gender: Optional[str] = None  # Values: male, female, other
    avatar: Optional[str] = None
    
class ResetPasswordRequest(BaseModel):
    id: str
    current_password: str
    new_password: str

class UserResponse(UserBase):
    id: PyObjectId = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }