from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional
from uuid import UUID
from model.task import TaskStatusEnum
from datetime import datetime


class TaskBase(BaseModel):
    title: str = Field(..., examples="Task 1")
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatusEnum] = TaskStatusEnum.pending
    priority: Optional[int] = Field(default=3, ge=1, le=5)

    @field_validator("due_date", mode="before")
    @classmethod
    def validate_due_date(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            try:
                v = datetime.strptime(v, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
        if v < date.today():
            raise ValueError("Due date must be greater than or equal to today's date.")
        return v


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatusEnum] = None
    priority: Optional[int] = None


class TaskOut(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    due_date: Optional[date]
    status: TaskStatusEnum
    priority: int

    class Config:
        from_attributes = True
