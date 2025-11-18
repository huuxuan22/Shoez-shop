from typing import Optional
from pydantic import Field
from datetime import datetime
from bson import ObjectId

from model.mongodb_base_model import BaseMongoModel, PyObjectId


class Message(BaseMongoModel):
    conversationId: PyObjectId
    senderId: str
    receiverId: str
    content: str
    type: str = "text"  # "text", "image", "file" for future expansion
    createdAt: Optional[datetime] = None
    isRead: bool = False

    class Config:
        json_encoders = {
            ObjectId: lambda v: str(v),
            datetime: lambda v: v.isoformat() if v else None
        }

