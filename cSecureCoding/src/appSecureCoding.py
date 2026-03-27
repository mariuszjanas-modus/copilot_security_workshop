from flask import Flask, jsonify
import random

def create_app():
    app = build_routes()
    app.run(debug=True)


def build_routes():

    app = Flask(__name__)

    @app.route('/secure_coding')
    def hello201():
        return "Welcome to the secure coding module!"

    @app.route('/secure_coding/random_boolean')
    def random_boolean():
        return jsonify({"value": random.choice([True, False])})

    @app.route('/secure_coding/cat')
    def cat():
        dummy_data = {
            "name": "Whiskers",
            "breed": "Siamese",
            "age": 3
        }
        response = jsonify(dummy_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return app