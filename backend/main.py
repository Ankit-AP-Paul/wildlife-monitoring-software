from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.region import region

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
