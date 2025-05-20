from sqlalchemy.orm import Session
from uuid import UUID
from schema.task import TaskCreate, TaskUpdate
from repository import task_repo
from fastapi import HTTPException


def create_task_service(db: Session, task_data: TaskCreate):
    return task_repo.create_task(db, task_data)


def get_task_service(db: Session, task_id: UUID):
    task = task_repo.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not Found")
    return task


def get_all_task_service(db: Session):
    return task_repo.get_all_tasks(db)


def update_task_service(db: Session, task_id: UUID, task_data: TaskUpdate):
    task = task_repo.update_task(db, task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not Found")
    return task


def delete_task_service(db: Session, task_id: UUID):
    success = task_repo.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"details": "Task deleted Successfully"}
