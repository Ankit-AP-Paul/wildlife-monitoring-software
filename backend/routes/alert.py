from fastapi import APIRouter, HTTPException
from bson import ObjectId

from models.alert import Alert
from schemas.alert import alertsEntity
from config.db import conn

alert = APIRouter(
    tags=["alert"]
)

@alert.post('/alert')
async def create_alert(alert: Alert):
    alert.sensor_id = ObjectId(alert.sensor_id)
    sensor = conn.technoverse.sensor.find_one({"_id": alert.sensor_id})
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor Not Found")
    conn.technoverse.alert.insert_one(dict(alert))
    return {"message" : "alert created successfully"}

@alert.get('/all_alerts')
async def get_all_alerts():
    alerts = conn.technoverse.alert.find()
    return alertsEntity(alerts)

@alert.get('/alert/{id}')
async def get_alert_by_sensor_id(id : str):
    id = ObjectId(id)
    sensor = conn.technoverse.sensor.find_one({"_id": id})
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor Not Found")
    alerts = conn.technoverse.alert.find({"sensor_id": id})
    return alertsEntity(alerts)