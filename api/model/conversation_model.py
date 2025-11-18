from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

from model.mongodb_base_model import BaseMongoModel, PyObjectId


class Participant(BaseModel):
    userId: str
    role: str  


class LastMessage(BaseModel):
    content: str
    senderId: str
    createdAt: datetime


class Conversation(BaseMongoModel):
    participants: List[Participant] = []
    lastMessage: Optional[LastMessage] = None
    unread: Dict[str, int] = Field(default_factory=dict)  
    updatedAt: Optional[datetime] = None

    class Config:
        json_encoders = {
            ObjectId: lambda v: str(v),
            datetime: lambda v: v.isoformat() if v else None
        }

