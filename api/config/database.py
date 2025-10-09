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
    # 1. Tạo client MongoDB (không truyền codec_options ở đây)
    db.client = AsyncIOMotorClient(settings.mongodb_url)

    # 2. Định nghĩa codec_options (áp dụng ở cấp database)
    codec_options = CodecOptions(
        uuid_representation=UuidRepresentation.STANDARD
    )

    # 3. Lấy database và áp dụng codec_options tại đây ✅
    db.database = db.client.get_database(
        settings.database_name,
        codec_options=codec_options
    )

    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    if db.client:
        db.client.close()
        print("🛑 Disconnected from MongoDB")

def get_database():
    return db.database
