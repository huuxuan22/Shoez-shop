from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class MomoCreatePaymentRequest(BaseModel):
    """Request schema để tạo MoMo payment"""
    order_id: str = Field(..., description="ID đơn hàng")
    phone_number: Optional[str] = Field(None, description="Số điện thoại MoMo (nếu có)")
    return_url: Optional[str] = Field(None, description="URL redirect sau khi thanh toán")
    cancel_url: Optional[str] = Field(None, description="URL redirect khi hủy thanh toán")


class MomoCreatePaymentResponse(BaseModel):
    """Response schema khi tạo payment request thành công"""
    pay_url: str = Field(..., description="URL để redirect đến MoMo payment page")
    order_id: str = Field(..., description="ID đơn hàng")
    transaction_id: str = Field(..., description="MoMo transaction ID")
    request_id: str = Field(..., description="Request ID")


class MomoCallbackRequest(BaseModel):
    """Request schema từ MoMo callback (IPN)"""
    partnerCode: str
    partnerRefId: str
    partnerTransId: str
    amount: int
    transId: str
    resultCode: int
    message: str
    responseTime: int
    extraData: Optional[str] = None
    signature: str


class MomoQueryStatusRequest(BaseModel):
    """Request schema để query payment status"""
    order_id: str = Field(..., description="ID đơn hàng")


class PaymentStatusResponse(BaseModel):
    """Response schema cho payment status"""
    order_id: str
    payment_status: str  # pending, success, failed, processing
    transaction_id: Optional[str] = None
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    payment_time: Optional[str] = None
    message: Optional[str] = None


