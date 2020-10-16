import os
import pytest

from estatico import create_app
from estatico.constants import FLASK_APP


os.environ['FLASK_APP'] = FLASK_APP


@pytest.fixture
def app():
    app = create_app()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
