from flask import Blueprint, request, render_template, session
from app.routes import Routes


sqltest = Blueprint("sqltest", __name__)


@sqltest.route("/")
def test_index():
    email = session.get("email")
    # TODO validate email
    return render_template("sqltest.html")
