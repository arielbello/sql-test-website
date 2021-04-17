from flask import Blueprint, request, render_template, session, url_for
from app.routes import Routes
from email_validator import validate_email, EmailNotValidError
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired


sqltest = Blueprint("sqltest", __name__)


class SqlForm(FlaskForm):
    sql = TextAreaField("email", validators=[DataRequired()], 
        render_kw={"placeholder": "Write your query here"})
    submit = SubmitField("Submit", _name="submit")
    run = SubmitField("Run", _name="run")


@sqltest.route("/", methods=["POST"])
def submit_query():
    form = SqlForm()
    print("query submitted")
    if request.form.get("run"):
        print("running query")
    elif request.form.get("submit"):
        print("submitting query")
    return test_index()


@sqltest.route("/", methods=["GET"])
def test_index():
    email = session.get("email")
    try:
        email = validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        print("attempting test with an invalid email:", email)
        return "400"

    sql_form = SqlForm()
    return render_template("sqltest.html", form=sql_form, 
    action=url_for("sqltest.submit_query"))
