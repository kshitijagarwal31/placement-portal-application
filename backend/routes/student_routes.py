from flask import Blueprint

student_bp = Blueprint("student_bp", __name__, url_prefix="/student")

@student_bp.route("/test")
def test():
    return "Student Route Working"