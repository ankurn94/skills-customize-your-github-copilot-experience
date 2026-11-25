# 📘 Assignment: SQLite Library API

## 🎯 Objective

Learn to persist application data by using SQLite with FastAPI. Students will replace temporary in-memory storage with a database and implement reliable CRUD operations.

## 📝 Tasks

### 🛠️ Create the Library Database

#### Description
Set up a SQLite database and connect it to a FastAPI application.

#### Requirements
Completed program should:

- Create a `library.db` database file when the application starts
- Create a `books` table with `id`, `title`, `author`, and `year` columns
- Make `id` the primary key and reject duplicate IDs
- Define a Pydantic model that validates `title` and `author` as non-empty strings and `year` as at least 1000
- Return validation errors through FastAPI

### 🛠️ Implement Database CRUD Operations

#### Description
Replace in-memory storage with SQL queries that manage books in SQLite.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book
- Implement `POST /books` to insert a new book
- Implement `PUT /books/{book_id}` to replace an existing book
- Implement `DELETE /books/{book_id}` to remove an existing book
- Return HTTP status 404 with a JSON detail message when a book is not found
- Return HTTP status 409 when a new or updated book would reuse an existing ID

### 🛠️ Preserve Data and Test the API

#### Description
Verify that SQLite persists data across server restarts and test successful and failed API requests.

#### Requirements
Completed program should:

- Confirm that a book remains available after stopping and restarting the application
- Use the `/docs` interface to test at least one successful case and one error case
- Verify that invalid input, missing books, and duplicate IDs produce the appropriate HTTP response
- Keep database connections open only for as long as each operation needs them
