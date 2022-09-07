from flask import Flask
from flask_restful import Api

import generator.yes as yesAnswer
import generator.no as noAnswer
import generator.random as randomAnswer

app = Flask(__name__)
api = Api(app)


api.add_resource(noAnswer.No, "/no")
api.add_resource(yesAnswer.Yes, "/yes")
api.add_resource(randomAnswer.Random, "/random")

if __name__ == '__main__':
    app.run(debug=False)
