from locust import HttpUser, task
from flaskr.utils import loadClubs, loadCompetitions


class ProjectPerfTest(HttpUser):
    competition = loadCompetitions()[2]
    club = loadClubs()[2]

    @task
    def index(self):
        self.client.get("/")

    @task
    def showSummary(self):
        self.client.post("/showSummary", {"email": self.club["email"]})

    @task
    def purchasePlaces(self):
        self.client.post(
            "/purchasePlaces",
            {
                "club": self.club["name"],
                "competition": self.competition["name"],
                "places": 0,
            },
        )

    @task
    def book(self):
        club_name = self.club["name"]
        competition_name = self.competition["name"]
        self.client.get(f"/book/{competition_name}/{club_name}")

    @task
    def pointsDisplayBoard(self):
        self.client.get("/pointsDisplayBoard")
