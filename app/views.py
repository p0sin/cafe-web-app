from flask import render_template, request
from .models import Cafes

def register_routes(app, db):

    @app.route('/')
    def index():
        cafes = Cafes.query.all()
        return render_template('index.html')


