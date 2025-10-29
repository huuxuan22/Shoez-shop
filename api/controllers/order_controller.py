from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional, Dict, Any, List
from dependences.dependencies import get_order_repo
from repositories.order_repository import OrderRepository
from schemas.order_schemas import OrderResponseSchema, OrderCreateSchema, OrderUpdateStatusSchema
from services.order_service import OrderService
from services.order_filter_service import OrderFilterService
from config.database import get_database
from config.context import get_current_user

order_router = APIRouter(prefix="/orders", tags=["Orders"])

def get_notification_service():
    """Lazy import notification_service"""
    from services.notification_service import notification_service
    return notification_service

def get_order_filter_service() -> OrderFilterService:
    order_repo = OrderRepository(get_database())
    order_service = OrderService(order_repo)
    return OrderFilterService(order_service)

@order_router.post("/", response_model=OrderResponseSchema)
async def create_order(order_data: OrderCreateSchema, order_repo: OrderRepository = Depends(lambda: OrderRepository(get_database()))):
    """
    Tạo đơn hàng mới và gửi notification cho admin
    Giải thích: 
    - Tạo order như bình thường
    - Sau khi tạo thành công, gửi notification cho admin để xác nhận
    """
    service = OrderService(order_repo)
    created_order = await service.create_order(order_data)
    
    try:
        order_id = str(created_order.get('id') or created_order.get('_id'))
        notif_service = get_notification_service()
        await notif_service.send_new_order_notification_to_admin(
            order_id=order_id,
            customer_name=order_data.fullName,
            order_total=order_data.total
        )
    except Exception as e:
        print(f"Error sending notification: {e}")
    
    return JSONResponse(content=jsonable_encoder(created_order), status_code=200)

@order_router.get("/user")
async def get_orders(order_repo=Depends(get_order_repo), 
                     current_user: dict = Depends(get_current_user)):
    """
    Lấy tất cả đơn hàng của user hiện tại (dùng user_context)
    """
    # Lấy user_id từ current_user context
    user_id = str(current_user.get("_id") or current_user.get("id"))
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    service = OrderService(order_repo)
    orders = await service.get_orders_by_user(user_id)
    return JSONResponse(content=orders, status_code=200)


@order_router.get("/admin/orders", response_model=Dict[str, Any])
async def get_all_orders_admin(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    starttime: Optional[str] = Query(None, description="Start time filter (ISO format)"),
    endtime: Optional[str] = Query(None, description="End time filter (ISO format)"),
    valueSearch: Optional[str] = Query(None, description="Search value for order ID, user ID, or status"),
    status: Optional[str] = Query(None, description="Filter by order status"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    try:
        result = await filter_service.get_filtered_orders(
            page=page,
            limit=limit,
            start_time=starttime,
            end_time=endtime,
            search_value=valueSearch,
            status=status
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
    query: str = Query(..., description="Search query"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    filter_service: OrderFilterService = Depends(get_order_filter_service)
):
    try:
        result = await filter_service.search_orders(
            search_term=query,
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
    """
    Admin xác nhận đơn hàng
    Giải thích:
    - Admin bấm xác nhận đơn hàng
    - Status chuyển từ pending -> confirmed
    - Gửi notification cho user để thông báo đơn hàng đã được xác nhận
    """
    service = OrderService(order_repo)
    updated_order = await service.update_order_status(payload.order_id, payload.status)
    if not updated_order:
        raise HTTPException(status_code=400, detail="Cannot update order status")
    
    # Send notification to user
    # Giải thích: Gửi notification theo từng status thông qua notification_service
    status = payload.status.lower()
    try:
        user_id = updated_order.get('user_id')
        order_id = str(updated_order.get('id') or updated_order.get('_id'))
        total = updated_order.get('total', 0)
        
        if user_id:
            notif_service = get_notification_service()
            if status == 'confirmed':
                # Confirmed -> Notify user
                await notif_service.send_order_confirmation(
                    user_id=user_id,
                    order_id=order_id,
                    order_total=total
                )
            elif status == 'shipping':
                # Shipping -> Notify user đang giao
                await notif_service.send_order_shipping(
                    user_id=user_id,
                    order_id=order_id
                )
            elif status == 'complete':
                # Complete -> Đơn hàng hoàn thành
                await notif_service.send_order_complete(
                    user_id=user_id,
                    order_id=order_id
                )
    except Exception as e:
        print(f"Error sending notification to user: {e}")
    
    return JSONResponse(content=jsonable_encoder(updated_order), status_code=200)

@order_router.get("/{order_id}", response_model=OrderResponseSchema)
async def get_order_by_id(order_id: str, order_repo: OrderRepository = Depends(get_order_repo)):
    service = OrderService(order_repo)
    order = await order_repo.get_by_id(order_id)
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return JSONResponse(content=jsonable_encoder(order), status_code=200)
