from flask import Flask
from app.sql_test.sql_page import sqltest
from app.home.home_page import home
from app.routes import Routes
from app import config


def configure():
    if app.config["ENV"] == "production":
        app.config.from_object(config.Config)
    elif app.config["ENV"] == "test":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)


app = Flask(__name__)
configure()

app.register_blueprint(home, url_prefix=Routes.INDEX)
app.register_blueprint(sqltest, url_prefix=Routes.SQL_TEST)
