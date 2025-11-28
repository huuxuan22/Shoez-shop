import os

from fastapi import Request
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware

from config.minio_client import minio_client
from controllers.auth_controller import auth_router
from config.config import get_settings
from controllers.cart_controller import cart_router
from controllers.order_controller import order_router
from controllers.product_controller import product_router
from controllers.user_controller import user_router
from controllers.notification_controller import notification_router
from controllers.review_controller import review_router
from controllers.low_rating_review_controller import low_rating_review_router
from controllers.favourite_product_controller import router as favourite_router
from controllers.category_controller import category_router
from controllers.payment_controller import payment_router
from controllers.brand_controller import brand_router
from controllers.statistics_controller import statistics_router
from controllers.conversation_controller import conversation_router
from controllers.message_controller import message_router
from exceptions.register_handlers import register_all_handlers
import exceptions.handlers 
from dependences.dependencies import set_language_dependency
from middleware.auth_middlewave import  AuthMiddlewave
from middleware.locale_middlewave import LocaleMiddlewave
from config.database import connect_to_mongo, close_mongo_connection, get_database
from config.socket import socket_app as socket_io_app
from utils.logger import logger
import uvicorn

load_dotenv()
settings = get_settings()
PRE_FIX = settings.api_prefix
app = FastAPI(
    title="My Shop API",
    docs_url="/docs",    
    redoc_url="/redoc"   
)
if not minio_client.bucket_exists(settings.minio_bucket):
    minio_client.make_bucket(settings.minio_bucket)

register_all_handlers(app)
app.include_router(auth_router, prefix=PRE_FIX)
app.include_router(product_router, prefix=PRE_FIX)
app.include_router(order_router, prefix=PRE_FIX)
app.include_router(cart_router, prefix=PRE_FIX)
app.include_router(user_router, prefix=PRE_FIX)
app.include_router(notification_router, prefix=PRE_FIX)
app.include_router(review_router, prefix=PRE_FIX)
app.include_router(low_rating_review_router, prefix=PRE_FIX)
app.include_router(favourite_router, prefix=PRE_FIX)
app.include_router(category_router, prefix=PRE_FIX)
app.include_router(payment_router, prefix=f"{PRE_FIX}/payments")
app.include_router(brand_router, prefix=PRE_FIX)
app.include_router(statistics_router, prefix=PRE_FIX)
app.include_router(conversation_router, prefix=PRE_FIX)
app.include_router(message_router, prefix=PRE_FIX)
@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    # Show SHOEZ banner
    logger.show_banner()
    
    # Connect to database
    logger.info("🔌 Connecting to database...")
    await connect_to_mongo()
    logger.success("Database connected successfully!")
    
    # Check MinIO connection
    try:
        logger.minio_connected(f"MinIO at {settings.minio_bucket}")
    except Exception as e:
        logger.minio_error(str(e))
    
    # Show API documentation URLs
    print("\n" + "="*70)
    print("📚 API Documentation:")
    print(f"   Swagger UI: http://127.0.0.1:8000/docs")
    print(f"   ReDoc:     http://127.0.0.1:8000/redoc")
    print("="*70 + "\n")

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler"""
    logger.info("🛑 Shutting down server...")
    await close_mongo_connection()
    logger.success("Server stopped gracefully!")
app.add_middleware(AuthMiddlewave)
app.add_middleware(LocaleMiddlewave)
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = get_database()
    response = await call_next(request)
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/socket.io", socket_io_app)

# Simple health check
@app.get(f"{PRE_FIX}/health")
async def health_check():
    return {"status": "ok"}
