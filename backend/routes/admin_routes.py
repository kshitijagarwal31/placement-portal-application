from flask import Blueprint

admin_bp = Blueprint("admin_bp", __name__, url_prefix="/admin")

@admin_bp.route("/test")
def test():
    return "Admin Route Working"