import json
import os


path = os.path.dirname(os.path.abspath(__file__))


def loadClubs():
    with open(path + "\\clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open(path + "\\competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions
