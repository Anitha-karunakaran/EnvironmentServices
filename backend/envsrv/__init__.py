import os
from flask import Flask, request, abort, jsonify

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    )

    @app.route('/')
    def root_app():

        return "Jai Hanuman"

    return app