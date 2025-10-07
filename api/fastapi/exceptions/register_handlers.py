from fastapi import FastAPI
from typing import Callable, Type
import  inspect

register_handlers = []

def exception_handler(exc_class: Type[Exception]):
    def decorator(func: Callable):
        register_handlers.append((exc_class, func))
        return func
    return decorator

def register_all_handlers(app: FastAPI):
    print("Đăng ký các handlers...")  # Thêm dòng này
    for exc_class, func in register_handlers:
        print(f"Đăng ký handler cho {exc_class}")  # Thêm dòng này
        app.add_exception_handler(exc_class, func)