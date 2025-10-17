from enum import Enum

class MessageKey(str, Enum):
    # General messages
    ERROR_SYSTEM = "error_system"
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    
    # Authentication
    LOGIN_SUCCESS = "login_success"
    LOGIN_FAILED = "login_failed"
    LOGOUT_SUCCESS = "logout_success"
    UNAUTHORIZED = "unauthorized"
    TOKEN_NOT_FOUND = "token_not_found"
    TOKEN_INVALID = "token_invalid"
    NOT_FOUND_USER_IN_TOKEN = "not_found_user_token"
    
    # User management
    USER_CREATED = "user_created"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    USER_EXIST = "user_exist"
    USER_NOT_FOUND = "user_not_found"
    USER_CREATE_SUCCESS = "user_success_created"

    # Product management
    PRODUCT_CREATED = "product_created"
    PRODUCT_UPDATED = "product_updated"
    PRODUCT_DELETED = "product_deleted"
    PRODUCT_NOT_FOUND = "product_not_found"
    
    # Order management
    ORDER_CREATED = "order_created"
    ORDER_UPDATED = "order_updated"
    ORDER_CANCELLED = "order_cancelled"
    ORDER_NOT_FOUND = "order_not_found"
    
    # Cart management
    CART_ITEM_ADDED = "cart_item_added"
    CART_ITEM_REMOVED = "cart_item_removed"
    CART_CLEARED = "cart_cleared"
    
    # File upload
    UPLOAD_SUCCESS = "upload_success"
    UPLOAD_FAILED = "upload_failed"
    INVALID_FILE_TYPE = "invalid_file_type"
    FILE_TOO_LARGE = "file_too_large"
    
    # Database
    DB_CONNECTION_SUCCESS = "db_connection_success"
    DB_CONNECTION_FAILED = "db_connection_failed"
    
    # MinIO/S3
    MINIO_CONNECTION_SUCCESS = "minio_connection_success"
    MINIO_CONNECTION_FAILED = "minio_connection_failed"
    
    # Validation errors
    VALIDATION_ERROR = "validation_error"
    REQUIRED_FIELD = "required_field"
    INVALID_EMAIL = "invalid_email"
    INVALID_PASSWORD = "invalid_password"
    
    # Log levels
    LOG_LEVEL_INFO = "log_level_info"
    LOG_LEVEL_WARNING = "log_level_warning"
    LOG_LEVEL_ERROR = "log_level_error"
    LOG_LEVEL_DEBUG = "log_level_debug"
    
    # Task status
    TASK_STATUS_TODO = "task_status_todo"
    TASK_STATUS_IN_PROGRESS = "task_status_in_progress"
    TASK_STATUS_COMPLETED = "task_status_completed"
    TASK_STATUS_CANCELLED = "task_status_cancelled"

class ErrorCode(int, Enum):
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503

class LanguageCode(str, Enum):
    ENGLISH = "en"
    VIETNAMESE = "vi"

class RoleEnum(str, Enum):
    ADMIN = 2 # Admin id sẽ là 2
    USER = 1 # user id sẽ là 1