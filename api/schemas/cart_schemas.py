from pydantic import BaseModel, Field
from typing import List, Optional, Union, Dict, Any
from model.product_model import Product

class CartItemSchema(BaseModel):
    product: Product
    quantity: int

class CartCreateSchema(BaseModel):
    userId: str
    items: List[CartItemSchema]

class AddCartItemSchema(BaseModel):
    product_id: str
    quantity: int
    size: str | int
    color: str

class CartItemStoredSchema(BaseModel):
    product: Dict[str, Any]
    size: Union[str, int]
    color: str
    quality: int

class CartDBSchema(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    userId: Optional[str] = None
    items: Optional[List[CartItemStoredSchema]] = None
    totalPrice: Optional[float] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        extra = "allow"

class CartResponseSchema(BaseModel):
    id: str
    user_id: Optional[str] = None
    items: Optional[List[CartItemStoredSchema]] = None
    totalPrice: float
    createdAt: Optional[str] = Field(None, alias="createdAt")
    updatedAt: Optional[str] = Field(None, alias="updatedAt")

    class Config:
        allow_population_by_field_name = True
        extra = "allow"

class CartDeleteManySchema(BaseModel):
    ids: List[str]
