# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for a collection of books using FastAPI. You will define API routes, validate request data, manage in-memory resources, and return appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the API and Define the Data Model

#### Description
Set up a FastAPI application and define a Pydantic model that represents a book.

#### Requirements
Completed program should:

- Create a FastAPI application named `app`
- Define a `Book` model with `id`, `title`, `author`, and `year` fields
- Add a root `GET /` endpoint that returns a welcome message
- Start successfully with `uvicorn main:app --reload`


### 🛠️ Implement CRUD Endpoints

#### Description
Use an in-memory dictionary to store book records and add endpoints for listing, retrieving, creating, updating, and deleting books.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book
- Implement `POST /books` to create a book and return it with HTTP status 201
- Implement `PUT /books/{book_id}` to replace a book
- Implement `DELETE /books/{book_id}` to remove a book
- Return HTTP status 404 with a JSON detail message when a book is not found


### 🛠️ Validate and Document the API

#### Description
Improve the API with input validation and verify that the automatic API documentation and endpoint behavior work as expected.

#### Requirements
Completed program should:

- Make `title` and `author` at least 1 character long
- Require `year` to be at least 1000
- Prevent duplicate book IDs when creating or updating
- Test at least one success case and one error case using FastAPI's interactive Swagger UI at `/docs`
- Use the Swagger UI to confirm the request bodies, responses, and status codes
