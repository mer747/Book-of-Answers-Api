from flask import Flask
from flask_restful import Api

from generator.yes import Yes
from generator.no import No
from generator.random import Random

app = Flask(__name__)
api = Api(app)


api.add_resource(No, "/no")
api.add_resource(Yes, "/yes")
api.add_resource(Random, "/random")

if __name__ == '__main__':
    app.run(debug=False)
