from flask import Blueprint

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")

@auth_bp.route("/test")
def test():
    return "Auth Route Working"