"""
Exceptions package for handling application errors.

This package provides custom exception classes and handlers
for consistent error handling across the application.
"""

# Import main exception classes
try:
    from .exception import (
        ForbiddenException,
        UnauthorizedException,
        SystemException,
        AuthTokenMissingException,
        AuthException,
        AppException,
        UserExistException,
        UserNotFoundException
    )

    __all__ = [
        'ForbiddenException',
        'UnauthorizedException',
        'SystemException',
        'AuthTokenMissingException',
        'AuthException',
        'AppException',
        'UserExistException',
        'UserNotFoundException'
    ]
except ImportError:
    __all__ = []
