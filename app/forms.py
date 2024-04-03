from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL

class AddCafe(FlaskForm):
    name =  StringField('Name', validators=[DataRequired()])
    image_url = StringField('Image', validators=[DataRequired(), URL()])
    map_url = StringField('Google Maps Link', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')
