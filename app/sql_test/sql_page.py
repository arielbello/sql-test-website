from flask import Blueprint, request, render_template, session, url_for
from email_validator import validate_email, EmailNotValidError
from .forms import SqlForm


sqltest = Blueprint("sqltest", __name__)


@sqltest.route("/", methods=["POST"])
def submit_query():
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
