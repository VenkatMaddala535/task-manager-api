def test_create_task(client):

    response = client.post(
        "/tasks",
        json={
            "title": "Learn Jenkins",
            "description": "Testing API"
        }
    )

    assert response.status_code == 201

    assert response.json["title"] == "Learn Jenkins"


def test_get_tasks(client):

    client.post(
        "/tasks",
        json={
            "title": "Task 1"
        }
    )

    response = client.get("/tasks")

    assert response.status_code == 200

    assert len(response.json) == 1


def test_update_task(client):

    response = client.post(
        "/tasks",
        json={
            "title": "Old Title"
        }
    )

    task_id = response.json["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "New Title",
            "completed": True
        }
    )

    assert response.status_code == 200

    assert response.json["title"] == "New Title"

    assert response.json["completed"] is True


def test_delete_task(client):

    response = client.post(
        "/tasks",
        json={
            "title": "Delete Me"
        }
    )

    task_id = response.json["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200