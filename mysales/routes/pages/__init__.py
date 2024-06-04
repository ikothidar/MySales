# Flask modules
from flask import Blueprint, render_template

# Blueprint modules
from .core import core_bp

pages_bp = Blueprint("pages", __name__, url_prefix="/")

pages_bp.register_blueprint(core_bp)


@pages_bp.route("/")
def index_route():
    return render_template("pages/index.html")
