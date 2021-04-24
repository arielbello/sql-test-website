from flask import redirect
from flask import Blueprint, request, render_template, session, url_for
from email_validator import validate_email, EmailNotValidError
from .query_controller import run_query, DbResponse
from .forms import SqlForm
from .server_db import write_entry
import pandas as pd


sqltest = Blueprint("sqltest", __name__)


def render_run(dbres: DbResponse):
    if dbres.successful:
        return test_index(result=dbres.result, row_count=dbres.count,
                          accepted=dbres.accepted)
    else:
        return test_index(errormsg=dbres.errormsg, accepted=dbres.accepted)


def render_submit(query: str, success: bool):
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
    if request.form.get("run"):
        return render_run(dbres)
    elif request.form.get("submit"):
        success = write_entry(query=query, email=session.get("email"),
                              accepted=dbres.accepted,
                              exec_time=dbres.exec_time)
        return render_submit(query, success)


@sqltest.route("/", methods=["GET"])
def test_index(errormsg=None, result=None, row_count=0,
               submit=False, accepted=False):
    email = session.get("email")
    try:
        email = validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        print("attempting test with an invalid email:", email)
        return redirect(url_for("home.index"), 403)

    sql_form = SqlForm()
    has_rows = isinstance(result, pd.DataFrame)
    rows_info = ""
    if has_rows and row_count > len(result):
        rows_info = f"""Displaying the first {len(result)} of
                    {row_count} results."""
    return render_template("sqltest.html", form=sql_form, errormsg=errormsg,
                           has_rows=has_rows, rows_info=rows_info,
                           accepted=accepted, result=result, submit=submit,
                           action=url_for("sqltest.submit_query"))
