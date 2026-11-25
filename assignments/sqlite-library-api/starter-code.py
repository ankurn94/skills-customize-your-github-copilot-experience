import sqlite3

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

DATABASE_NAME = "library.db"

app = FastAPI(title="SQLite Library API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=1000)


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
            """
        )


initialize_database()


@app.get("/")
def welcome():
    return {"message": "Welcome to the SQLite Library API"}


@app.get("/books")
def list_books():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, author, year FROM books ORDER BY id"
        ).fetchall()

    return [dict(row) for row in rows]


# TODO: Implement GET /books/{book_id}


# TODO: Implement POST /books


# TODO: Implement PUT /books/{book_id}


# TODO: Implement DELETE /books/{book_id}
