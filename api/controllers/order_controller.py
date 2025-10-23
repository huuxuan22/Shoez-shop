from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional, Dict, Any, List
from datetime import datetime
from dependences.dependencies import get_order_repo
from repositories.order_repository import OrderRepository
from schemas.order_schemas import OrderResponseSchema, OrderCreateSchema, OrderUpdateStatusSchema
from services.order_service import OrderService
from services.order_filter_service import OrderFilterService
from config.database import get_database

order_router = APIRouter(prefix="/orders", tags=["Orders"])


def get_order_filter_service() -> OrderFilterService:
    """
    Dependency injection cho OrderFilterService
    Tuân thủ Dependency Inversion Principle
    """
    order_repo = OrderRepository(get_database())
    order_service = OrderService(order_repo)
    return OrderFilterService(order_service)

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
    starttime: Optional[str] = Query(None, description="Start time filter (ISO format)"),
    endtime: Optional[str] = Query(None, description="End time filter (ISO format)"),
    valueSearch: Optional[str] = Query(None, description="Search value for order ID, user ID, or status"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    """
    Lấy tất cả đơn hàng gần nhất theo phân trang cho admin với filter
    Tuân thủ Single Responsibility Principle và Dependency Inversion Principle
    """
    try:
        result = await filter_service.get_filtered_orders(
            page=page,
            limit=limit,
            start_time=starttime,
            end_time=endtime,
            search_value=valueSearch
        )
        
        return JSONResponse(
            content=jsonable_encoder(result),
            status_code=200
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid parameter: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@order_router.get("/admin/search", response_model=Dict[str, Any])
async def search_orders_admin(
    q: str = Query(..., description="Search query"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    """
    Tìm kiếm orders theo từ khóa
    """
    try:
        result = await filter_service.search_orders(
            search_term=q,
            page=page,
            limit=limit
        )
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")


@order_router.get("/admin/by-status", response_model=Dict[str, Any])
async def get_orders_by_status_admin(
    status: str = Query(..., description="Order status"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    """
    Lấy orders theo status
    """
    try:
        result = await filter_service.get_orders_by_status(
            status=status,
            page=page,
            limit=limit
        )
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Filter error: {str(e)}")


@order_router.get("/admin/by-date-range", response_model=Dict[str, Any])
async def get_orders_by_date_range_admin(
    start_date: str = Query(..., description="Start date (ISO format)"),
    end_date: str = Query(..., description="End date (ISO format)"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    """
    Lấy orders trong khoảng thời gian
    """
    try:
        result = await filter_service.get_orders_by_date_range(
            start_date=start_date,
            end_date=end_date,
            page=page,
            limit=limit
        )
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Date range error: {str(e)}")


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
