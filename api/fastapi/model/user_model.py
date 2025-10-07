from typing import Optional
from model.mongodb_base_model import BaseMongoModel


class User(BaseMongoModel):
    email: str
    password: str
    full_name: Optional[str] = None
    numberphone: Optional[str] = None
    age: Optional[int] = None
    avatar: Optional[str] = None
    is_active: bool = True
    role_id: Optional[int] = None



