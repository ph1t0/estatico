from estatico import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/')
    assert response.data == b'<!doctype html>\n<title>Hello from Flask</title>\n<h1>Hello, World!</h1>'
