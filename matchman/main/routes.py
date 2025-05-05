from flask import render_template

from matchman.main import main


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")
