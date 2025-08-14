from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv

load_dotenv()  

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
mongo_db_name = os.getenv("MONGO_DB_NAME")

if not mongo_db_name:
	raise ValueError("Environment variable MONGO_DB_NAME is not set.")

db = client[mongo_db_name]
