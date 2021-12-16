from typing import Optional

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Title 1', 'author': 'Author 1'},
    'book_2': {'title': 'Title 2', 'author': 'Author 2'},
    'book_3': {'title': 'Title 3', 'author': 'Author 3'},
    'book_4': {'title': 'Title 4', 'author': 'Author 4'},
    'book_5': {'title': 'Title 5', 'author': 'Author 5'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


# Pass in parameter, book: str, you can make it optional by Optional[str]
@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


# Needs to be above url with parameter, otherwise will think its parameter
@app.get("/books/mybook")
async def read_favourite_book():
    return {"book_title": "My favourite book"}


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):

    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}

    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}

    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}

    return {"Direction": direction_name, "sub": "Right"}


@app.post("/")
async def create_book(book_title: str, book_author: str):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {"title": book_title, "author": book_author}
    BOOKS[book_name] = book_information


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'






