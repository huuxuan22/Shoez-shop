from typing import List, Dict, Any, Optional
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from utils.logger import logger
from repositories.review_repository import ReviewRepository
from schemas.review_schemas import ReviewCreateSchema, ReviewUpdateSchema
from bson import ObjectId


class ReviewService:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def _serialize_for_json(self, data: Any) -> Any:
        """Convert ObjectId và datetime để serialize thành JSON"""
        if isinstance(data, ObjectId):
            return str(data)
        elif isinstance(data, datetime):
            return data.isoformat()
        elif isinstance(data, dict):
            return {key: self._serialize_for_json(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self._serialize_for_json(item) for item in data]
        else:
            return data

    async def create_review(self, review_data: ReviewCreateSchema, user_id: str, user_name: str) -> Dict[str, Any]:
        """Tạo review mới (hoặc update nếu đã có)"""
        # Kiểm tra user đã review sản phẩm này trong đơn hàng này chưa
        existing_review = await self.review_repo.check_user_reviewed(
            user_id=user_id,
            product_id=review_data.product_id,
            order_id=review_data.order_id
        )
        
        # Nếu đã có review → Update thay vì tạo mới
        if existing_review:
            # Get review ID (có thể là str hoặc ObjectId)
            review_id = existing_review.get("id") or existing_review.get("_id")
            if not review_id:
                # Fallback: try to find by user_id, product_id, order_id
                reviews = await self.review_repo.get_all(skip=0, limit=1, filter_query={
                    "user_id": user_id,
                    "product_id": review_data.product_id,
                    "order_id": review_data.order_id
                })
                if reviews and len(reviews) > 0:
                    review_id = reviews[0].get("id") or reviews[0].get("_id")
            
            if review_id:
                # Update existing review
                update_dict = {
                    "rating": review_data.rating,
                    "comment": review_data.comment,
                    "updated_at": datetime.utcnow()
                }
                updated = await self.review_repo.update(review_id, update_dict)
                return updated

        # Tạo review mới
        review_dict = jsonable_encoder(review_data)
        review_dict["user_id"] = user_id
        review_dict["user_name"] = user_name
        review_dict["status"] = "approved"  # Tự động approve
        review_dict["helpful_count"] = 0
        review_dict["admin_comments"] = []
        
        # Đánh dấu cần chú ý nếu rating <= 3
        review_dict["needs_attention"] = review_data.rating <= 3
        
        review_dict["created_at"] = review_dict["updated_at"] = datetime.utcnow()

        # Chỉ lưu media do người dùng upload gửi từ FE trong review_data.images

        created_review = await self.review_repo.create(review_dict)
        
        # Nếu rating <= 3, gửi notification cho admin qua WebSocket
        if created_review.get("rating", 0) <= 3:
            await self._notify_admin_low_rating(created_review)
        
        return created_review
    
    async def _notify_admin_low_rating(self, review: Dict[str, Any]):
        """Lưu vào database và gửi notification cho admin khi có review thấp"""
        try:
            # 1. Lưu vào database (collection: low_rating_reviews)
            from services.low_rating_review_service import get_low_rating_review_service
            low_rating_service = get_low_rating_review_service()
            saved_review = await low_rating_service.create_low_rating_review(review)
            
            # 2. Gửi WebSocket notification
            from config.socket import get_sio
            sio = get_sio()
            notification_data = {
                "type": "low_rating_review",
                "review_id": str(review.get("id") or review.get("_id")),
                "product_id": review.get("product_id"),
                "user_name": review.get("user_name"),
                "rating": review.get("rating"),
                "comment": review.get("comment"),
                "message": f"Có review {review.get('rating')} sao từ {review.get('user_name') or 'Khách hàng'}",
                "timestamp": datetime.utcnow().isoformat()
            }
            
            await sio.emit('admin_notification', notification_data, room='admin', namespace='/notifications')
        except Exception as e:
            logger.error(f"Error notifying admin: {e}")
    async def get_reviews_by_product(self, product_id: str, page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """Lấy reviews theo product_id với pagination"""
        skip = (page - 1) * limit
        
        reviews = await self.review_repo.get_by_product(product_id, skip, limit)
        total = await self.review_repo.count_by_product(product_id)
        
        return {
            "reviews": self._serialize_for_json(reviews),
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": (total + limit - 1) // limit
        }

    async def get_reviews_by_user(self, user_id: str) -> List[Dict[str, Any]]:
        """Lấy tất cả reviews của user"""
        reviews = await self.review_repo.get_by_user(user_id)
        return self._serialize_for_json(reviews)

    async def get_reviews_by_order(self, order_id: str) -> List[Dict[str, Any]]:
        """Lấy reviews theo order_id"""
        reviews = await self.review_repo.get_by_order(order_id)
        return self._serialize_for_json(reviews)

    async def update_review(self, review_id: str, update_data: ReviewUpdateSchema, user_id: str) -> Dict[str, Any]:
        """Update review (chỉ user sở hữu mới được update)"""
        # Check ownership
        review = await self.review_repo.get_by_id(review_id)
        if not review:
            raise ValueError("Review not found")
        
        if review.get("user_id") != user_id:
            raise ValueError("Bạn không có quyền chỉnh sửa review này")

        update_dict = update_data.dict(exclude_unset=True)
        update_dict["updated_at"] = datetime.utcnow()

        updated_review = await self.review_repo.update(review_id, update_dict)
        return updated_review

    async def delete_review(self, review_id: str, user_id: str) -> bool:
        """Xóa review (chỉ user sở hữu mới được xóa)"""
        review = await self.review_repo.get_by_id(review_id)
        if not review:
            return False
        
        if review.get("user_id") != user_id:
            raise ValueError("Bạn không có quyền xóa review này")

        return await self.review_repo.delete(review_id)

    async def toggle_helpful(self, review_id: str, user_id: str, helpful: bool) -> Dict[str, Any]:
        """Toggle helpful cho review"""
        # TODO: Lưu user nào đã mark helpful để tránh spam
        increment = 1 if helpful else -1
        updated_review = await self.review_repo.update_helpful_count(review_id, increment)
        return updated_review

    async def get_pending_reviews_for_user(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Lấy danh sách sản phẩm chưa được đánh giá của user
        Returns: List of products cần đánh giá
        """
        from repositories.order_repository import OrderRepository
        from config.database import get_database
        
        order_repo = OrderRepository(get_database())
        
        # Lấy tất cả đơn hàng đã hoàn thành của user
        orders = await order_repo.get_by_user(user_id)
        complete_orders = [order for order in orders if order.get("status") == "complete"]
        
        pending_reviews = []
        
        for order in complete_orders:
            order_id = order.get("id") or order.get("_id")
            items = order.get("items", [])
            
            for item in items:
                product_id = item.get("productId") or item.get("_id")
                if not product_id:
                    continue
                
                # Check xem đã review chưa
                already_reviewed = await self.review_repo.check_user_reviewed(
                    user_id=user_id,
                    product_id=product_id,
                    order_id=str(order_id)
                )
                
                if not already_reviewed:
                    pending_reviews.append({
                        "order_id": order_id,
                        "product": item,
                        "created_at": order.get("created_at")
                    })
        
        return self._serialize_for_json(pending_reviews)

