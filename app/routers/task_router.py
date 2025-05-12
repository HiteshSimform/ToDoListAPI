from fastapi import APIRouter, Depends, status
from typing import List
from uuid import UUID
from schema.task import TaskCreate, TaskUpdate, TaskOut
from dependencies.db_dependencies import get_db_session
from sqlalchemy.orm import Session
from services import task as task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db:Session = Depends(get_db_session)):
    return task_service.create_task_service(db, task_data)

@router.get("/", response_model=List[TaskOut])
def get_tasks(db: Session=Depends(get_db_session)):
    return task_service.get_all_task_service(db)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: UUID, db: Session=Depends(get_db_session)):
    return task_service.get_task_service(db, task_id)

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: UUID, task_data: TaskUpdate, db: Session=Depends(get_db_session)):
    return task_service.update_task_service(db, task_id, task_data)

@router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID, db: Session=Depends(get_db_session)):
    return task_service.delete_task_service(db, task_id)