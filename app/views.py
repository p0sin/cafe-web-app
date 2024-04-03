from flask import render_template, request, redirect, url_for
from .models import Cafes
from .forms import AddCafe

def register_routes(app, db):

    @app.route('/')
    def index():
        cafes = Cafes.query.all()
  
        return render_template('index.html', cafes=cafes)
    
    @app.route('/add', methods=["GET", "POST"])
    def add():
        form = AddCafe()

        if request.method == 'POST':
            map_url = form.map_url.data
            map_url = map_url.split('"')[1]
            
            cafe = Cafes(
                name=request.form["name"],
                image=request.form["image_url"],
                location=map_url
            )

            db.session.add(cafe)
            db.session.commit()

            # Delete all records from the Cafes db
            # Cafes.query.delete()
            # db.session.commit()

            return redirect(url_for('index'))

        return render_template('add.html', form=form)


