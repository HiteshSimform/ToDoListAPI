from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from typing import Optional
from uuid import UUID
from model.task import TaskStatusEnum


class TaskBase(BaseModel):
    title: str = Field(..., examples="Task 1")
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatusEnum] = TaskStatusEnum.pending
    priority: Optional[int] = Field(default=3, ge=1, le=5)

    @field_validator("due_date", mode="before")
    def validate_due_date(cls, v):
        if v and isinstance(v, date) and v < date.today():
            raise ValueError("Due date must be greater than current date")
        return v

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatusEnum] = None
    priority: Optional[int] = None

    class Config:
        orm_mode = True


class TaskOut(TaskBase):
    title: str = Field(..., example="Task 1")
