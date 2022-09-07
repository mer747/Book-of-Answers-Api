import json
import random
from flask_restful import Resource


class Random(Resource):
    def get(self):
        with open("answers.json", "r") as file:
            data = json.load(file)
            yes = data["yes"]
            no = data["no"]
            decide = [yes, no]
            randomize = random.choice(decide)
            answer = random.choice(randomize)
            if randomize == yes:
                return {"answer": answer, "type": "yes"}
            elif randomize == no:
                return {"answer": answer, "type": "no"}
