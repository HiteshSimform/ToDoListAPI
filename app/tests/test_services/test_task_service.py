from services import task as task_service
from schema.task import TaskCreate, TaskUpdate
from datetime import date, timedelta


def test_create_task_service(db):
    task_data = TaskCreate(
        title="Service Task", due_date=date.today() + timedelta(days=1)
    )
    task = task_service.create_task_service(db, task_data)
    assert task.title == "Service Task"


def test_get_task_service(db):
    task_data = TaskCreate(title="Fetchable")
    created = task_service.create_task_service(db, task_data)
    fetched = task_service.get_task_service(db, created.id)
    assert fetched.id == created.id


def test_update_task_service(db):
    task = task_service.create_task_service(db, TaskCreate(title="Old Title"))
    updated = task_service.update_task_service(
        db, task.id, TaskUpdate(title="New Title")
    )
    assert updated.title == "New Title"


def test_delete_task_service(db):
    task = task_service.create_task_service(db, TaskCreate(title="Trash"))
    result = task_service.delete_task_service(db, task.id)
    assert result["details"] == "Task deleted Successfully"
