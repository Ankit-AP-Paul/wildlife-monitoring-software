from pydantic import BaseModel
from datetime import datetime

class Sensor(BaseModel):
    name: str
    latitude: float
    longitude: float
    region_id: str
    radius: float
    deployment_date: datetime
    status: str
    