from flask import Blueprint

competitions = Blueprint("competitions", __name__, template_folder="templates")

from matchman.competitions import routes  # noqa: E402, F401
