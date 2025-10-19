from functools import wraps
from fastapi import  HTTPException, status
from config.context import current_user

def require_roles(*roles):
    """
    Decorator kiểm tra user có role hợp lệ hay không
    """
    def decorator(func):
        @wraps(func)   # 💡 Thêm dòng này để giữ nguyên thông tin hàm gốc
        async def wrapper(*args, **kwargs):
            user = current_user.get()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Unauthenticated"
                )

            user_role = user.get("role") if isinstance(user, dict) else getattr(user, "role", None)
            if user_role not in roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Permission denied"
                )

            return await func(*args, **kwargs)
        return wrapper
    return decorator
