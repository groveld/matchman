import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "not-a-secret-key"
    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    # MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
