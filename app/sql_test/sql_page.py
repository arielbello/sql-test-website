from flask import redirect
from flask import Blueprint, request, render_template, session, url_for
from email_validator import validate_email, EmailNotValidError
from .query_controller import run_query
from .forms import SqlForm
import pandas as pd


sqltest = Blueprint("sqltest", __name__)


def _write_to_db(query):
    # TODO write to postgres
    pass


@sqltest.route("/", methods=["POST"])
def submit_query():
    form = SqlForm()
    query = form.sql.data
    if not form.validate_on_submit():
        errormsg = form.sql.errors[0] if form.sql.errors else None
        return test_index(errormsg=errormsg)

    if request.form.get("run"):
        dbres = run_query(query)
        if dbres.successful:
            return test_index(result=dbres.result, accepted=dbres.accepted)
        else:
            return test_index(errormsg=dbres.result, accepted=dbres.accepted)
    elif request.form.get("submit"):
        _write_to_db(query)
        return test_index(submit=True)


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
