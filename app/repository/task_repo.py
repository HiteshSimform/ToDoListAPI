from sqlalchemy.orm import Session
from model.task import Task
from schema.task import TaskCreate, TaskUpdate, TaskOut
from uuid import UUID
from pydantic import UUID4

def create_task(db: Session, task_data: TaskCreate) -> Task:
    task = Task(**task_data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: UUID4) -> Task:
    return db.query(Task).filter(Task.id == str(task_id), Task.is_deleted == False).first()

def get_all_tasks(db:Session):
    return db.query(Task).filter(Task.is_deleted==False).all()

def update_task(db: Session, task_id: UUID, task_data: TaskUpdate) -> Task:
    task=  get_task_by_id(db,str(task_id))
    if task:
        for key, value in task_data.model_dump(exclude_unset=True).items():
            setattr(task,key,value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: UUID4) -> bool:
    task = get_task_by_id(db, task_id)
    if task:
        task.is_deleted = True
        db.commit()
        return True
    return False