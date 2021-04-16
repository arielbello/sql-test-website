from app.routes import Routes
from flask import session
import pytest


@pytest.fixture
def response(flask_app, valid_email):
    with flask_app.test_client() as client:
        yield client.get(Routes.SQL_TEST)


@pytest.mark.skip(reason="unable to access current session")
def test_valid_email(response):
    assert response.status_code == 200


def test_invalid_email(client):
    response = client.get(Routes.SQL_TEST)
    assert response.status_code != 200


def test_has_multiline_form(response):
    assert b"form" in response.data


def test_has_schema(response):
    assert b"schema" in response.data


def test_has_question(response):
    assert b"question" in response.data


@pytest.mark.skip(reason="too involved to test")
def test_multiple_users(client):
    pass
    # TODO multiple users doing the test at the same time


def test_run_query(client):
    assert "execute" in str(response.data).lower()
    # TODO show query results for valid queries
    # TODO show query errors for invalid queries
    # TODO info on query match
    # TODO test user has only read access to the db test tables
    # TODO prevent SQL injection


def test_submit(client):
    assert "submit" in str(response.data).lower()
    # TODO mock user and test database response
    # TODO check send user reference (email), execution time, query string, correct answer
    # TODO prevent SQL injection
    # TODO check confirmation message
