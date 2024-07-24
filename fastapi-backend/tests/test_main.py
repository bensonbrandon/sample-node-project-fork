from fastapi.testclient import TestClient
from fastapi-backend.app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Jane Doe", "email": "janedoe@example.com"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Jane Doe", "email": "janedoe@example.com"
    }
