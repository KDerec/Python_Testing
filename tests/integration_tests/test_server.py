import pytest
from ..conftest import (
    test_client,
    undeducted_points_text,
    club_and_competition,
)


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
    THEN check that the response is OK and welcome message is here
    """
    email = "test@test.com"
    response = test_client.post("/showSummary", data={"email": email})

    assert response.status_code == 200
    assert f"Welcome, {email}" in response.data.decode()


def test_showSummary_with_unknow_email(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/showSummary' page is posted (POST) with unknow email
    THEN check that the response is unauthorized and no account message is here
    """
    email = "wrong@test.com"
    response = test_client.post("/showSummary", data={"email": email})

    assert response.status_code == 401
    assert "No account related to this email" in response.data.decode()


def test_purchasePlaces_happy_path(test_client, club_and_competition):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/purchasePlaces' page is posted (POST) with enough club point,
    competition place and required places
    THEN check that the response is OK, success message is here,
    available point and number of place are deducted
    """
    club_name = club_and_competition["club"]
    competition_name = club_and_competition["competition"]
    requiredPlaces = 5
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 200
    assert "Points available: 17" in response.data.decode()
    assert "Number of Places: 15" in response.data.decode()
    assert "Great-booking complete!" in response.data.decode()


def test_purchasePlaces_required_places_isnt_int(
    test_client, undeducted_points_text, club_and_competition
):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/purchasePlaces' page is posted (POST) with enough club point,
    competition place, but required place isn't an integer
    THEN check that the response is Bad request, error message is here,
    available point and number of place are the same
    """
    club_name = club_and_competition["club"]
    competition_name = club_and_competition["competition"]
    requiredPlaces = ""
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 400
    with pytest.raises(ValueError):
        int(requiredPlaces)
    assert undeducted_points_text["available_points"] in response.data.decode()
    assert undeducted_points_text["number_of_places"] in response.data.decode()
    assert (
        "Please enter an integer number, try again." in response.data.decode()
    )


def test_purchasePlaces_required_places_is_less_or_equal_to_zero(
    test_client, undeducted_points_text, club_and_competition
):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/purchasePlaces' page is posted (POST) with enough club point,
    competition place, but required places is less or equal to zero
    THEN check that the response is Bad request, error message is here,
    available point and number of place are the same
    """
    club_name = club_and_competition["club"]
    competition_name = club_and_competition["competition"]
    requiredPlaces = -1
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 400
    assert undeducted_points_text["available_points"] in response.data.decode()
    assert undeducted_points_text["number_of_places"] in response.data.decode()
    assert (
        "Please enter a number bigger than 0, try again."
        in response.data.decode()
    )


def test_purchasePlaces_more_required_places_than_club_points(
    test_client, undeducted_points_text, club_and_competition
):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/purchasePlaces' page is posted (POST) with more required places
    than the club points
    THEN check that the response is Bad request, error message is here,
    available point and number of place are the same
    """
    club_name = club_and_competition["club"]
    competition_name = club_and_competition["competition"]
    requiredPlaces = 100
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 400
    assert undeducted_points_text["available_points"] in response.data.decode()
    assert undeducted_points_text["number_of_places"] in response.data.decode()
    assert (
        "You can&#39;t order more than your available points"
        in response.data.decode()
    )


def test_purchasePlaces_more_required_places_than_available_places(
    test_client, undeducted_points_text, club_and_competition
):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/purchasePlaces' page is posted (POST) with enough club point,
    but more required places than the available place of the competition
    THEN check that the response is Bad request, error message is here,
    available point and number of place are the same
    """
    club_name = club_and_competition["club"]
    competition_name = club_and_competition["competition"]
    requiredPlaces = 21
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 400
    assert undeducted_points_text["available_points"] in response.data.decode()
    assert undeducted_points_text["number_of_places"] in response.data.decode()
    assert (
        """You can&#39;t order more than 20 places 
                    for this competitions, try again."""
        in response.data.decode()
    )
