from fastapi import APIRouter, HTTPException, File, UploadFile
from bson import ObjectId
import os

from config.db import conn

audio = APIRouter(tags=["audio"])

DOWNLOAD_FOLDER = "audio"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@audio.post('/audio')
async def upload_audio(sensor_id: str, file: UploadFile = File(...)):
    sensor_id = ObjectId(sensor_id)
    sensor = conn.technoverse.sensor.find_one({"_id": sensor_id})
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor Not Found")
    content = await file.read()
    conn.technoverse.audio.insert_one({
        "sensor_id": sensor_id,
        "filename": file.filename,
        "content": content
    })
    return {"message": "audio uploaded successfully"}

@audio.get('/audio/{sensor_id}')
async def get_audio(sensor_id: str):
    sensor_id = ObjectId(sensor_id)
    sensor = conn.technoverse.sensor.find_one({"_id": sensor_id})
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor Not Found")
    audios = conn.technoverse.audio.find({"sensor_id": sensor_id})
    if not audios:
        raise HTTPException(status_code=404, detail="Audio Not Found")
    for audio in audios:
        file_path = os.path.join(DOWNLOAD_FOLDER, audio["filename"])
        with open(file_path, "wb") as f:
            f.write(audio["content"])
    return {"message": "audio downloaded successfully"}
