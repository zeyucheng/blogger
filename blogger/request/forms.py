from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class RequestForm(FlaskForm):
    user_photo = FileField('Plz share your whole body picture with your favorite cloth to us!!!',
                           validators=[FileAllowed(['jpg', 'png'])])
    content = TextAreaField('Talk about your style and your favorite cloth brand', validators=[DataRequired()])
    price = StringField('How much do you want to spend on the suit?', validators=[DataRequired()])
    submit = SubmitField('Send request')
