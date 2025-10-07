from i18n.translator import MessageKey
from typing import Union
from fastapi import HTTPException, status

class SystemException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class UnauthorizedException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class ForbiddenException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class AuthTokenMissingException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class AuthException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class AppException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class UserExistException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

class UserNotFoundException(Exception):
    def __init__(self, message: Union [MessageKey, str]):
        self.message = message

USER_NOT_FOUND_EXCEPTION = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")