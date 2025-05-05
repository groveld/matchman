from flask import Blueprint

edit = Blueprint("edit", __name__, template_folder="templates")

from matchman.edit import routes  # noqa: E402, F401
