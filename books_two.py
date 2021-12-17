from typing import Optional
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of book",
                                       max_length=100,
                                       min_length=1, )
    rating: int = Field(gt=-1, lt=101)

    class Config:
        # Serves as example purpose
        schema_extra = {
            "example": {
                "id": "1be23387-491b-494d-a705-5500cece7e95",
                "title": "Computer Science Pro",
                "author": "Coding with Mati",
                "description": "Very nice description",
                "rating": 75
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter-1]
            return f'ID {book_id} DELETED'


def create_books_no_api():
    book_1 = Book(id="dbe23387-491b-494d-a705-5500cece7e95",
                  title="Title 1",
                  author="author 1",
                  description="Description 1",
                  rating=60)

    book_2 = Book(id="13a12d07-923e-4f5a-a83d-a5aea5b13d7a",
                  title="Title 2",
                  author="author 2",
                  description="Description 2",
                  rating=60)

    book_3 = Book(id="590d6e7d-4854-4588-9de0-43f254b44e20",
                  title="Title 3",
                  author="author 3",
                  description="Description 3",
                  rating=60)

    book_4 = Book(id="2c2ee173-54ff-4349-9f3a-5d5db9666c24",
                  title="Title 4",
                  author="author 4",
                  description="Description 4",
                  rating=60)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
