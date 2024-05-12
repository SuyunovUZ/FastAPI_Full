from fastapi import FastAPI, HTTPException, Depends
from pydantic import Field, BaseModel
from uuid import UUID
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

app = FastAPI(title='Books API')

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Book(BaseModel):
    title: str = Field(min_length=1, max_length=212)
    author: str = Field(min_length=1, max_length=212)
    description: str = Field(min_length=1, max_length=212)
    price: int = Field(gt=0, lt=1000)


BOOKS = []


@app.post('/books')
async def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.price = book.price

    db.add(book_model)
    db.commit()

    return book


@app.get('/books')
async def read_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


@app.put('/books/{book_id}')
async def read_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Book with id {book_id} does not exist'
        )
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.price = book.price

    db.add(book_model)
    db.commit()

    return book


@app.delete('/books/{book_id}')
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Book with id {book_id} does not exist'
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()
    return f'Deleted book with id {book_id}'
