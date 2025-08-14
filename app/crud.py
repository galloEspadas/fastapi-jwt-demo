from .database import db
from . import utils

async def create_user(username: str, password: str):
    hashed_password = utils.hash_password(password)
    await db.users.insert_one({"username": username, "password_hash": hashed_password})
    return {"username": username}

async def get_user_by_username(username: str):
    return await db.users.find_one({"username": username})

async def get_all_usernames():
    users = await db.users.find({}, {"_id": 0, "username": 1}).to_list(length=None)
    return [u["username"] for u in users]