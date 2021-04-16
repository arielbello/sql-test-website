from app.routes import Routes
from email_validator import EmailNotValidError, validate_email
import pytest


@pytest.fixture
def response(client):
    return client.get(Routes.INDEX)


def test_valid_response(response):
    assert response.status_code == 200


def test_email_form(response):
    assert b"email" in response.data


def test_start_test(response):
    assert "start test" in str(response.data).lower()
    assert "submit" in str(response.data).lower()


def test_invalid_email(client, invalid_email):
    response = client.post(Routes.SUBMIT, data={"email": invalid_email})
    assert "start test" in str(response.data).lower()


@pytest.mark.skip(reason="no csrf token to try")
def test_valid_email(client, valid_email):
    pass