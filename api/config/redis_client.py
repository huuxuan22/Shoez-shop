import redis
from config.config import get_settings
from typing import Optional

settings = get_settings()

class RedisClient:
    """Redis client wrapper để quản lý kết nối Redis"""
    
    def __init__(self):
        self._client: Optional[redis.Redis] = None
        self._is_available = False
        
    def connect(self):
        """Kết nối đến Redis server"""
        try:
            self._client = redis.Redis(
                host=settings.redis_host,
                port=settings.redis_port,
                db=settings.redis_db,
                decode_responses=True,
                socket_connect_timeout=5
            )
            # Test connection
            self._client.ping()
            self._is_available = True
            return True
        except Exception as e:
            print(f"Warning: Redis connection failed: {e}")
            self._client = None
            self._is_available = False
            return False
    
    @property
    def client(self) -> Optional[redis.Redis]:
        """Lấy Redis client, tự động kết nối nếu chưa kết nối"""
        if self._client is None:
            self.connect()
        return self._client
    
    @property
    def is_available(self) -> bool:
        """Kiểm tra Redis có sẵn sàng không"""
        if self._client is None:
            self.connect()
        return self._is_available
    
    def set_email_verification_code(self, email: str, code: str, expire_seconds: int = 900) -> bool:
        """
        Lưu mã xác thực email vào Redis
        
        Args:
            email: Email của người dùng (dùng làm key)
            code: Mã xác thực đã được hash
            expire_seconds: Thời gian hết hạn (mặc định 15 phút = 900 giây)
            
        Returns:
            bool: True nếu lưu thành công, False nếu có lỗi
        """
        if not self.is_available or not self._client:
            return False
        
        try:
            key = f"email_verification:{email}"
            self._client.set(key, code, ex=expire_seconds)
            return True
        except Exception as e:
            print(f"Error setting verification code in Redis: {e}")
            return False
    
    def get_email_verification_code(self, email: str) -> Optional[str]:
        """
        Lấy mã xác thực email từ Redis
        
        Args:
            email: Email của người dùng
            
        Returns:
            str: Mã xác thực đã hash hoặc None nếu không tìm thấy
        """
        if not self.is_available or not self._client:
            return None
        
        try:
            key = f"email_verification:{email}"
            return self._client.get(key)
        except Exception as e:
            print(f"Error getting verification code from Redis: {e}")
            return None
    
    def delete_email_verification_code(self, email: str) -> bool:
        """
        Xóa mã xác thực email khỏi Redis sau khi xác thực thành công
        
        Args:
            email: Email của người dùng
            
        Returns:
            bool: True nếu xóa thành công
        """
        if not self.is_available or not self._client:
            return False
        
        try:
            key = f"email_verification:{email}"
            self._client.delete(key)
            return True
        except Exception as e:
            print(f"Error deleting verification code from Redis: {e}")
            return False

# Singleton instance
redis_client = RedisClient()

