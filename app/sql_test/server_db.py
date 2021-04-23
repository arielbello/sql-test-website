import sqlalchemy
from flask import current_app


_engine = None

def setup_engine():
    global _engine
    _engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgres+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL(
            drivername="postgresql+pg8000",
            username=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            host=current_app.config["DB_URL"],
            port=current_app.config["DB_PORT"],
            database=current_app.config["DB_NAME"]
        )
    )
    return _engine
