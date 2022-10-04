import pytest
from flaskr.server import create_app


@pytest.fixture()
def test_client():
    flask_app = create_app(test_config=True)
    yield flask_app.test_client()


@pytest.fixture()
def undeducted_points_text():
    data = {
        "available_points": "Points available: 22",
        "number_of_places": "Number of Places: 20",
    }
    return data


@pytest.fixture()
def db_data():
    data = {
        "club": "Club1",
        "competition": "Competition1",
        "email": "test@test.com",
    }
    return data
