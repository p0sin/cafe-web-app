from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, BooleanField, TimeField
from wtforms.validators import DataRequired, URL

class AddCafe(FlaskForm):
    name =  StringField('Name', validators=[DataRequired()])
    image_url = StringField('Image', validators=[DataRequired(), URL()])
    map_url = StringField('Google Maps Link', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    opening_hour = TimeField('Opening Hour')
    closing_hour = TimeField('Closing Hour')
    wifi = SelectField(u'Wifi Connection', choices=[('low', 'Low'), ('high', 'High')])
    noise = SelectField(u'Noise Level', choices=[('low', 'Low'), ('high', 'High')])
    pet_friendly = BooleanField('Pet Friendly')
    electric_outlets = BooleanField('Electric Outlets')
    submit = SubmitField('Submit')
