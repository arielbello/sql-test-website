import datetime

class Config(object):
    APPLICATION_ROOT = '/'
    DEBUG = False
    ENV = 'production'
    EXPLAIN_TEMPLATE_LOADING = False
    JSONIFY_MIMETYPE = 'application/json'
    JSONIFY_PRETTYPRINT_REGULAR = False
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    MAX_CONTENT_LENGTH = None
    MAX_COOKIE_SIZE = 4093
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=31)
    PREFERRED_URL_SCHEME = 'http'
    PRESERVE_CONTEXT_ON_EXCEPTION = None
    PROPAGATE_EXCEPTIONS = None
    # TODO set a ke
    SECRET_KEY = '<secret_key>'
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
    DB_NAME = "<production-db>"
    DB_USERNAME = "<username>"
    DB_PASSWORD = "<password>"


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    DB_NAME = "<development-db>"
    DB_USERNAME = "<username>"
    DB_PASSWORD = "<password>"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    ENV = "test"
    DB_NAME = "<test-db>"
    DB_USERNAME = "<username>"
    DB_PASSWORD = "<password>"

    SESSION_COOKIE_SECURE = False