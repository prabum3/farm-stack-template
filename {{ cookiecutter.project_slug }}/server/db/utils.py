import logging

from motor.motor_asyncio import AsyncIOMotorClient
from settings.config import MONGODB_URL
from db.mongodb import db

log = logging.getLogger("uvicorn")

async def connect_to_mongo():
  log.info("Connecting to MongoDB...")
  db.client = AsyncIOMotorClient(str(MONGODB_URL))
  log.info("Successfully connected to MongoDB...")


async def close_mongo_connection():
  db.client.close()
  log.info("MongoDB Disconnected")
