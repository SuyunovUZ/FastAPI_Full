from fastapi import FastAPI, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Post, Author

app = FastAPI(title='Simple Tortoise API')


async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]}
)


@app.on_event("startup")
async def startup():
    await init_db()


# Pydantic model API
Post_model = pydantic_model_creator(Post, name='Post')
Author_model = pydantic_model_creator(Author, name='Author')

@app.post("/author")
async def create_author(author: Author_model):
    user = await Author.create(**author.dict())
    return user


@app.post("/post")
async def create_post(post: Post_model):
    return await Post.create(**post.dict())


@app.post("/posts")
async def get_posts(author_id: int, post: Post_model):
    post = await Post.create(author_id=author_id, title=post.title, body=post.body, image=post.image)
    return post


@app.get('/posts')
async def get_posts():
    return await Post.all()


@app.get('/posts/{pk}')
async def get_post(pk: int):
    post = await Post.get_or_none(id=pk)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post does not exist")

    return post


@app.put('/posts/{pk}')
async def update_post(pk: int, title: str, content: str):
    post = await Post.get_or_none(id=pk)
    if post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post does not exist")

    post.title = title
    post.content = content
    await post.save()
    return post


@app.delete('/posts/{pk}')
async def delete_post(pk: int):
    post = await Post.get_or_none(id=pk)
    if post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Post does not exist')

    await post.delete()
    return {'message': 'Deleted successfully'}
