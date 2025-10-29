from pydantic import BaseModel, Field
from typing import List, Optional

class FavouriteProductSchema(BaseModel):
    user_id: str
    product: List[str] = []

class FavouriteProductCreateSchema(BaseModel):
    user_id: str
    product: List[str] = []

class FavouriteProductResponseSchema(FavouriteProductSchema):
    _id: Optional[str] = None

    class Config:
        orm_mode = True
