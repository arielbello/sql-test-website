from flask import Blueprint, request, render_template, session
from app.routes import Routes
from email_validator import validate_email
from email_validator import EmailNotValidError


sqltest = Blueprint("sqltest", __name__)


@sqltest.route("/")
def test_index():
    email = session.get("email")
    try:
        email = validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        print("attempting test with an invalid email:", email)
        return "400"

    # TODO validate email
    return render_template("sqltest.html")
