from fastapi import APIRouter, HTTPException
from bson import ObjectId

from models.region import Region
from schemas.region import regionsEntity, regionEntity
from config.db import conn

region = APIRouter(
    tags=["region"]
)

@region.post('/region')
async def create_region(region: Region):
    conn.technoverse.region.insert_one(dict(region))
    return region.dict()

@region.get('/all_region')
async def get_all_regions():
    regions = conn.technoverse.region.find()
    return regionsEntity(regions)

@region.get('/region/{id}')
async def get_region_by_id(id : str):
    id = ObjectId(id)
    region = conn.technoverse.region.find_one({"_id": id})
    if not region:
        raise HTTPException(status_code=404, detail="Region Not Found")
    return regionEntity(region)