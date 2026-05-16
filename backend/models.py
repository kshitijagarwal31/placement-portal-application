from database import db
from flask_security import UserMixin, RoleMixin



class User(db.Model, UserMixin):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    fs_uniquifier = db.Column(db.String(250), unique=True, nullable=False)
    roles = db.relationship("Role", backref="users", secondary="user_role", lazy=True)
    
    company_profile = db.relationship("CompanyProfile", backref="user", lazy=True, uselist=False)
    student_profile = db.relationship("StudentProfile", backref="user", lazy=True, uselist=False)
    
    is_approved = db.Column(db.Boolean, default=False)
    
    
    
class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    
    
class UserRole(db.Model):
    __tablename__ = "user_role"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    
    
class CompanyProfile(db.Model):
    __tablename__ = "company_profile"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    industry = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    hr_contact_number = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text, nullable=False)
    website_link = db.Column(db.String(300), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    
class StudentProfile(db.Model):
    __tablename__ = "student_profile"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    college_name = db.Column(db.String(200), nullable=True)
    cgpa = db.Column(db.Float, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    resume = db.Column(db.String(300), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    
class PlacementDrive(db.Model):
    __tablename__ = "placement_drive"
    
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    job_title = db.Column(db.String(200), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(200), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    last_date = db.Column(db.Date, nullable=False)
    skills_required = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(200), default="Pending")
    is_approved = db.Column(db.Boolean, default=False)
    applications = db.relationship("Application", backref="placement_drive", lazy=True)
    company = db.relationship("User", backref="placement_drives", lazy=True)
    
    
class Application(db.Model):
    __tablename__ = "application"
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drive.id"), nullable=False)
    apply_date = db.Column(db.Date, default=db.func.current_date())
    status = db.Column(db.String(50), default="Pending")    
    student = db.relationship("User", backref="applications", lazy=True)
    
    interview_date = db.Column(db.DateTime, nullable=True) 
    interview_mode = db.Column(db.String(50)) 
    interview_location = db.Column(db.String(300), nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    offer_letter = db.Column(db.String(300), nullable=True)
    
    __table_args__ = (db.UniqueConstraint('student_id', 'drive_id', name='unique_application'),)
    

    