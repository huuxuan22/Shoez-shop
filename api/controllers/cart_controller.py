from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from dependences.dependencies import get_cart_repo
from repositories.cart_repository import CartRepository
from services import cart_service
from services.cart_service import CartService
from schemas.cart_schemas import CartCreateSchema, CartResponseSchema, CartDeleteManySchema
from config.database import get_database

cart_router = APIRouter(prefix="/cart", tags=["Cart"])

@cart_router.post("/", response_model=CartResponseSchema)
async def create_cart(cart_data: CartCreateSchema, cart_repo: CartRepository = Depends(get_cart_repo)):
    service = CartService(cart_repo)
    created_cart = await service.create_cart(cart_data)

    return JSONResponse(content=jsonable_encoder(created_cart), status_code=200)

@cart_router.get("/user/{user_id}", response_model=CartResponseSchema)
async def get_cart(user_id: str, cart_repo: CartRepository = Depends(get_cart_repo)):
    service = CartService(cart_repo)
    cart = await service.get_cart_by_user(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    # Trả về JSONResponse với status_code=200
    return JSONResponse(content=jsonable_encoder(cart), status_code=200)
#
# # Thêm item vào cart
@cart_router.delete("/delete-multiple")
async def delete_multiple_carts(payload: CartDeleteManySchema, cart_repo: CartRepository = Depends(get_cart_repo)):
    service = CartService(cart_repo)
    count = await service.delete_multiple_carts(payload.ids)
    return JSONResponse(content="OK", status_code=200)

