from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
import uuid
import pytz

tz = pytz.timezone("Asia/Ho_Chi_Minh")

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return {"type": "string", "format": "objectid"}


class BaseMongoModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")  # _id MongoDB
    uuid: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime = Field(default_factory=lambda: datetime.now(tz))
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    is_deleted: bool = False

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
        "populate_by_name": True
    }
