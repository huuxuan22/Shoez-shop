from pydantic import BaseModel, Field
from typing import List, Optional
from model.product_model import Product

class CartItemSchema(BaseModel):
    product: Product
    quantity: int

class CartCreateSchema(BaseModel):
    userId: str
    items: List[CartItemSchema]

class CartResponseSchema(CartCreateSchema):
    id: str = Field(..., alias="_id")
    totalPrice: float
    createdAt: Optional[str] = Field(None, alias="created_at")
    updatedAt: Optional[str] = Field(None, alias="updated_at")

    class Config:
        allow_population_by_field_name = True

class CartDeleteManySchema(BaseModel):
    ids: List[str]
