
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.crud import task as task_crud

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task)


@router.get("/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return task_crud.get_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = task_crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = task_crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_crud.update_task(db, task, task_data)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int, db: Session = Depends(get_db)):
    task = task_crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task_crud.delete_task(db, task)
