from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Crud API", description="CRUD with FastAPI", version="1")

database = []


class Post:
    def __init__(self, title: str, description: str = None, author: str = None):
        self.title = title
        self.description = description
        self.author = author
        self.created_at = datetime.now()


@app.post("/posts/")
async def create_post(title: str, description: str = None, author: str = None):
    post = Post(title, description, author)
    database.append(post)
    return {"data": post.__dict__, "message": "Post created successfully"}


@app.get("/get-posts/")
async def get_posts():
    return database


@app.put("/posts/{id}")
async def update_post(post_id: int, title: str, description: str, author: str = None):
    database[post_id] = Post(title, description, author)
    return {"post_id": post_id, "message": "Post updated successfully"}


@app.delete("/posts/{id}")
async def delete_post(post_id: int):
    deleted_post = database.pop(post_id)
    return {"post_id": post_id, "deleted_podt": deleted_post.__dict__, "message": "Post deleted successfully"}

