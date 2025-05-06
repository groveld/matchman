from flask import Blueprint

main = Blueprint("main", __name__)

from matchman.main import routes  # noqa: E402, F401
