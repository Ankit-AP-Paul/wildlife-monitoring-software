from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name : str
    email : str
    password : str
    phone_no : int
    gov_body : str
    region_id : str
    created_at : datetime = datetime.now()
    
