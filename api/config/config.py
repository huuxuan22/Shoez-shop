from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field

class Settings(BaseSettings):
    debug: bool = Field(default=False, alias="DEBUG")
    minio_url: str = Field(..., alias="MINIO_URL")
    aws_access_key_id: str = Field(..., alias="MINIO_ACCESS_KEY")
    aws_secret_access_key: str = Field(..., alias="MINIO_SECRET_KEY")
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


@lru_cache
def get_settings() -> Settings:
    return Settings()