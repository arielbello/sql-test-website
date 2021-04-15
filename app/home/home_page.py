from flask import Blueprint, request, render_template

home = Blueprint("home", __name__)
a_var = 10

@home.route("/")
def index():
    return render_template("index.html")
