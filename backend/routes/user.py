from fastapi import APIRouter, HTTPException
import hashlib

from models.user import User
from config.db import conn
from schemas.user import usersEntity, userEntity


user = APIRouter()

@user.post('/signup')
async def user_signup(user: User):
    user.password = hashlib.sha256(user.password.encode()).hexdigest()
    conn.technoverse.user.insert_one(dict(user))
    return usersEntity(conn.technoverse.user.find({"email": user.email}))[0]

@user.post('/signin')
async def user_login(email: str, password: str):
    password = hashlib.sha256(password.encode()).hexdigest()
    users = usersEntity(conn.technoverse.user.find({"email": email, "password": password}))
    if (len(users)==0):
        raise HTTPException(status_code=403, detail="Login Error")
    else:
        return users[0]