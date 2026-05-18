from flask import Blueprint, request, make_response, jsonify 
from flask_security import auth_required, roles_required 
from user_datastore import user_datastore 
from database import db 
from models import User, Role, StudentProfile, CompanyProfile, PlacementDrive, Application

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/admin/dashboard_data", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_dashboard_data():

    stats = {
        "total_students": User.query.join(User.roles).filter(Role.name == "student").count(),
        "total_companies": User.query.join(User.roles).filter(Role.name == "company").count(),
        "total_placement_drives": PlacementDrive.query.count(),
        "total_applications": Application.query.count()
    }

    students = User.query.join(User.roles).filter(Role.name == "student").all()
    students_list = [
        {
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "is_active": s.is_active
        } for s in students
    ]

    companies = User.query.join(User.roles).filter(
        Role.name == "company",
        User.is_approved == True
    ).all()
    companies_list = [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "is_active": c.is_active
        } for c in companies
    ]

    company_requests = User.query.join(User.roles).filter(
        Role.name == "company",
        User.is_approved == False
    ).all()
    company_requests_list = [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email
        } for c in company_requests
    ]

    placement_drives = PlacementDrive.query.filter_by(status="Active").all()
    drives_list = [
        {
            "id": d.id,
            "job_title": d.job_title,
            "company_name": d.company.name if d.company else "N/A",
            "start_date": str(d.start_date),
            "end_date": str(d.last_date)
        } for d in placement_drives
    ]

    closed_drives = PlacementDrive.query.filter_by(status="Closed").all()
    closed_drives_list = [
        {
            "id": d.id,
            "job_title": d.job_title,
            "company_name": d.company.name if d.company else "N/A",
            "start_date": str(d.start_date),
            "end_date": str(d.last_date)
        } for d in closed_drives
    ]

    drive_requests = PlacementDrive.query.filter_by(status="Pending").all()
    drive_requests_list = [
        {
            "id": d.id,
            "job_title": d.job_title,
            "company_name": d.company.name if d.company else "N/A",
            "start_date": str(d.start_date),
            "end_date": str(d.last_date)
        } for d in drive_requests
    ]

    applications = Application.query.all()
    applications_list = [
        {
            "id": a.id,
            "student_name": a.student.name if a.student else "N/A",
            "drive": a.placement_drive.job_title if a.placement_drive else "N/A",
            "company_name": a.placement_drive.company.name if a.placement_drive and a.placement_drive.company else "N/A",
            "status": a.status or "Pending",
            "apply_date": str(a.apply_date)
        } for a in applications
    ]

    return jsonify({
        "stats": stats,
        "students": students_list,
        "companies": companies_list,
        "company_requests": company_requests_list,
        "placement_drives": drives_list,
        "closed_drives": closed_drives_list,
        "drive_requests": drive_requests_list,
        "applications": applications_list
    })
    
    
@admin_bp.route("/admin/company/approve/<int:id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def approve_company(id):
    company = User.query.join(User.roles).filter(
        User.id == id,
        Role.name == "company"
    ).first()
    if not company:
        return {"message": "Company not found"}, 404
    company.is_approved = True
    db.session.commit()    
    return {"message": "Company approved successfully"}, 200


@admin_bp.route("/admin/company/reject/<int:id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def reject_company(id):
    company = User.query.get(id)
    if not company:
        return {"message": "Company not found"}, 404
    db.session.delete(company)
    db.session.commit()
    return {"message": "Company rejected and deleted"}, 200


@admin_bp.route("/admin/company/blacklist/<int:company_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def blacklist_company(company_id):
    user = User.query.get(company_id)
    if not user:
        return jsonify({"message": "Company not found"}), 404
    user.active = False
    company = CompanyProfile.query.filter_by(user_id=company_id).first()
    if company:
        company.is_active = False
    db.session.commit()
    return jsonify({"message": "Company blacklisted ✅"})


@admin_bp.route("/admin/company/unblacklist/<int:company_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def unblacklist_company(company_id):
    user = User.query.get(company_id)
    if not user:
        return jsonify({"message": "Company not found"}), 404
    user.active = True
    company = CompanyProfile.query.filter_by(user_id=company_id).first()
    if company:
        company.is_active = True
    db.session.commit()
    return jsonify({"message": "Company unblacklisted ✅"})


@admin_bp.route("/admin/student/blacklist/<int:student_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def blacklist_student(student_id):
    user = User.query.get(student_id)
    if not user:
        return jsonify({"message": "Student not found"}), 404
        
    user.active = False
        
    student = StudentProfile.query.filter_by(user_id=student_id).first()
    if student:
        student.is_active = False
        
    db.session.commit()
    return jsonify({"message": "Student blacklisted ✅"})


@admin_bp.route("/admin/student/unblacklist/<int:student_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def unblacklist_student(student_id):
    user = User.query.get(student_id)
    if not user:
        return jsonify({"message": "Student not found"}), 404
        
    user.active = True
        
    student = StudentProfile.query.filter_by(user_id=student_id).first()
    if student:
        student.is_active = True
        
    db.session.commit()
    return jsonify({"message": "Student unblacklisted ✅"})


@admin_bp.route("/admin/placement_drive/approve/<int:drive_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def approve_drive(drive_id):
    drive = PlacementDrive.query.get(drive_id)
    if not drive:
        return jsonify({"message": "Drive not found"}), 404
    drive.status = "Active"    
    drive.is_approved = True
    db.session.commit()
    return jsonify({"message": f"Drive approved ✅"})


@admin_bp.route("/admin/placement_drive/reject/<int:drive_id>", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def reject_drive(drive_id):
    drive = PlacementDrive.query.get(drive_id)
    if not drive:
        return jsonify({"message": "Drive not found"}), 404
    drive.status = "Rejected"
    db.session.commit()
    return jsonify({"message": f"Drive rejected ✅"})


@admin_bp.route("/admin/company_detail/<int:company_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_company_detail(company_id):
    company = User.query.get(company_id)
    if not company:
        return jsonify({"message": "Company not found"}), 404

    profile = CompanyProfile.query.filter_by(user_id=company_id).first()
    drives = PlacementDrive.query.filter_by(company_id=company_id).all()

    total  = len(drives)
    active = sum(1 for d in drives if d.status == "Active")
    closed = sum(1 for d in drives if d.status == "Closed")

    return jsonify({
        "name"       : company.name,
        "email"      : company.email,
        "is_active"  : company.is_active,
        "industry"   : profile.industry if profile else "N/A",
        "description": profile.description if profile else "N/A",
        "contact"    : profile.hr_contact_number if profile else "N/A",
        "address"    : profile.address if profile else "N/A",
        "website_link": profile.website_link if profile else "N/A",
        "stats": {
            "total_drives" : total,
            "active_drives": active,
            "closed_drives": closed
        },
        "drives": [
            {
                "id"        : d.id,
                "job_title" : d.job_title,
                "start_date": str(d.start_date),
                "end_date"  : str(d.last_date),
                "status"    : d.status
            } for d in drives
        ]
    })
    
    
@admin_bp.route("/admin/student_detail/<int:student_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_student_detail(student_id):
    student = User.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    profile = student.student_profile
    applications = student.applications

    total = len(applications)
    shortlisted = sum(1 for a in applications if a.status == "Shortlisted")
    rejected = sum(1 for a in applications if a.status == "Rejected")

    return jsonify({
        "name": student.name,
        "email": student.email,
        "college_name": profile.college_name if profile else "N/A",
        "cgpa": profile.cgpa if profile else "N/A",
        "skills": profile.skills if profile else "N/A",
        "bio": profile.bio if profile else "N/A",
        "is_active": student.active,
        "stats": {
            "total": total,
            "shortlisted": shortlisted,
            "rejected": rejected
        },
        "applications": [
            {
                "id": a.id,
                "drive": a.placement_drive.job_title if a.placement_drive else "N/A",
                "company": a.placement_drive.company.name if a.placement_drive and a.placement_drive.company else "N/A",
                "date": str(a.apply_date),
                "status": a.status
            } for a in applications
        ]
    })
    
    
@admin_bp.route("/admin/drive_detail/<int:drive_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_drive_detail(drive_id):
    drive = PlacementDrive.query.get(drive_id)
    if not drive:
        return jsonify({"message": "Drive not found"}), 404

    apps = drive.applications
    return jsonify({
        "job_title"         : drive.job_title,
        "company"           : drive.company.name if drive.company else "N/A",
        "salary"            : drive.salary,
        "start_date"        : str(drive.start_date),
        "end_date"          : str(drive.last_date),
        "skills_required"   : drive.skills_required,
        "status"            : drive.status,
        "description"       : drive.job_description,
        "total_applications": len(apps),
        "shortlisted"       : len([a for a in apps if a.status == "Shortlisted"]),
        "selected"          : len([a for a in apps if a.status == "Selected"]),
        "rejected"          : len([a for a in apps if a.status == "Rejected"]),
        "applications"      : [
            {
                "id"          : a.id,
                "student_name": a.student.name if a.student else "N/A",
                "apply_date"  : str(a.apply_date),
                "status"      : a.status
            } for a in apps
        ]
    })
    
    
@admin_bp.route("/admin/application_detail/<int:app_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_application_detail(app_id):
    app_data = Application.query.get(app_id)
    if not app_data:
        return jsonify({"message": "Application not found"}), 404

    drive = app_data.placement_drive
    return jsonify({
        "id"            : app_data.id,
        "status"        : app_data.status,
        "apply_date"    : str(app_data.apply_date),
        "interview_date": str(app_data.interview_date) if app_data.interview_date else "",
        "interview_mode": app_data.interview_mode or "N/A",
        "interview_location": app_data.interview_location or "",
        "feedback"      : app_data.feedback or "N/A",
        "offer_letter"  : app_data.offer_letter or "",
        "resume": app_data.student.student_profile.resume if app_data.student and app_data.student.student_profile else "",
        "job_title"     : drive.job_title if drive else "N/A",
        "company"       : drive.company.name if drive and drive.company else "N/A",
        "salary"        : drive.salary if drive else "N/A",
        "skills_required": drive.skills_required if drive else "N/A",
        "description"   : drive.job_description if drive else "N/A",
        "start_date"    : str(drive.start_date) if drive else "",
        "end_date"      : str(drive.last_date) if drive else ""
    })