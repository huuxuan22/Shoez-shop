from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from dependences.dependencies import get_cart_repo
from repositories.cart_repository import CartRepository
from services import cart_service
from services.cart_service import CartService
from schemas.cart_schemas import CartCreateSchema, CartResponseSchema, CartDeleteManySchema, AddCartItemSchema
from config.database import get_database
from config.context import get_current_user

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

    return JSONResponse(content=jsonable_encoder(cart), status_code=200)

# Get cart by current user (UserContext)
@cart_router.get("/user", response_model=CartResponseSchema)
async def get_cart_current_user(cart_repo: CartRepository = Depends(get_cart_repo),
                                current_user: dict = Depends(get_current_user)):
    service = CartService(cart_repo)
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    cart = await service.get_cart_by_user(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return JSONResponse(content=jsonable_encoder(cart), status_code=200)

@cart_router.post("/item")
async def add_item_to_cart(payload: AddCartItemSchema,
                           cart_repo: CartRepository = Depends(get_cart_repo),
                           current_user: dict = Depends(get_current_user)):
    service = CartService(cart_repo)
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    updated = await service.add_item(user_id, {
        "product_id": payload.product_id,
        "quantity": payload.quantity,
        "size": payload.size,
        "color": payload.color
    })
    if not updated:
        raise HTTPException(status_code=400, detail="Could not add item to cart")
    return JSONResponse(content=jsonable_encoder(updated), status_code=200)
    
@cart_router.delete("/delete-multiple")
async def delete_multiple_carts(payload: CartDeleteManySchema, cart_repo: CartRepository = Depends(get_cart_repo)):
    service = CartService(cart_repo)
    count = await service.delete_multiple_carts(payload.ids)
    return JSONResponse(content="OK", status_code=200)

