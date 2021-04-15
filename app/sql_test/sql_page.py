from flask import Blueprint, request, render_template

sqltest = Blueprint("sqltest", __name__)

@sqltest.route("/")
def index():
    return render_template("sqltest.html")
