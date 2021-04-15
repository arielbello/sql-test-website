from app.routes import Routes
import pytest


@pytest.fixture
def response(client):
    return client.get(Routes.SQL_TEST)


def test_valid_response(response):
    assert response.status_code == 200


def test_has_multiline_form(response):
    assert b"form" in response.data