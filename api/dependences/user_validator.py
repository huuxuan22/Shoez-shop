
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from config.enum import MessageKey
from exceptions.exception import UserExistException
from schemas.auth_schemas import UserCreate
from model.user_model import User

def validate_unique_user(user: UserCreate, db: Session = Depends()):
    if db.query(User).filter(User.email == user.email).first():
        raise UserExistException(MessageKey.USER_EXIST)
    if db.query(User).filter(User.numberphone == user.numberphone).first():
        raise UserExistException(MessageKey.USER_EXIST)
    return user
