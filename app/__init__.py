from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
from .utils.error_handle import handle_error

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_error_handler(Exception, handle_error)

    db.init_app(app)
    Migrate(app, db)

    from app.routes.interaccion_routes import interaccion_bp

    app.register_blueprint(interaccion_bp, url_prefix="/api")

    return app
