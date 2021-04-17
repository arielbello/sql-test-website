from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email as EmailValidator
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), EmailValidator()],
                       render_kw={"placeholder": "enter your email"})
    submit = SubmitField("Start Test")
