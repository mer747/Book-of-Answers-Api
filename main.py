from flask import Flask
from flask_restful import Api, Resource
import json
import random

app = Flask(__name__)
api = Api(app)


class Yes(Resource):
    def get(Resource):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["yes"])
            return {"answer": answer}


class No(Resource):
    def get(Resource):
        with open("answers.json", "r") as file:
            data = json.load(file)
            answer = random.choice(data["no"])
            return {"answer": answer}


class Random(Resource):
    def get(Resource):
        with open("answers.json", "r") as file:
            data = json.load(file)
            decide = [data["yes"], data["no"]]
            randomize = random.choice(decide)
            answer = random.choice(randomize)
            return {"answer": answer}


api.add_resource(No, "/no")
api.add_resource(Yes, "/yes")
api.add_resource(Random, "/random")

if __name__ == '__main__':
    app.run(debug=True)
