"""Initialize the Flask application."""

from flask import Flask

from matchman.config import Config


def create_app(config_class: object = Config) -> Flask:
    """Initialize and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    initialize_extensions(app)
    configure_logging(app)
    register_error_handlers(app)
    return app


def register_blueprints(app):
    from matchman.competitions import competitions
    from matchman.edit import edit
    from matchman.main import main

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(competitions, url_prefix="/competitions")
    app.register_blueprint(edit, url_prefix="/edit")


def initialize_extensions(app):
    pass


def configure_logging(app):
    pass


def register_error_handlers(app):
    pass
