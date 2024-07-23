from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.post('/user')
async def create_user(user: User):
    conn.technoverse.user.insert_one(dict(user))
    return {"message": "User created"}

@user.get('/user')
async def get_users():
    return usersEntity(conn.technoverse.user.find())