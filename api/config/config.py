from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field

class Settings(BaseSettings):
    debug: bool = Field(default=False, alias="DEBUG")
    minio_url: str = Field(..., alias="MINIO_URL")
    minio_access_key: str = Field(..., alias="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(..., alias="MINIO_SECRET_KEY")
    minio_bucket: str = Field(..., alias="MINIO_BUCKET")
    port_image: str = Field(..., alias="PORT_IMAGE")
    minio_secure: bool = False
    system_log_file : str = Field(..., alias="SYSTEM_LOG_FILE")
    api_prefix: str = Field(..., alias="API_PREFIX")
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = Field(..., alias="ALGORITHM")
    access_token_expire_seconds: int = Field(..., alias="ACCESS_TOKEN_EXPIRE_SECONDS")
    bucket_name: str = Field(..., alias="BUCKET_NAME")
    google_client_id: str = Field(..., alias="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(..., alias="GOOGLE_CLIENT_SECRET")
    frontend_url: str = Field(..., alias="FRONTEND_URL")
    backend_url: str = Field(..., alias="BACKEND_URL")
    server_metadata_url: str = Field(..., alias="GOOGLE_SERVER_METADATA_URL")
    google_scope: str = Field("openid email profile", alias="GOOGLE_SCOPE")
    google_access_type: str = Field("offline", alias="GOOGLE_ACCESS_TYPE")
    google_prompt: str = Field("consent", alias="GOOGLE_PROMPT")
    facebook_app_id: str = Field(..., alias="FACEBOOK_APP_ID")
    facebook_app_secret: str = Field(..., alias="FACEBOOK_APP_SECRET")
    mongodb_url: str = Field(..., alias="MONGODB_URL")
    database_name: str = Field(..., alias="DATABASE_NAME")
    redis_host: str = Field(..., alias="REDIS_HOST")
    redis_port: int = Field(..., alias="REDIS_PORT")
    redis_db: int = Field(..., alias="REDIS_DB")
    # SMTP Configuration
    smtp_host: str = Field(..., alias="SMTP_HOST")
    smtp_port: int = Field(..., alias="SMTP_PORT")
    smtp_username: str = Field(..., alias="SMTP_USERNAME")
    smtp_password: str = Field(..., alias="SMTP_PASSWORD")
    smtp_from_email: str = Field(..., alias="SMTP_FROM_EMAIL")
    smtp_use_tls: bool = Field(default=True, alias="SMTP_USE_TLS")
    # MoMo Payment Configuration
    momo_partner_code: Optional[str] = Field(default=None, alias="MOMO_PARTNER_CODE")
    momo_access_key: Optional[str] = Field(default=None, alias="MOMO_ACCESS_KEY")
    momo_secret_key: Optional[str] = Field(default=None, alias="MOMO_SECRET_KEY")
    momo_api_url: Optional[str] = Field(
        default="https://test-payment.momo.vn/v2/gateway/api/create",
        alias="MOMO_API_URL"
    )
    momo_ipn_url: Optional[str] = Field(default=None, alias="MOMO_IPN_URL")
    momo_redirect_url: Optional[str] = Field(default=None, alias="MOMO_REDIRECT_URL")
    momo_environment: str = Field(default="sandbox", alias="MOMO_ENVIRONMENT")
    momo_demo_mode: bool = Field(default=False, alias="MOMO_DEMO_MODE")
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def client_kwargs(self) -> dict:
        return {
            "scope": self.google_scope,
            "access_type": self.google_access_type,
            "prompt": self.google_prompt,
        }

    @property
    def backend_api_base(self) -> str:
        """
        Base URL for backend API endpoints, e.g. http://localhost:8000/api/v1
        """
        return f"{self.backend_url}"


@lru_cache
def get_settings() -> Settings:
    return Settings()