import os
from bson import CodecOptions, UuidRepresentation
from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()
settings = get_settings()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.mongodb_url)
    codec_options = CodecOptions(
        uuid_representation=UuidRepresentation.STANDARD
    )

    db.database = db.client.get_database(
        settings.database_name,
        codec_options=codec_options
    )

async def close_mongo_connection():
    if db.client:
        db.client.close()

def get_database():
    return db.database
