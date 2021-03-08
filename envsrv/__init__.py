import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SSECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
                                'postgres://postgres:postgres@localhost:5432/envsrvdb',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    @app.route('/')
    def root_app():
        return "Jai Hanuman! Jai Shree Ram"

    return app