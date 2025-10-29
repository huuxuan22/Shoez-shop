from typing import Optional, Union
from pydantic import BaseModel
from bson import ObjectId
from uuid import UUID

from model.mongodb_base_model import BaseMongoModel


class User(BaseMongoModel):
    id: Union[str, UUID]
    email: Optional[str] = None  
    password: Optional[str] = None  
    full_name: Optional[str] = None
    numberphone: Optional[str] = None
    age: Optional[int] = None
    avatar: Optional[str] = None
    address: Optional[str] = None
    birthday: Optional[str] = None  
    gender: Optional[str] = None  
    is_active: bool = True
    role: Optional[str] = None
    is_login: Optional[str] = None  # Values: "GOOGLE", "FACEBOOK", "NORMAL"

    def to_token_dict(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "role": self.role
        }

    class Config:
        json_encoders = {
            ObjectId: lambda v: str(v),
            UUID: lambda v: str(v)
        }
