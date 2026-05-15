from flask import Blueprint

company_bp = Blueprint("company_bp", __name__, url_prefix="/company")

@company_bp.route("/test")
def test():
    return "Company Route Working"