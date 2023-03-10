from flask import Flask

def create_app():
    app = Flask(__name__)

    from .authenticate import auth as authblueprint

    app.register_blueprint(authblueprint)

    return app