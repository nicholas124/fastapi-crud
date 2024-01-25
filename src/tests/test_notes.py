# test_notes.py

import json
import pytest
from app.api import crud

# Test case for creating a note
def test_create_note(test_app, monkeypatch):
    # Define a test request payload
    test_request_payload = {"title": "something", "description": "something else"}
    
    # Define the expected response payload
    test_response_payload = {"id": 1, "title": "something", "description": "something else"}

    # Define a mock function to replace the actual post function from the 'crud' module
    async def mock_post(payload):
        return 1

    # Use monkeypatch to replace the 'post' function with the mock function
    monkeypatch.setattr(crud, "post", mock_post)

    # Make a POST request to create a note with the test payload
    response = test_app.post("/notes/", content=json.dumps(test_request_payload),)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    # Assert that the response payload matches the expected payload
    assert response.json() == test_response_payload


# Test case for creating a note with invalid JSON
def test_create_note_invalid_json(test_app):
    # Make a POST request with an invalid JSON payload
    response = test_app.post("/notes/", content=json.dumps({"title": "something"}))

    # Assert that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422


def test_read_note(test_app, monkeypatch):
    # Define a test request payload
    test_data = {"id": 1, "title": "something", "description": "something else"}
    
    async def mock_get(id):
        return test_data
    
    monkeypatch.setattr(crud, "get", mock_get)
    
    response = test_app.get("/notes/1")
    
    assert response.status_code == 200
    assert response.json() == test_data
    
def test_read_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/notes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

    response = test_app.get("/notes/0")
    assert response.status_code == 422
    
# def test_read_note_not_found(test_app, monkeypatch):
#     async def mock_get(id):
#         return None
    
#     monkeypatch.setattr(crud, "get", mock_get)
    
#     response = test_app.get("/notes/1")
    
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Note not found"}
    
    
def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1},
        {"title": "someone", "description": "someone else", "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/notes/")
    assert response.status_code == 200
    assert response.json() == test_data
    
    
    
def test_update_note(test_app, monkeypatch):
    test_update_data = {"title": "someone", "description": "someone else", "id": 1}

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/notes/1/", content=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
    ],
)
def test_update_note_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/notes/{id}/", content=json.dumps(payload),)
    assert response.status_code == status_code
    
    
def test_remove_note(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/notes/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/notes/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"