import json
import random
from flask_restful import Resource


class No(Resource):
    def get(self):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["no"])
            return {"answer": answer, "type": "no"}
