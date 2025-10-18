"""
Script to hash existing plain text passwords in MongoDB
Run this once to migrate existing users' passwords
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config.config import get_settings
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def hash_existing_passwords():
    """Hash all plain text passwords in the users collection"""
    settings = get_settings()
    
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    collection = db['users']
    
    print("🔍 Checking users...")
    
    # Find all users
    users = await collection.find({}).to_list(length=None)
    
    if not users:
        print("❌ No users found!")
        return
    
    print(f"📝 Found {len(users)} users")
    
    updated_count = 0
    
    # Check and hash each user's password
    for user in users:
        password = user.get('password', '')
        
        # Check if password is already hashed (bcrypt hashes start with $2b$)
        if not password.startswith('$2b$'):
            # Hash the plain text password
            hashed_password = pwd_context.hash(password)
            
            # Update the user
            result = await collection.update_one(
                {"_id": user['_id']},
                {"$set": {"password": hashed_password}}
            )
            
            if result.modified_count > 0:
                print(f"✅ Hashed password for user: {user.get('email', 'Unknown')}")
                updated_count += 1
            else:
                print(f"⚠️  Failed to update user: {user.get('email', 'Unknown')}")
        else:
            print(f"⏭️  Password already hashed for user: {user.get('email', 'Unknown')}")
    
    print(f"\n🎉 Migration completed! Updated {updated_count}/{len(users)} users")

if __name__ == "__main__":
    asyncio.run(hash_existing_passwords())

