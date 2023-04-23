from flask import Flask, Response
from flask_restful import Resource,Api

class Multiplication(Resource):

	def get(self,a,b):
		return Response(f"{a*b}")

app = Flask(__name__)
api = Api(app)

api.add_resource(Multiplication,'/<float:a>/<float:b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
