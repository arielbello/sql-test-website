from flask import Blueprint, url_for, redirect, request, render_template, session
from app.routes import Routes
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields import SubmitField
from wtforms.validators import Email as EmailValidator
from wtforms.validators import DataRequired


home = Blueprint("home", __name__)


class EmailForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), EmailValidator()], 
        render_kw={"placeholder": "enter your email"})
    submit = SubmitField("Start Test")


def render_form(form):
    return render_template("index.html", form=form, action=Routes.SUBMIT)


@home.route("/")
def index():
    form = EmailForm()
    return render_form(form)


@home.route(Routes.SUBMIT, methods=["POST"])
def submit():
    # TODO 
    form = EmailForm()
    
    if form.validate_on_submit():
        session["email"] = request.form.get("email")
        session["permanent"] = True
        return redirect(Routes.SQL_TEST)
    else:
        print(form.errors)
        return render_form(form)
