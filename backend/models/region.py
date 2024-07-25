from pydantic import BaseModel

class Region(BaseModel):
    name : str
    description : str
    wildlife : list
    birds : list