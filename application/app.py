import flask
from application.extensions import db
from application.config import DevelopmentConfig


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    return app
