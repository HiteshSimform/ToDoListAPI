import uuid
from sqlalchemy import Column, String, Text, Date, Enum, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import enum
from sqlalchemy.dialects.postgresql import UUID  # PostgreSQL specific
from db.base import Base

# Base = declarative_base()


class TaskStatusEnum(str, enum.Enum):
    """
    Enumeration for task status.

    Attributes:
        pending (str): Task is yet to be started.
        completed (str): Task has been completed.
        in_progress (str): Task is currently in progress.
    """

    pending = "pending"
    completed = "completed"
    in_progress = "in_progress"


class Task(Base):
    """
    Task model represents a task in the to-do or task management system.

    Attributes:
        id (UUID): Unique identifier for the task.
        title (str): Short title of the task.
        description (str): Detailed description of the task (optional).
        due_date (date): Deadline for the task completion (optional).
        status (TaskStatusEnum): Current status of the task.
        priority (int): Priority of the task.
        created_at (datetime): Timestamp when the task was created.
        updated_at (datetime): Timestamp when the task was last updated.
        is_deleted (bool): Flag to indicate if the task is soft-deleted.
    """

    __tablename__ = "tasks"

    # id = Column(
    #     UUID(as_uuid=True),
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     unique=True,
    #     nullable=False,
    #     doc="UUID primary key.",
    # )
    id = Column(
        String(36),  # Store UUID as a string (length 36 for UUIDs in string format)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # Default UUID as string
        unique=True,
        nullable=False,
        doc="UUID primary key as string.",
    )
    title = Column(String, index=True, nullable=False, doc="Title of the task.")
    description = Column(Text, nullable=True, doc="Optional detailed description.")
    due_date = Column(Date, nullable=True, doc="Optional deadline for the task.")
    status = Column(
        Enum(TaskStatusEnum),
        default=TaskStatusEnum.pending,
        nullable=False,
        doc="Status of the task (pending, completed, in_progress).",
    )
    priority = Column(Integer, default=3, doc="Priority level (default is 3).")
    created_at = Column(
        DateTime, server_default=func.now(), doc="Timestamp when the task was created."
    )
    updated_at = Column(
        DateTime, onupdate=func.now(), doc="Timestamp when the task was last updated."
    )
    is_deleted = Column(
        Boolean, default=False, doc="Soft delete flag. True if the task is deleted."
    )

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status}, due_date={self.due_date})>"


# from sqlalchemy import Column, Integer, String, Text, Date, Enum, Boolean, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# import enum
# from typing import Optional

# Base = declarative_base()


# class TaskStatusEnum(str, enum.Enum):
#     """
#     TaskStatusEnum :
#     """

#     pending = "pending"
#     completed = "completed"
#     in_progress = "in_progress"


# class Task(Base):
#     """
#     Task :
#     """

#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True, nullable=False)
#     description = Column(Text, nullable=True)
#     due_date = Column(Date, nullable=True)
#     status = Column(
#         Enum(TaskStatusEnum), default=TaskStatusEnum.pending, nullable=False
#     )
#     priority = Column(Integer, default=3)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, onupdate=func.now())
#     is_deleted = Column(Boolean, default=False)

#     def __repr__(self):
#         return f"<Task(id={self.id}, title={self.title}, status={self.status}, due_date={self.due_date})>"
