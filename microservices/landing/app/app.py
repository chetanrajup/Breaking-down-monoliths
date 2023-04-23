from flask import Flask, render_template, request, flash, redirect, url_for
import requests
from flask_restful import Api
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
urls = {
    "addition": "http://addition-service:5050",
    "subtraction": "http://subtraction-service:5050",
    "multiplication": "http://multiplication-service:5050",
    "division": "http://division-service:5050",
    "exponent": "http://exponent-service:5050"

}


def get_response(service, n1, n2):
    result = {
        "flag": 1,
        "message": ""
    }
    try:
        res = requests.get(f"{urls[service]}/{n1}/{n2}")
        result["flag"] = 0
        result["message"] = res.text
    except:
        result["message"] = f"{service}-service is down ): try after some time..."

    return result


def add(n1, n2):
    return get_response("addition", n1, n2)


def minus(n1, n2):
    return get_response("subtraction", n1, n2)


def multiply(n1, n2):
    return get_response("multiplication", n1, n2)


def divide(n1, n2):
    return get_response("division", n1, n2)


def exponent(n1, n2):
    return get_response("exponent", n1, n2)


@app.route('/', methods=['POST', 'GET'])
def index():
    flag = 0
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')

    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
    except:
        number_1 = number_2 = 0

    operation = request.form.get('operation')
    result = {
        "flag": 1,
        "message": ""
    }
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result = minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'exponent':
        result = exponent(number_1, number_2)
    elif operation == 'divide':
        if number_2 == 0:
            result["flag"] = 1
            result["message"] = "Divide by Zero Error"
        else:
            result = divide(number_1, number_2)
    if result["flag"] == 0:
        flash(
            f'The result of operation {operation} on {number_1} and {number_2} is {result["message"]}')
    else:
        flash(result["message"])
    try:
        return render_template('index.html')
    except Exception as e:
        return f"An error occurred"


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
