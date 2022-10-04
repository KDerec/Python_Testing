import json
import os
import datetime

path = os.path.dirname(os.path.abspath(__file__))


def loadClubs():
    with open(path + "\\clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open(path + "\\competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def checkAndCreateIsInThePastForCompetitions(competitions):
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
