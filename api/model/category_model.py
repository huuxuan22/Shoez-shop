from typing import Optional
from model.mongodb_base_model import BaseMongoModel


class Category(BaseMongoModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True

    class Config:
        validate_by_name = True
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Sneakers",
                "description": "Giày thể thao, sneaker",
                "is_active": True
            }
        }

