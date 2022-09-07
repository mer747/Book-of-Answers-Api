import json
import random
from flask_restful import Resource


class Yes(Resource):
    def get(self):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["yes"])
            return {"answer": answer, "type": "yes"}
