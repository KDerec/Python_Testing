from ..conftest import test_client


def test_index(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200


def test_showSummary_with_correct_email(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/showSummary' page is posted (POST) with correct email
    THEN check that the response is valid
    """
    response = test_client.post(
        "/showSummary", data={"email": "test@test.com"}
    )

    assert response.status_code == 200


def test_showSummary_with_unknow_email(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/showSummary' page is posted (POST) with unknow email
    THEN check that the response isn't valid
    """
    response = test_client.post(
        "/showSummary", data={"email": "wrong@test.com"}
    )

    assert response.status_code == 401
