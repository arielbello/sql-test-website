from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SqlForm(FlaskForm):
    sql = TextAreaField("SQL Query", validators=[])
    submit = SubmitField("Submit", _name="submit")
    run = SubmitField("Run", _name="run")
