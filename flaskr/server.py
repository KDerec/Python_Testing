from flask import Flask, render_template, request, redirect, flash, url_for
from flaskr.utils import (
    loadClubs,
    loadCompetitions,
    checkAndCreateIsInThePastForCompetitions,
)


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "something_special"

    if test_config is None:
        competitions = loadCompetitions()
        clubs = loadClubs()
    if test_config is True:
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
        clubs = [
            {"name": "Club1", "email": "test@test.com", "points": "22"},
            {"name": "Club2", "email": "test2@test.com", "points": "10"},
        ]

    competitions = checkAndCreateIsInThePastForCompetitions(competitions)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/showSummary", methods=["POST"])
    def showSummary():
        try:
            club = [
                club
                for club in clubs
                if club["email"] == request.form["email"]
            ][0]
            return render_template(
                "welcome.html", club=club, competitions=competitions
            )
        except IndexError:
            flash("No account related to this email, try again.", "error")
            return render_template("index.html"), 401

    @app.route("/book/<competition>/<club>")
    def book(competition, club):
        foundClub = [c for c in clubs if c["name"] == club][0]
        foundCompetition = [
            c for c in competitions if c["name"] == competition
        ][0]
        if foundCompetition["is_in_the_past"] is True:
            flash("You can't order place for an outdated competition.")
            return (
                render_template(
                    "welcome.html", club=foundClub, competitions=competitions
                ),
                400,
            )
        if foundClub and foundCompetition:
            return render_template(
                "booking.html", club=foundClub, competition=foundCompetition
            )
        else:
            flash("Something went wrong-please try again")
            return render_template(
                "welcome.html", club=club, competitions=competitions
            )

    @app.route("/purchasePlaces", methods=["POST"])
    def purchasePlaces():
        competition = [
            c for c in competitions if c["name"] == request.form["competition"]
        ][0]
        club = [c for c in clubs if c["name"] == request.form["club"]][0]
        clubPoints = int(club["points"])
        availablePlaces = int(competition["numberOfPlaces"])

        while True:
            try:
                placesRequired = int(request.form["places"])
            except ValueError:
                flash("⚠ Please enter an integer number, try again.")
                break
            if placesRequired < 0:
                flash("⚠ Please enter a number bigger than 0, try again.")
                break
            if placesRequired > clubPoints:
                flash(
                    """⚠ You can't order more than your available points, 
                    try again."""
                )
                break
            if placesRequired > availablePlaces:
                flash(
                    f"""⚠ You can't order more than {availablePlaces} places 
                    for this competitions, try again."""
                )
                break
            try:
                club[competition["name"]]
            except KeyError:
                club[competition["name"]] = 0

            if placesRequired + club[competition["name"]] > 12:
                reservedPoint = club[competition["name"]]
                flash(
                    f"""⚠ You can't order more than 12 places for this 
                    competitions (you already purchase {reservedPoint} places).
                    """
                )
                break
            if placesRequired <= availablePlaces:
                competition["numberOfPlaces"] = (
                    availablePlaces - placesRequired
                )
                club["points"] = clubPoints - placesRequired
                club[competition["name"]] += placesRequired
                flash(f"Great-booking complete! ({placesRequired} places)")
                return render_template(
                    "welcome.html", club=club, competitions=competitions
                )
            break

        return (
            render_template(
                "welcome.html", club=club, competitions=competitions
            ),
            400,
        )

    @app.route("/pointsDisplayBoard")
    def pointsDisplayBoard():
        return render_template("points-display-board.html", clubs=clubs)

    @app.route("/logout")
    def logout():
        return redirect(url_for("index"))

    if test_config is None:
        app.run(debug=True)
    if test_config is True:
        return app


if __name__ == "__main__":
    create_app()
