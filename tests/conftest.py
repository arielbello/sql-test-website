from app.main import app
import pytest


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        with app.app_context():
            # context config
            pass
        yield client


@pytest.fixture(scope="session")
def valid_email():
    return "test_user@sqltest.com"


@pytest.fixture(scope="session")
def invalid_email():
    return "--; DROP * FROM User"