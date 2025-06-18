from flask import Flask
from src.utils.database import mongo


def create_app():
    app = Flask(__name__)

    # Configuración
    app.config.from_object('config.settings.Config')

    # Extensiones
    mongo.init_app(app)

    # Blueprints
    from src.routes.movie_routes import movies_bp
    app.register_blueprint(movies_bp, url_prefix='/api/v1')

    return app