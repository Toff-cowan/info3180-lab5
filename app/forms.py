# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField(
        "Movie Title",
        validators=[DataRequired(message="This field is required.")]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired(message="This field is required.")]
    )

    poster = FileField(
        "Photo Upload",
        validators=[
            FileRequired(message="This field is required."),
            FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")
        ]
    )