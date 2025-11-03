from fastapi import APIRouter, Depends, HTTPException, Request, Body
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Dict, Any
from schemas.payment_schemas import (
    MomoCreatePaymentRequest,
    MomoCreatePaymentResponse,
    MomoCallbackRequest,
    PaymentStatusResponse
)
from services.momo_payment_service import MomoPaymentService
from services.order_service import OrderService
from repositories.order_repository import OrderRepository
from config.database import get_database
from config.context import get_current_user
from utils.logger import logger
from fastapi.encoders import jsonable_encoder

payment_router = APIRouter(tags=["Payment"])


def get_momo_payment_service() -> MomoPaymentService:
    """Dependency injection cho MoMo Payment Service"""
    return MomoPaymentService()


def get_order_service() -> OrderService:
    """Dependency injection cho Order Service"""
    return OrderService(OrderRepository(get_database()))


@payment_router.post("/momo/create", response_model=MomoCreatePaymentResponse)
async def create_momo_payment(
    request_data: MomoCreatePaymentRequest,
    current_user: dict = Depends(get_current_user),
    momo_service: MomoPaymentService = Depends(get_momo_payment_service),
    order_service: OrderService = Depends(get_order_service)
):
    """
    Tạo MoMo payment request
    
    Flow:
    1. Verify order exists và belongs to user
    2. Check order status (chỉ cho phép tạo payment nếu pending)
    3. Create payment request đến MoMo
    4. Return payment URL để redirect
    """
    try:
        # Verify user owns the order
        user_id = str(current_user.get("_id") or current_user.get("id"))
        
        # Get order to verify
        order_id = request_data.order_id
        order_repo = OrderRepository(get_database())
        order = await order_repo.get_by_id(order_id)
        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        
        # Verify order belongs to user
        order_user_id = str(order.get("user_id"))
        if order_user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to access this order")
        
        # Check order status
        order_status = order.get("status", "pending")
        if order_status not in ["pending", "payment_pending"]:
            raise HTTPException(
                status_code=400,
                detail=f"Cannot create payment for order with status: {order_status}"
            )
        
        # Check payment method
        payment_method = order.get("paymentMethod", "")
        if payment_method != "momo":
            raise HTTPException(
                status_code=400,
                detail="Order payment method is not MoMo"
            )
        
        # Get order total
        order_total = order.get("total", 0)
        if order_total <= 0:
            raise HTTPException(status_code=400, detail="Invalid order total")
        
        # Create order info string
        items_count = len(order.get("items", []))
        order_info = f"Thanh toan don hang {order_id[:8]} - {items_count} san pham"
        
        # Create payment request
        payment_result = await momo_service.create_payment_request(
            order_id=order_id,
            amount=order_total,
            order_info=order_info,
            phone_number=request_data.phone_number,
            return_url=request_data.return_url,
            cancel_url=request_data.cancel_url
        )
        
        # Update order status to payment_pending
        await order_service.update_order_status(order_id, "payment_pending")
        
        # Store payment transaction info in order (optional)
        # Could add payment_transaction_id field to order model
        
        logger.info(f"MoMo payment created for order {order_id}: {payment_result.get('transaction_id')}")
        
        return JSONResponse(
            content=jsonable_encoder({
                "pay_url": payment_result["pay_url"],
                "order_id": order_id,
                "transaction_id": payment_result["transaction_id"],
                "request_id": payment_result["request_id"]
            }),
            status_code=200
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating MoMo payment: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create payment: {str(e)}")


@payment_router.post("/momo/callback")
async def momo_payment_callback(
    request: Request,
    callback_data: MomoCallbackRequest = Body(...),
    momo_service: MomoPaymentService = Depends(get_momo_payment_service),
    order_service: OrderService = Depends(get_order_service)
):
    """
    Xử lý callback từ MoMo (IPN - Instant Payment Notification)
    
    Flow:
    1. Verify signature
    2. Process callback data
    3. Update order status based on payment result
    4. Send notifications if needed
    """
    try:
        # Convert Pydantic model to dict
        callback_dict = callback_data.dict()
        
        logger.info(f"Received MoMo callback: {jsonable_encoder(callback_dict)}")
        
        # Process callback
        payment_result = await momo_service.process_callback(callback_dict)
        
        order_id = payment_result["order_id"]
        payment_status = payment_result["payment_status"]
        
        # Update order based on payment status
        if payment_status == "success":
            # Update order status to confirmed (payment successful)
            await order_service.update_order_status(order_id, "confirmed")
            
            # TODO: Update payment info in order document
            # Could add fields: payment_transaction_id, payment_status, payment_time
            
            logger.info(f"Order {order_id} payment successful")
            
        elif payment_status == "failed":
            # Keep order as pending or mark as payment_failed
            await order_service.update_order_status(order_id, "pending")
            
            logger.warning(f"Order {order_id} payment failed: {payment_result.get('message')}")
        
        # Return success response to MoMo
        # MoMo expects HTTP 200 status
        return JSONResponse(
            content={
                "status": "success",
                "message": "Callback processed"
            },
            status_code=200
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing MoMo callback: {str(e)}")
        # Still return 200 to MoMo to prevent retries
        return JSONResponse(
            content={
                "status": "error",
                "message": str(e)
            },
            status_code=200
        )


@payment_router.get("/momo/status/{order_id}", response_model=PaymentStatusResponse)
async def get_payment_status(
    order_id: str,
    current_user: dict = Depends(get_current_user),
    order_service: OrderService = Depends(get_order_service)
):
    """
    Lấy trạng thái thanh toán của đơn hàng
    """
    try:
        user_id = str(current_user.get("_id") or current_user.get("id"))
        
        # Get order
        order_repo = OrderRepository(get_database())
        order = await order_repo.get_by_id(order_id)
        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        
        # Verify ownership
        order_user_id = str(order.get("user_id"))
        if order_user_id != user_id:
            raise HTTPException(status_code=403, detail="Access denied")
        
        # Determine payment status from order status
        order_status = order.get("status", "pending")
        payment_status = "pending"
        
        if order_status == "payment_pending":
            payment_status = "processing"
        elif order_status == "confirmed":
            payment_status = "success"
        elif order_status in ["cancelled", "failed"]:
            payment_status = "failed"
        
        return JSONResponse(
            content=jsonable_encoder({
                "order_id": order_id,
                "payment_status": payment_status,
                "transaction_id": order.get("payment_transaction_id"),
                "amount": order.get("total"),
                "payment_method": order.get("paymentMethod"),
                "payment_time": order.get("payment_time"),
                "message": None
            }),
            status_code=200
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting payment status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


