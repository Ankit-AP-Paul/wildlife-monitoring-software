from fastapi import APIRouter

from models.region import Region
from schemas.region import regionsEntity
from config.db import conn

region = APIRouter()

@region.post('/region')
async def create_region(region: Region):
    conn.technoverse.region.insert_one(dict(region))
    return region.dict()

@region.get('/region')
async def get_regions():
    regions = conn.technoverse.region.find()
    return regionsEntity(regions)