import datetime
import os


class Config(object):
    APPLICATION_ROOT = '/'
    DEBUG = False
    TEST_DB_FOLDER = 'assets/'
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        host = f'/cloudsql/{os.getenv("DB_HOST")}'
    else:
        host = '127.0.0.1'

    DB_HOST = host
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "<server-db-name>")
    TEST_DB_PATH = "assets/test.db"
    ENV = 'production'
    EXPLAIN_TEMPLATE_LOADING = False
    JSONIFY_MIMETYPE = 'application/json'
    JSONIFY_PRETTYPRINT_REGULAR = False
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    MAX_CONTENT_LENGTH = None
    MAX_COOKIE_SIZE = 4093
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=31)
    PREFERRED_URL_SCHEME = 'https'
    PRESERVE_CONTEXT_ON_EXCEPTION = None
    PROPAGATE_EXCEPTIONS = None
    # TODO set a key when deploying
    SECRET_KEY = os.getenv("SECRET_KEY", "<secret_key>")
    SEND_FILE_MAX_AGE_DEFAULT = datetime.timedelta(seconds=43200)
    SERVER_NAME = None
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_SAMESITE = None
    SESSION_COOKIE_SECURE = False
    SESSION_REFRESH_EACH_REQUEST = True
    TEMPLATES_AUTO_RELOAD = None
    TESTING = False
    TRAP_BAD_REQUEST_ERRORS = None
    TRAP_HTTP_EXCEPTIONS = False
    USE_X_SENDFILE = False


class ProductionConfig(Config):
    DB_USER = os.getenv("DB_USER", default="<db-user>")
    DB_PASSWORD = os.getenv("DB_PASSWORD", default="<password>")


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    DB_USER = os.getenv("DB_USER", default="<db-user>")
    DB_PASSWORD = os.getenv("DB_PASSWORD", default="<password>")

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    ENV = "test"
    DB_USER = os.getenv("DB_USER", default="<db-user>")
    DB_PASSWORD = os.getenv("DB_PASSWORD", default="<password>")

    SESSION_COOKIE_SECURE = False
