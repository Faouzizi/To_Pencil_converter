from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.widgets import TextArea

class image_path_forms(FlaskForm):
    path = TextField("path")
    submit = SubmitField("Send")