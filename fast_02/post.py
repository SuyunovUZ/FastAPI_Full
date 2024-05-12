from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title='Post API')


class Category(BaseModel):
    title: str = Field(min_length=4, max_length=212)
    date: datetime = Field(default_factory=datetime.utcnow)


class Tag(BaseModel):
    title: str = Field(min_length=2, max_length=212)
    date: datetime = Field(default_factory=datetime.utcnow)


class Post(BaseModel):
    id: UUID
    title: str or None = Field(min_length=1, max_length=212)
    category: Category = Field(default_factory=Category)
    tags: List[Tag] = Field(default_factory=Tag)
    date: datetime = Field(default_factory=datetime.utcnow)
    description: str = Field(min_length=2, max_length=212)


posts = []


@app.post("/post")
def create_post(post: Post):
    posts.append(post)
    return {"data": post}


@app.get('/post')
def get_posts():
    return posts


@app.put('/post/{id}')
def update_post(id: UUID, post: Post):
    count = 0
    for i in posts:
        count = count + 1
        if i.id == id:
            i.title = post.title
            i.date = post.date
            i.description = post.description
    raise HTTPException(
        status_code=404, detail=f'Post {id} does not exist'
    )


@app.delete('/post/{id}')
def delete_post(id: UUID):
    count = 0
    for i in posts:
        count += 1
        if i.id == id:
            del posts[count - 1]
    raise HTTPException(
        status_code=404,
        detail=f'Post deleted {count-1} does not exist'
    )
