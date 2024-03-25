from elote import EloCompetitor
import json
from collections import OrderedDict

characters = {}

with open("battles.json") as file:
    sagas = json.load(file)

for saga_name, saga_battles in sagas.items():
    for battle in saga_battles:
        if battle["a"] not in characters:
            characters[battle["a"]] = EloCompetitor(initial_rating=1500)
        if battle["b"] not in characters:
            characters[battle["b"]] = EloCompetitor(initial_rating=1500)
        if battle["winner"] == "a":
            characters[battle["a"]].beat(characters[battle["b"]])
        elif battle["winner"] == "b":
            characters[battle["b"]].beat(characters[battle["a"]])
        else:
            characters[battle["a"]].tied(characters[battle["b"]])

results = OrderedDict([(character[0], character[1].rating) for character in sorted(characters.items(), key=lambda item: item[1].rating, reverse=True)])

with open("results.json", "w") as result_file:
    json.dump(results, result_file)
