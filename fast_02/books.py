from datetime import datetime
# pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI(title='Books API', description='this api for books project', version='1.0.0')


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1, max_length=212)
    author: str or None = Field(min_length=1, max_length=212)
    description: str or None = Field(min_length=1, max_length=600)
    raiting: int = Field(gt=-1, lt=101)
    date: datetime = Field(default_factory=datetime.now)


database = []


@app.get('/')
async def read_root():
    return {'message': 'Welcome to FastAPI Books API'}


@app.get('/books')
async def get__all_books():
    return database


@app.post('/books')
async def create_book(book: Book):
    database.append(book)
    return {'data': book, 'message': 'Book created successfully'}


@app.put('/books/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for i in database:
        counter += 1
        if i.id == book_id:
            # i.title = book.title
            # i.author = book.author
            # i.description = book.description
            # i.date = book.date
            database[counter - 1] = book
            return {'data': database[counter - 1], 'message': 'book updated successfully'}

    raise HTTPException(
        status_code=404,
        detail=f'ID: {counter-1} book not found'
    )


@app.delete('/books/{book_id}')
async def delete_book(book_id: UUID):
    counter = 0
    for i in database:
        counter += 1
        if i.id == book_id:
            del database[counter - 1]
            return {'data': database[counter - 1], 'message': 'book deleted successfully'}
    raise HTTPException(
        status_code=404,
        detail=f'ID: {counter-1} book not found'
    )
