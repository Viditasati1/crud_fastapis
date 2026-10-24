# FastAPI Task CRUD API

A simple REST API built using FastAPI, SQLAlchemy, and SQLite to manage tasks.

## Features
- Create a task
- Retrieve all tasks
- Retrieve a task by ID
- Update a task using PATCH
- Delete a task
- Automatic API documentation with Swagger UI

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Setup

Clone the repository and navigate to the project directory.

```bash
git clone <your-repository-url>
cd fastapicrud
```

Create and activate a virtual environment:


python3 -m venv venv
source venv/bin/activate




Run the application:


uvicorn app.main:app --reload


## API Documentation

Open the following URL after starting the server:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /tasks/| Create a task |
| GET | /tasks/ | Get all tasks |
| GET | /tasks/{task_id} | Get a task by ID |
| PATCH | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## License

This project is intended for learning and practice.
