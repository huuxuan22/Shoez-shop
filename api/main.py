import os

from fastapi import Request
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware

from config.minio_client import minio_client
from controllers.auth_controller import auth_router
import boto3
from config.config import get_settings
import exceptions.handlers
from controllers.product_controller import product_router
from controllers.user_controller import user_router
from exceptions.register_handlers import register_all_handlers
from dependences.dependencies import set_language_dependency
from middleware.auth_middlewave import  AuthMiddlewave
from middleware.locale_middlewave import LocaleMiddlewave
from config.database import connect_to_mongo, close_mongo_connection, get_database

# Load environment variables
load_dotenv()
PRE_FIX = os.getenv("api_prefix")
# Create FastAPI app
# app = FastAPI(title="SHOEZ", version="1.0.0", dependencies=[Depends(set_language_dependency)])
app = FastAPI(
    title="My Shop API",
    docs_url="/docs",    # đường dẫn Swagger UI
    redoc_url="/redoc"   # đường dẫn ReDoc
)
settings = get_settings()
# Tạo bucket nếu chưa tồn tại
if not minio_client.bucket_exists(settings.minio_bucket):
    minio_client.make_bucket(settings.minio_bucket)

register_all_handlers(app)
# Include routers
app.include_router(auth_router, prefix=PRE_FIX)
app.include_router(product_router, prefix=PRE_FIX)
app.include_router(user_router, prefix=PRE_FIX)
setting = get_settings()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.add_middleware(AuthMiddlewave)
app.add_middleware(LocaleMiddlewave)
app.add_middleware(SessionMiddleware, secret_key=setting.secret_key)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = get_database()
    response = await call_next(request)
    return response

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup_event():
    print("Swagger UI: http://127.0.0.1:8000/docs")
    print("ReDoc: http://127.0.0.1:8000/redoc")
