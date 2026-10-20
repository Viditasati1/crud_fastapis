
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


# CREATE
def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# READ ALL
def get_tasks(db: Session):
    return db.query(Task).all()


# READ ONE
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


# UPDATE
def update_task(db: Session, db_task: Task, task: TaskUpdate):
    updates = task.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task


# DELETE
def delete_task(db: Session, db_task: Task):
    db.delete(db_task)
    db.commit()
