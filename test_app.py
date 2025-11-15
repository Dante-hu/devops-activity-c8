# test_app.py
import app


def test_hello():
    client = app.app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_goodbye():
    client = app.app.test_client()
    response = client.get("/goodbye")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Goodbye, World!"}


def test_mood():
    client = app.app.test_client()
    response = client.post("/mood", json={"mood": "great"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "I'm feeling great!"}
