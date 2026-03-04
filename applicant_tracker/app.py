# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Applicant

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/update/<int:id>", methods=["GET", "POST"])     # Update applicant status
def update_applicant(id):
    applicant = Applicant.query.get_or_404(id)

    if request.method == "POST":
        applicant.status = request.form["status"]
        db.session.commit()
        return redirect(url_for("list_applicants"))

    return render_template("update_applicant.html", applicant=applicant)

@app.route("/add", methods=["GET", "POST"])     # Route to add a new applicant
def add_applicant():
    if request.method == "POST":
        new_applicant = Applicant(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            phone=request.form.get("phone"),
            applied_date=request.form.get("applied_date")
        )
        db.session.add(new_applicant)
        db.session.commit()
        return redirect(url_for("list_applicants"))
    return render_template("add_applicant.html")

@app.route("/edit/<int:applicant_id>", methods=["GET", "POST"])     # Route to edit an existing applicant's details
def edit_applicant(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)

    if request.method == "POST":
        applicant.first_name = request.form["first_name"]
        applicant.last_name = request.form["last_name"]
        applicant.email = request.form["email"]
        applicant.phone = request.form.get("phone")
        applicant.applied_date = request.form.get("applied_date")

        db.session.commit()
        return redirect(url_for("list_applicants"))

    return render_template("edit_applicant.html", applicant=applicant)

@app.route("/delete/<int:applicant_id>", methods=["POST", "GET"])       # Route to delete an applicant from the database
def delete_applicant(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)

    db.session.delete(applicant)
    db.session.commit()

    return redirect(url_for("list_applicants"))

@app.route("/")
def dashboard():
    total_applicants = Applicant.query.count()

    recent_applicants = Applicant.query.order_by(
        Applicant.applied_date.desc()
    ).limit(5).all()

    recent_count = len(recent_applicants)

    return render_template(
        "dashboard.html",
        total_applicants=total_applicants,
        recent_applicants=recent_applicants,
        recent_count=recent_count
    )
