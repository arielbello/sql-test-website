from flask import redirect
from flask import Blueprint, request, render_template, session, url_for
from email_validator import validate_email, EmailNotValidError
from .query_controller import run_query
from .forms import SqlForm
from .server_db import write_entry
import pandas as pd


sqltest = Blueprint("sqltest", __name__)


def render_run(result, accepted, success):
    if success:
        return test_index(result=result, accepted=accepted)
    else:
        return test_index(errormsg=result, accepted=accepted)


def render_submit(query, accepted, exec_time):
    success = write_entry(query=query, email=session.get("email"),
                          accepted=accepted, exec_time=exec_time)
    if success:
        return test_index(submit=True)
    else:
        return test_index(errormsg="Unable to submit", submit=False)


@sqltest.route("/", methods=["POST"])
def submit_query():
    form = SqlForm()
    if not form.validate_on_submit():
        errormsg = form.sql.errors[0] if form.sql.errors else None
        return test_index(errormsg=errormsg)

    query = form.sql.data
    dbres = run_query(query)
    accepted = dbres.accepted
    if request.form.get("run"):
        return render_run(accepted=accepted, result=dbres.result,
                          success=dbres.successful)
    elif request.form.get("submit"):
        return render_submit(query, accepted, dbres.exec_time)


@sqltest.route("/", methods=["GET"])
def test_index(errormsg=None, result=None, submit=False, accepted=False):
    email = session.get("email")
    try:
        email = validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        print("attempting test with an invalid email:", email)
        return redirect(url_for("home.index"), 403)

    sql_form = SqlForm()
    has_rows = isinstance(result, pd.DataFrame)
    return render_template("sqltest.html", form=sql_form, errormsg=errormsg,
                           has_rows=has_rows, accepted=accepted,
                           result=result, submit=submit,
                           action=url_for("sqltest.submit_query"))
