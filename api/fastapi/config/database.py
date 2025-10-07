import os
from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()
settings = get_settings()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.mongodb_url)
    db.database = db.client[settings.database_name]
    print("Connected to MongoDB")

async def close_mongo_connection():
    db.client.close()
    print("Disconnected from MongoDB")

def get_database():
    return db.database