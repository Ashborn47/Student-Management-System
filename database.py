from motor.motor_asyncio import AsyncIOMotorClient
from config import get_settings

settings = get_settings()

async def get_database():
    client = AsyncIOMotorClient(settings.mongodb_url)
    return client[settings.database_name]

async def get_student_collection():
    db = await get_database()
    return db.students