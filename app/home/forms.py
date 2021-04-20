from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email as EmailValidator
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), EmailValidator()],
                       render_kw={"autofocus": True})
    submit = SubmitField("Start Test")
