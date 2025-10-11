from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional, Dict, Any,List
from dependences.dependencies import get_order_repo
from repositories.order_repository import OrderRepository
from schemas.order_schemas import OrderResponseSchema, OrderCreateSchema, OrderUpdateStatusSchema
from services.order_service import OrderService
from config.database import get_database

order_router = APIRouter(prefix="/orders", tags=["Orders"])

@order_router.post("/", response_model=OrderResponseSchema)
async def create_order(order_data: OrderCreateSchema, order_repo: OrderRepository = Depends(lambda: OrderRepository(get_database()))):
    service = OrderService(order_repo)
    created_order = await service.create_order(order_data)
    return JSONResponse(content=jsonable_encoder(created_order), status_code=200)

@order_router.get("/user")
async def get_orders(id: str = Query(..., description="User ID"), order_repo=Depends(get_order_repo)):
    if not id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    service = OrderService(order_repo)
    orders = await service.get_orders_by_user(id)
    return JSONResponse(content=orders, status_code=200)


@order_router.get("/admin/orders", response_model=Dict[str, Any])
async def get_all_orders_admin(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    order_repo: OrderRepository = Depends(lambda: OrderRepository(get_database()))
):
    """
    Lấy tất cả đơn hàng gần nhất theo phân trang cho admin
    Trả về danh sách orders và tổng số trang
    """
    service = OrderService(order_repo)
    total_orders = await service.count_orders()
    total_pages = (total_orders + limit - 1) // limit  # ceil(total_orders / limit)

    # Lấy danh sách order theo page, limit
    orders = await service.get_orders_paginated(skip=(page - 1) * limit, limit=limit)

    return JSONResponse(
        content=jsonable_encoder({
            "total_pages": total_pages,
            "current_page": page,
            "total_orders": total_orders,
            "orders": orders
        }),
        status_code=200
    )

@order_router.get("/admin/all", response_model=List[OrderResponseSchema])
async def get_all_orders(order_repo: OrderRepository = Depends(lambda: OrderRepository(get_database()))):
    """
    Lấy toàn bộ đơn hàng, sắp xếp theo created_at giảm dần (gần nhất trước)
    Dùng cho admin, không phân trang
    """
    service = OrderService(order_repo)

    orders = await service.count_orders()

    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")

    return JSONResponse(content=jsonable_encoder(orders), status_code=200)

@order_router.patch("/admin/update-status", response_model=OrderResponseSchema)
async def update_order_status(
    payload: OrderUpdateStatusSchema,
    order_repo: OrderRepository = Depends(get_order_repo)
):
    service = OrderService(order_repo)
    updated_order = await service.update_order_status(payload.order_id, payload.status)
    if not updated_order:
        raise HTTPException(status_code=400, detail="Cannot update order status")
    return JSONResponse(content=jsonable_encoder(updated_order), status_code=200)
