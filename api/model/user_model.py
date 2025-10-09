from typing import Optional, Union
from pydantic import BaseModel
from bson import ObjectId
from uuid import UUID

from model.mongodb_base_model import BaseMongoModel


class User(BaseMongoModel):
    id: Union[str, UUID]
    email: str
    password: str
    full_name: Optional[str] = None
    numberphone: Optional[str] = None
    age: Optional[int] = None
    avatar: Optional[str] = None
    is_active: bool = True
    role: Optional[str] = None

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
