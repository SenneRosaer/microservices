import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_rating_app(script_info=None):
    app = Flask(__name__)

    CORS(app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    from rating.api.rating import rating_blueprint
    app.register_blueprint(rating_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'rating_app':app , 'database':db}

    return app