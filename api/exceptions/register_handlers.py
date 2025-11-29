from fastapi import FastAPI
from typing import Callable, Type
import  inspect
from utils.logger import logger

register_handlers = []

def exception_handler(exc_class: Type[Exception]):
    def decorator(func: Callable):
        register_handlers.append((exc_class, func))
        return func
    return decorator

def register_all_handlers(app: FastAPI):
    logger.info("Đăng ký các handlers...")
    for exc_class, func in register_handlers:
        logger.info(f"Đăng ký handler cho {exc_class}")
        app.add_exception_handler(exc_class, func)