from flask import Flask


def create_app():
    """Application factory for creating the Flask app."""
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

    return app
