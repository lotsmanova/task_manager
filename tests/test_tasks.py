from tests.test_auth import auth_header
from tests.conftest import client


def test_add_task():
    response = client.post("tasks/", json={"title": "test", "description": "test", "status": "create", "owner_id": 1},
                           headers=auth_header())
    assert response.status_code == 200
    assert "task_id" in response.json()


def test_get_tasks():
    response = client.get("tasks/",  headers=auth_header())
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_edit_task():
    task_id = 1
    response = client.patch(f"tasks/{task_id}", json={"title": "test_update", "description": "test",
                                                      "status": "create", "owner_id": 1},  headers=auth_header())
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_get_one_task():
    task_id = 1
    response = client.get(f"tasks/{task_id}",  headers=auth_header())
    assert response.status_code == 200
    assert "title" in response.json()


def test_delete_task():
    task_id = 1
    response = client.delete(f"tasks/{task_id}",  headers=auth_header())
    assert response.status_code == 200
    assert response.json()["message"] == "task deleted"
