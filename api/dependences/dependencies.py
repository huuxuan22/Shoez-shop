# dependencies.py
from fastapi import Request
from config.context import lang_var
from fastapi import Depends

from repositories.cart_repository import CartRepository
from repositories.image_repository import ImageRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
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

async def get_user_repo():
    async with UserRepository(get_database()) as repo:
        yield repo

async def get_product_repo():
    async with ProductRepository(get_database()) as repo:
        yield repo

async def get_cart_repo():
    async with CartRepository(get_database()) as repo:
        yield repo

async def get_image_repo():
    yield ImageRepository()


