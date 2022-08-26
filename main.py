from flask import Flask
from flask_restful import Api, Resource
import json
import random

app = Flask(__name__)
api = Api(app)


class Yes(Resource):
    def get(self):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["yes"])
            return {"answer": answer, "type": "yes"}


class No(Resource):
    def get(self):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["no"])
            return {"answer": answer, "type": "no"}


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


api.add_resource(No, "/no")
api.add_resource(Yes, "/yes")
api.add_resource(Random, "/random")

if __name__ == '__main__':
    app.run(debug=True)
