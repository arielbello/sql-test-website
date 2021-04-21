from flask import Flask
from flask_bootstrap import Bootstrap
import config
from home.home_page import home
from routes import Routes
from sql_test.sql_page import sqltest


def configure():
    if app.config["ENV"] == "production":
        app.config.from_object(config.ProductionConfig)
    elif app.config["ENV"] == "test":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)


app = Flask(__name__)
configure()
Bootstrap(app)

app.register_blueprint(home, url_prefix=Routes.INDEX)
app.register_blueprint(sqltest, url_prefix=Routes.SQL_TEST)
