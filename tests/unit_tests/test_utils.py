from flaskr.utils import checkAndCreateIsInThePastForCompetitions


def test_should_add_key_to_competition_dict():
    competitions = [
        {
            "name": "Competition1",
            "date": "2023-01-01 00:00:00",
            "numberOfPlaces": "20",
        },
        {
            "name": "Competition2",
            "date": "2020-12-12 12:00:00",
            "numberOfPlaces": "10",
        },
    ]
    assert (
        checkAndCreateIsInThePastForCompetitions(competitions)[0][
            "is_in_the_past"
        ]
        == False
    )
    assert (
        checkAndCreateIsInThePastForCompetitions(competitions)[1][
            "is_in_the_past"
        ]
        == True
    )
