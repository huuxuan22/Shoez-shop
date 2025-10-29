from typing import List, Dict, Any, Optional
from datetime import datetime
from config.socket import get_sio
from repositories.notification_repository import NotificationRepository
from config.database import get_database


class NotificationService:
    def __init__(self):
        self.sio = get_sio()
        self._repository = None
    
    @property
    def repository(self):
        """Lazy load repository khi cần dùng"""
        if self._repository is None:
            self._repository = NotificationRepository(get_database())
        return self._repository
    
    async def send_notification_to_user(
        self, 
        user_id: str, 
        notification_data: Dict[str, Any]
    ):
        """
        Gửi notification đến user (WebSocket + Database)
        - user_id: ID của user cần gửi
        - notification_data: Dữ liệu notification
        """
        room = f'user_{user_id}'
        
        # 1. Save to database
        await self.repository.create_notification(
            user_id=user_id,
            order_id=notification_data.get('order_id'),
            title=notification_data.get('title'),
            message=notification_data.get('message'),
            type=notification_data.get('type'),
            metadata=notification_data
        )
        
        # 2. Emit via WebSocket
        await self.sio.emit('notification', notification_data, room=room, namespace='/notifications')
        print(f'📬 Notification sent to user {user_id}: {notification_data}')
    
    async def send_order_confirmation(
        self, 
        user_id: str, 
        order_id: str, 
        order_total: float
    ):
        """
        Gửi notification xác nhận đơn hàng
        """
        notification = {
            'type': 'order_confirmed',
            'order_id': order_id,
            'message': f'Đơn hàng #{order_id} đã được xác nhận',
            'title': 'Đơn hàng của bạn đã được xác nhận',
            'total': order_total,
            'timestamp': datetime.utcnow().isoformat()
        }
        await self.send_notification_to_user(user_id, notification)
    
    async def send_order_placed_notification(
        self,
        user_id: str,
        order_id: str,
        order_total: float
    ):
        """
        Gửi notification khi user đặt hàng thành công
        """
        notification = {
            'type': 'order_placed',
            'order_id': order_id,
            'message': f'Cảm ơn bạn đã đặt hàng #{order_id}',
            'title': 'Đặt hàng thành công',
            'total': order_total,
            'timestamp': datetime.utcnow().isoformat()
        }
        await self.send_notification_to_user(user_id, notification)
    
    async def send_new_order_notification_to_admin(
        self,
        order_id: str,
        customer_name: str,
        order_total: float
    ):
        """
        Gửi notification cho admin khi có order mới
        - Chỉ emit WebSocket, không lưu vào DB (admin không cần lưu)
        """
        notification = {
            'type': 'new_order',
            'order_id': order_id,
            'message': f'Đơn hàng mới #{order_id} từ {customer_name}',
            'title': 'Đơn hàng mới',
            'total': order_total,
            'timestamp': datetime.utcnow().isoformat()
        }
        await self.sio.emit('notification', notification, room='admin', namespace='/notifications')
        print(f'📬 New order notification sent to admin: Order #{order_id}')
    
    async def send_order_shipping(
        self,
        user_id: str,
        order_id: str
    ):
        """
        Gửi notification khi đơn hàng đang giao (WebSocket + Database)
        """
        notification = {
            'type': 'order_shipping',
            'order_id': order_id,
            'message': f'Đơn hàng #{order_id} đang được giao',
            'title': 'Đơn hàng đang giao',
            'timestamp': datetime.utcnow().isoformat()
        }
        await self.send_notification_to_user(user_id, notification)
    
    async def send_order_complete(
        self,
        user_id: str,
        order_id: str
    ):
        """
        Gửi notification khi đơn hàng hoàn thành (WebSocket + Database)
        """
        notification = {
            'type': 'order_complete',
            'order_id': order_id,
            'message': f'Đơn hàng #{order_id} đã hoàn thành',
            'title': 'Đơn hàng hoàn thành',
            'timestamp': datetime.utcnow().isoformat()
        }
        await self.send_notification_to_user(user_id, notification)

notification_service = NotificationService()
