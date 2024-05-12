# pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI(title="FastAPI kirish")


@app.get('/')
async def root():
    return {"message": "Hello FastAPI"}


@app.get('api/v1/posts/')
async def posts():
    data = {
        "title": "post1",
        "description": "hello fastapi"
    }
    return data.__dict__
