
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models.task import Task
from app.routes.task import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Task CRUD API",
    lifespan=lifespan
)


app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "task crud api is running"}
