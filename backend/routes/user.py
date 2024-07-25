from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
import hashlib

from models.user import User
from config.db import conn
from schemas.user import usersEntity
from schemas.region import regionsEntity


user = APIRouter()

@user.post('/signup')
async def user_signup(user: User):
    if(len(usersEntity(conn.technoverse.user.find({"email": user.email})))>0):
        raise HTTPException(status_code=403, detail="Email Already Exists")
    user.region_id = ObjectId(user.region_id)
    region = conn.technoverse.region.find_one({"_id": user.region_id})
    if not region:
        raise HTTPException(status_code=404, detail="Region Not Found")
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