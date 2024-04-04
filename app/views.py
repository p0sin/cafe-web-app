from flask import render_template, request, redirect, url_for
from .models import Cafes
from .forms import AddCafe

from datetime import datetime

def register_routes(app, db):

    @app.route('/')
    def index():
        cafes = Cafes.query.all()
  
        return render_template('index.html', cafes=cafes)
    
    @app.route('/add', methods=["GET", "POST"])
    def add():
        form = AddCafe()

        if request.method == 'POST':

            # Format map_url
            map_url = form.map_url.data
            map_url = map_url.split('"')[1]

            # Format times
            opening_hour_str = request.form['opening_hour']  # Get the string representation of the time
            opening_hour = datetime.strptime(opening_hour_str, '%H:%M')  # Convert the string to a time object

            closing_hour_str = request.form['closing_hour']  # Get the string representation of the time
            closing_hour = datetime.strptime(closing_hour_str, '%H:%M')  # Convert the string to a time object

            # Format Booleans
            pet_friendly = request.form.get("pet_friendly", False)
            electric_outlets = request.form.get("electric_outlets", False)

            booleans = [value if value != 'y' else True for value in [pet_friendly, electric_outlets]]


            # # Print every element to data types
            # for field_name, field in form._fields.items():
            #             field_data = getattr(form, field_name).data
            #             print(f'{field_name} -- {field_data} -- {type(field_data)}')
            
            cafe = Cafes(
                name=request.form["name"],
                image=request.form["image_url"],
                location=map_url,
                opening_hour=opening_hour,
                closing_hour=closing_hour,
                wifi=request.form["wifi"],
                noise=request.form["noise"],
                pet_friendly=booleans[0],
                electric_outlets=booleans[1],
            )

            db.session.add(cafe)
            db.session.commit()

            # Delete all records from the Cafes db
            # Cafes.query.delete()
            # db.session.commit()

            return redirect(url_for('index'))

        return render_template('add.html', form=form)


