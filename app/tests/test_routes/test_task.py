import pytest
from datetime import date, timedelta
from uuid import UUID


def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Live project task",
            "due_date": str(date.today() + timedelta(days=2)),
            "priroty": 2,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data


def test_create_task_invalid_due_date(client):
    response = client.post(
        "/tasks/",
        json={"title": "Old Task", "due_date": str(date.today() - timedelta(days=1))},
    )
    assert response.status_code == 422


def test_get_all_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_task(client):
    new_task = client.post("/tasks/", json={"title": "One Task"}).json()
    task_id = new_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task(client):
    task = client.post("/tasks/", json={"title": "Update me"}).json()
    updated = client.put(f"/tasks/{task['id']}", json={"title": "Updated Title"})
    assert updated.status_code == 200
    assert updated.json()["title"] == "Updated Title"


def test_delete_task(client):
    task = client.post("/tasks/", json={"title": "To be Deleted"}).json()
    response = client.delete(f"/tasks/{task['id']}")
    assert response.status_code == 204
    get_deleted = client.get(f"/tasks/{task['id']}")
    assert get_deleted.status_code == 404
