import hashlib
import hmac
import json
import time
import uuid
from typing import Dict, Any, Optional
import httpx
from fastapi import HTTPException
from config.config import get_settings
from utils.logger import logger

settings = get_settings()


class MomoPaymentService:
    """
    Service xử lý thanh toán MoMo Payment Gateway
    
    Flow:
    1. create_payment_request() - Tạo payment request và nhận pay_url
    2. MoMo redirect user đến pay_url
    3. User thanh toán trên MoMo
    4. MoMo gọi callback (IPN) đến callback_url
    5. verify_callback() - Verify signature và xử lý callback
    """
    
    def __init__(self):
        self.partner_code = getattr(settings, 'MOMO_PARTNER_CODE', None)
        self.access_key = getattr(settings, 'MOMO_ACCESS_KEY', None)
        self.secret_key = getattr(settings, 'MOMO_SECRET_KEY', None)
        self.api_url = getattr(settings, 'MOMO_API_URL', 'https://test-payment.momo.vn/v2/gateway/api/create')
        self.ipn_url = getattr(settings, 'MOMO_IPN_URL', None)
        self.redirect_url = getattr(settings, 'MOMO_REDIRECT_URL', None)
        
        if not all([self.partner_code, self.access_key, self.secret_key]):
            logger.warning("MoMo payment credentials not configured. Payment features will not work.")
    
    def _generate_request_id(self) -> str:
        """Generate unique request ID"""
        return str(int(time.time() * 1000))
    
    def _create_signature(self, raw_data: str) -> str:
        """
        Tạo signature cho MoMo payment request
        
        Algorithm:
        - Tạo raw string từ các fields
        - HMAC SHA256 với secret key
        """
        return hmac.new(
            self.secret_key.encode('utf-8'),
            raw_data.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
    
    def _create_raw_signature_string(
        self,
        partner_code: str,
        partner_ref_id: str,
        amount: int,
        partner_trans_id: str
    ) -> str:
        """
        Tạo raw string để sign theo format MoMo yêu cầu
        
        Format: partnerCode=$partnerCode&partnerRefId=$partnerRefId&partnerTransId=$partnerTransId&amount=$amount
        """
        return f"partnerCode={partner_code}&partnerRefId={partner_ref_id}&partnerTransId={partner_trans_id}&amount={amount}"
    
    async def create_payment_request(
        self,
        order_id: str,
        amount: float,
        order_info: str = "Thanh toan don hang",
        phone_number: Optional[str] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Tạo payment request đến MoMo Gateway
        
        Args:
            order_id: ID đơn hàng
            amount: Số tiền (VND)
            order_info: Thông tin đơn hàng
            phone_number: Số điện thoại MoMo (optional)
            return_url: URL redirect sau khi thanh toán thành công
            cancel_url: URL redirect khi hủy thanh toán
        
        Returns:
            Dict chứa pay_url và transaction info
        """
        if not all([self.partner_code, self.access_key, self.secret_key]):
            raise HTTPException(
                status_code=500,
                detail="MoMo payment configuration is missing. Please contact administrator."
            )
        
        # Generate unique IDs
        partner_ref_id = order_id
        partner_trans_id = f"ORDER_{order_id}_{int(time.time())}"
        request_id = self._generate_request_id()
        
        # Convert amount to int (MoMo requires integer)
        amount_int = int(amount)
        
        # Create signature
        raw_signature = self._create_raw_signature_string(
            partner_code=self.partner_code,
            partner_ref_id=partner_ref_id,
            amount=amount_int,
            partner_trans_id=partner_trans_id
        )
        signature = self._create_signature(raw_signature)
        
        # Prepare request data
        request_data = {
            "partnerCode": self.partner_code,
            "partnerName": "Shoez Shop",
            "partnerRefId": partner_ref_id,
            "partnerTransId": partner_trans_id,
            "requestId": request_id,
            "amount": amount_int,
            "requestType": "captureWallet",  # Loại thanh toán: ví MoMo
            "orderId": partner_trans_id,
            "orderInfo": order_info,
            "redirectUrl": return_url or self.redirect_url or f"{settings.frontend_url}/payment/success",
            "ipnUrl": self.ipn_url or f"{settings.backend_url}/api/v1/payments/momo/callback",
            "extraData": "",  # Base64 encoded, empty for now
            "lang": "vi",
            "signature": signature
        }
        
        # Add phone number if provided
        if phone_number:
            request_data["userInfo"] = {
                "phoneNumber": phone_number
            }
        
        try:
            # Send request to MoMo API
            logger.info(f"Creating MoMo payment request for order {order_id}")
            logger.debug(f"Request data: {json.dumps(request_data, indent=2)}")
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.api_url,
                    json=request_data,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.access_key}"
                    }
                )
                response.raise_for_status()
                result = response.json()
            
            logger.info(f"MoMo payment response: {json.dumps(result, indent=2)}")
            
            # Verify response
            if result.get("resultCode") != 0:
                error_message = result.get("message", "Unknown error")
                logger.error(f"MoMo payment creation failed: {error_message}")
                raise HTTPException(
                    status_code=400,
                    detail=f"MoMo payment error: {error_message}"
                )
            
            # Return payment URL
            pay_url = result.get("payUrl")
            if not pay_url:
                raise HTTPException(
                    status_code=500,
                    detail="MoMo did not return payment URL"
                )
            
            return {
                "pay_url": pay_url,
                "order_id": order_id,
                "transaction_id": partner_trans_id,
                "request_id": request_id,
                "partner_ref_id": partner_ref_id
            }
            
        except httpx.HTTPError as e:
            logger.error(f"Error calling MoMo API: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to create MoMo payment: {str(e)}"
            )
        except Exception as e:
            logger.error(f"Unexpected error in create_payment_request: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected error: {str(e)}"
            )
    
    def verify_callback_signature(self, callback_data: Dict[str, Any]) -> bool:
        """
        Verify signature từ MoMo callback
        
        Args:
            callback_data: Data từ MoMo callback
        
        Returns:
            True nếu signature hợp lệ, False nếu không
        """
        try:
            # Extract required fields
            partner_code = callback_data.get("partnerCode")
            partner_ref_id = callback_data.get("partnerRefId")
            partner_trans_id = callback_data.get("partnerTransId")
            amount = callback_data.get("amount")
            received_signature = callback_data.get("signature")
            
            if not all([partner_code, partner_ref_id, partner_trans_id, amount, received_signature]):
                logger.warning("Missing required fields in MoMo callback")
                return False
            
            # Create signature to compare
            raw_signature = self._create_raw_signature_string(
                partner_code=partner_code,
                partner_ref_id=partner_ref_id,
                amount=int(amount),
                partner_trans_id=partner_trans_id
            )
            expected_signature = self._create_signature(raw_signature)
            
            # Compare signatures (case-insensitive)
            is_valid = expected_signature.lower() == received_signature.lower()
            
            if not is_valid:
                logger.warning(f"Invalid MoMo callback signature. Expected: {expected_signature}, Received: {received_signature}")
            
            return is_valid
            
        except Exception as e:
            logger.error(f"Error verifying MoMo callback signature: {str(e)}")
            return False
    
    async def process_callback(self, callback_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Xử lý callback từ MoMo (IPN)
        
        Args:
            callback_data: Data từ MoMo callback
        
        Returns:
            Dict chứa thông tin payment result
        """
        # Verify signature first
        if not self.verify_callback_signature(callback_data):
            raise HTTPException(
                status_code=400,
                detail="Invalid signature"
            )
        
        # Extract payment info
        result_code = callback_data.get("resultCode")
        partner_ref_id = callback_data.get("partnerRefId")  # Order ID
        partner_trans_id = callback_data.get("partnerTransId")
        amount = callback_data.get("amount")
        trans_id = callback_data.get("transId")  # MoMo transaction ID
        message = callback_data.get("message", "")
        
        # Determine payment status
        if result_code == 0:
            payment_status = "success"
        elif result_code == 1000:
            payment_status = "pending"
        elif result_code == 1001:
            payment_status = "processing"
        else:
            payment_status = "failed"
        
        return {
            "order_id": partner_ref_id,
            "payment_status": payment_status,
            "transaction_id": trans_id,
            "partner_trans_id": partner_trans_id,
            "amount": amount / 100 if amount else None,  # MoMo returns amount in cents
            "result_code": result_code,
            "message": message
        }
    
    async def query_payment_status(self, order_id: str) -> Dict[str, Any]:
        """
        Query payment status từ MoMo (nếu cần)
        
        Note: MoMo sẽ tự động gọi IPN callback, nhưng có thể query thủ công nếu cần
        """
        # Implementation depends on MoMo API for query
        # For now, return basic info
        return {
            "order_id": order_id,
            "status": "pending"  # Will be updated by callback
        }

