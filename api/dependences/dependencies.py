# dependencies.py
from fastapi import Request, Depends
from config.context import lang_var
from passlib.context import CryptContext
from repositories.cart_repository import CartRepository
from repositories.image_repository import ImageRepository
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from repositories.comment_repository import CommentRepository
from repositories.notification_repository import NotificationRepository
from repositories.category_repository import CategoryRepository
from repositories.brand_repository import BrandRepository
from config.database import get_database

async def set_language_dependency(request: Request):
    lang = request.headers.get("Accept-language")
    if lang is None:
        lang = 'vi'
    lang = lang.split(",")[0].lower()
    if lang not in ("en", "vi"):
        lang = "en"
    lang_var.set(lang)
    return lang

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_repo():
    async with UserRepository(get_database()) as repo:
        yield repo

async def get_product_repo():
    async with ProductRepository(get_database()) as repo:
        yield repo

async def get_cart_repo():
    async with CartRepository(get_database()) as repo:
        yield repo

async def get_order_repo():
    async with OrderRepository(get_database()) as repo:
        yield repo

async def get_image_repo():
    yield ImageRepository()

async def get_comment_repo():
    async with CommentRepository(get_database()) as repo:
        yield repo

async def get_notification_repo():
    async with NotificationRepository(get_database()) as repo:
        yield repo

async def get_category_repo():
    async with CategoryRepository(get_database()) as repo:
        yield repo

async def get_brand_repo():
    async with BrandRepository(get_database()) as repo:
        yield repo


