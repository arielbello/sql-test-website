from app.routes import Routes
import pytest


@pytest.fixture
def response(client):
    return client.get(Routes.INDEX)


def test_valid_response(response):
    assert response.status_code == 200


def test_email_form(response):
    assert b"<form" in response.data
    # TODO must be valid email
    # assert form submit response



def test_start_test(response):
    assert "start test" in str(response.data).lower()

    