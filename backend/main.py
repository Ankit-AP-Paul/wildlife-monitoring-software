from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.region import region
from routes.sensor import sensor
from routes.alert import alert
from routes.audio import audio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"message": "FastAPI is running"}

app.include_router(user)
app.include_router(region)
app.include_router(sensor)
app.include_router(alert)
app.include_router(audio)
