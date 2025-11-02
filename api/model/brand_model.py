from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from uuid import UUID

from model.mongodb_base_model import BaseMongoModel


class Brand(BaseMongoModel):
    name: str = Field(..., description="Tên thương hiệu")
    logo: Optional[str] = Field(None, description="URL logo thương hiệu")
    description: Optional[str] = Field(None, description="Mô tả thương hiệu")
    is_active: bool = Field(True, description="Trạng thái hoạt động")

    class Config:
        validate_by_name = True
        from_attributes = True
        json_encoders = {
            ObjectId: lambda v: str(v),
            UUID: lambda v: str(v),
        }
        json_schema_extra = {
            "example": {
                "name": "Nike",
                "logo": "http://minio:9000/trademark/nike_logo.png",
                "description": "Thương hiệu giày thể thao hàng đầu thế giới",
                "is_active": True
            }
        }

