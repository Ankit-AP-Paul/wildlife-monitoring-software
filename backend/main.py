from fastapi import FastAPI

from routes.user import user

app = FastAPI()

@app.get('/')
def index():
    return {"message": "FastAPI is running"}

app.include_router(user)