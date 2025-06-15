from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo = PyMongo(app)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()