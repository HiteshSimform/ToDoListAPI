from repository import task_repo
from schema.task import TaskCreate, TaskUpdate
from datetime import date, timedelta


def test_repo_create(db):
    task_data = TaskCreate(title="Repo Task", due_date=date.today() + timedelta(days=1))
    task = task_repo.create_task(db, task_data)
    assert task.id is not None


def test_repo_get_by_id(db):
    task = task_repo.create_task(db, TaskCreate(title="Find Me"))
    found = task_repo.get_task_by_id(db, task.id)
    assert found.id == task.id


def test_repo_update(db):
    task = task_repo.create_task(db, TaskCreate(title="Old Repo"))
    updated = task_repo.update_task(db, task.id, TaskUpdate(title="Updated Repo"))
    assert updated.title == "Updated Repo"


def test_repo_delete(db):
    task = task_repo.create_task(db, TaskCreate(title="Soft Delete"))
    success = task_repo.delete_task(db, task.id)
    assert success
    deleted = task_repo.get_task_by_id(db, task.id)
    assert deleted is None
