from pydantic import BaseModel
from datetime import datetime


class Alert(BaseModel):
    sensor_id: str
    description: str
    date: datetime
    actions: str
