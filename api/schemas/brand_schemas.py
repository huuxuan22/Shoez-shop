from pydantic import BaseModel, Field
from typing import Optional


class BrandCreate(BaseModel):
    name: str = Field(..., description="Tên thương hiệu")
    logo: Optional[str] = Field(None, description="URL logo thương hiệu")
    description: Optional[str] = Field(None, description="Mô tả thương hiệu")
    is_active: Optional[bool] = Field(True, description="Trạng thái hoạt động")


class BrandUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Tên thương hiệu")
    logo: Optional[str] = Field(None, description="URL logo thương hiệu")
    description: Optional[str] = Field(None, description="Mô tả thương hiệu")
    is_active: Optional[bool] = Field(None, description="Trạng thái hoạt động")


class BrandResponse(BaseModel):
    id: str
    name: str
    logo: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

