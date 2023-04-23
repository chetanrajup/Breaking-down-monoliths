from flask import Flask, Response
from flask_restful import Resource,Api
import math

class GreatestCommonDivisor(Resource):

	def get(self,a,b):
		return Response(f"{math.gcd(a,b)}")

app = Flask(__name__)
api = Api(app)

api.add_resource(GreatestCommonDivisor,'/<int:a>/<int:b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
