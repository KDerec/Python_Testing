import json
import os
import datetime

path = os.path.dirname(os.path.abspath(__file__))


def loadClubs():
    """Return the content of clubs.json in a list."""
    with open(path + "\\clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    """Return the content of competitions.json in a list."""
    with open(path + "\\competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def checkAndCreateIsInThePastForCompetitions(competitions):
    """
    Add a "is_in_the_past" key for a list of dicts with "date" key.

            Parameters:
                    competitions (list): A list of dict with a "date" key and a
                    value formated in "%Y-%m-%d %H:%M:%S" format

            Returns:
                    competitions (list): A list of dict with a "is_in_the_past"
                    key egal to True or False
    """
    now = datetime.datetime.now()
    for i in range(len(competitions)):
        competitionDateStr = competitions[i]["date"]
        competitionDateObj = datetime.datetime.strptime(
            competitionDateStr, "%Y-%m-%d %H:%M:%S"
        )
        if competitionDateObj < now:
            competitions[i]["is_in_the_past"] = True
        else:
            competitions[i]["is_in_the_past"] = False
    return competitions
