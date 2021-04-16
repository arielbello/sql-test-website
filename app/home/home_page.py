from flask import Blueprint, url_for, redirect, request, render_template, session
from app.routes import Routes


home = Blueprint("home", __name__)


@home.route("/")
def index():
    from app.main import app
    return render_template("index.html", action=Routes.CHECK_EMAIL)


@home.route(Routes.CHECK_EMAIL, methods=["POST"])
def check_email():
    # TODO 
    session["email"] = request.form.get("email")
    session["permanent"] = True
    return redirect(Routes.SQL_TEST)
