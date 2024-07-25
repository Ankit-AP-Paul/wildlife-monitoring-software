from fastapi import APIRouter, HTTPException
from bson import ObjectId

from models.sensor import Sensor
from schemas.sensor import sensorsEntity, sensorEntity
from config.db import conn

sensor = APIRouter(
    tags=["sensor"]
)

@sensor.post('/sensor')
async def create_sensor(sensor: Sensor):
    sensor.region_id = ObjectId(sensor.region_id)
    region = conn.technoverse.region.find_one({"_id": sensor.region_id})
    if not region:
        raise HTTPException(status_code=404, detail="Region Not Found")
    conn.technoverse.sensor.insert_one(dict(sensor))
    return { "message" : "Sensor saved successfully" }

@sensor.get('/all_sensor')
async def get_all_sensors():
    sensors = conn.technoverse.sensor.find()
    return sensorsEntity(sensors)

@sensor.get('/sensor/{id}')
async def get_sensor_by_id(id : str):
    id = ObjectId(id)
    sensor = conn.technoverse.sensor.find_one({"_id": id})
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor Not Found")
    return sensorEntity(sensor)