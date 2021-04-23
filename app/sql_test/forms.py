from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length


class SqlForm(FlaskForm):
    CHAR_LEN = 512
    length_msg = f"Query cannot be longer than {CHAR_LEN} characters"
    placeholder = "Write your query here.\nExample:\nSELECT * FROM Users"
    sql = TextAreaField("SQL Query",
                        validators=[InputRequired("Write your query"),
                                    Length(max=CHAR_LEN, message=length_msg)],
                        render_kw={"autofocus": True,
                                   "placeholder": placeholder})
    submit = SubmitField("Submit", _name="submit")
    run = SubmitField("Run", _name="run")
