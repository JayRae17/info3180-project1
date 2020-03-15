from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email


class addProfile(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Select Gender',choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    bio = TextAreaField('Biography', validators=[DataRequired()])

    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
