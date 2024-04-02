# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from os import path

db = SQLAlchemy()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__, template_folder='templates')

    # Configure the Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./cafes.db"

    db.init_app(app)

    # Imports
    from .views import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)
    

    return app