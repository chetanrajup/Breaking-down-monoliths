from flask import Flask, Response
from flask_restful import Resource,Api
import math

class LeastCommonMultiple(Resource):

	def get(self,a,b):
		return Response(f"{abs(a*b) // math.gcd(a, b)}")

app = Flask(__name__)
api = Api(app)

api.add_resource(LeastCommonMultiple,'/<int:a>/<int:b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
