from flask import Flask
from app.sql_test.sql_page import sqltest
from app.home.home_page import home
from app.routes import Routes


app = Flask(__name__)

app.register_blueprint(home, url_prefix=Routes.INDEX)
app.register_blueprint(sqltest, url_prefix=Routes.SQL_TEST)
