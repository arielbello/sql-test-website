from app.main import app
import pytest

print("conftest")

@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        with app.app_context():
            # context config
            pass
        yield client