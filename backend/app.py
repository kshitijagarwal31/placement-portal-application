from flask import Flask
from config import LocalDevelopmentConfig
from database import db

from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.student_routes import student_bp
from routes.company_routes import company_bp


def create_app():

    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(company_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)