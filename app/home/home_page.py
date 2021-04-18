from flask import Blueprint, url_for, redirect, request
from flask import render_template, session
from .forms import EmailForm


home = Blueprint("home", __name__)


def render_form(form):
    return render_template("index.html", form=form, action="/")


@home.route("/")
def index():
    form = EmailForm()
    return render_form(form)


@home.route("/", methods=["POST"])
def submit():
    form = EmailForm()
    if form.validate_on_submit():
        session["email"] = request.form.get("email")
        session["permanent"] = True
        return redirect(url_for("sqltest.test_index"))
    else:
        return render_form(form)
