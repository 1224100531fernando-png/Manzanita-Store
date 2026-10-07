from flask import Flask

from config import Config


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    return app