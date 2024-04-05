# Import SQLAlchemy's 'db' object from the 'app' package
from app import db

# Define a SQLAlchemy model class named 'Cafes'
class Cafes(db.Model):
    # Specify the name of the database table associated with this model
    __tablename__ = 'cafes'

    # Define columns for the 'cafes' table
    cafe_id = db.Column(db.Integer, primary_key=True)  # Primary key column for cafe ID
    name = db.Column(db.String(250), nullable=False)  # Column for cafe name (max length: 250 characters)
    map_url = db.Column(db.String(500), nullable=False)     # Column for cafe location (text field)
    image_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    opening_hour = db.Column(db.DateTime, nullable=False)
    closing_hour = db.Column(db.DateTime, nullable=False)
    wifi = db.Column(db.String(10))
    noise = db.Column(db.String(10))
    pet_friendly = db.Column(db.Boolean)
    electric_outlets = db.Column(db.Boolean)

    # Define a special method '__repr__' to represent the object as a string
    def __repr__(self):
        # Return a formatted string representing the object's name and location
        return f'Cafe with name {self.name} located in {self.location}'
    
    # Dont forget to flask db upgrade and flask db migrate if changes on Model are made


