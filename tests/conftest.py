import pytest
from flaskr.server import create_app


@pytest.fixture()
def test_client():
    flask_app = create_app(test_config=True)
    yield flask_app.test_client()
