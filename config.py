import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FIREBIRD_HOST = os.environ.get("FIREBIRD_HOST") or "localhost"
    FIREBIRD_PORT = int(os.environ.get("FIREBIRD_PORT") or 3050)
    FIREBIRD_DATABASE = os.environ.get("FIREBIRD_DATABASE")
    FIREBIRD_USER = os.environ.get("FIREBIRD_USER") or "SYSDBA"
    FIREBIRD_PASSWORD = os.environ.get("FIREBIRD_PASSWORD") or "masterkey"
    FIREBIRD_CHARSET = os.environ.get("FIREBIRD_CHARSET") or "UTF8"

    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    # MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
