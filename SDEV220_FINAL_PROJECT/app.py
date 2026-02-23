from flask import Flask, render_template, request, redirect, url_for
from models import db, Applicant

app = Flask(__name__)       # Initialize the database and create the tables
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)        # Create the database tables if they don't exist

with app.app_context():
    db.create_all()

@app.route("/add", methods=["GET", "POST"])     # Route to add a new applicant
def add_applicant():                            # If the request method is POST, retrieve the form data for the applicant's full name, email, and phone number. Create a new Applicant instance with this
    if request.method == "POST":                # data, add it to the database session, and commit the session to save the new applicant to the database. After adding the new applicant, redirect to the
        name = request.form["full_name"]        # list of applicants. If the request method is GET, render the form template to add a new applicant.
        email = request.form["email"]
        phone = request.form["phone"]

        new_applicant = Applicant(full_name=name, email=email, phone=phone) # Create a new applicant instance with the form data
        db.session.add(new_applicant)
        db.session.commit()

        return redirect(url_for("list_applicants")) # Redirect to the list of applicants after adding a new one

    return render_template("add_applicant.html")    # Render the form to add a new applicant when the request method is GET

@app.route("/")     # Route to list all applicants
def list_applicants():      # Query the database for all applicants, ordered by the date they applied (most recent first)
    applicants = Applicant.query.order_by(Applicant.applied_on.desc()).all()
    return render_template("list_applicants.html", applicants=applicants)   # Render the template to display the list of applicants, passing the applicants data to the template

@app.route("/update/<int:id>", methods=["POST"])    # Route to update the status of an applicant, identified by their ID. The new status is sent via a POST request from the form in the list of applicants.
def update_applicant(id):                           # Retrieve the applicant from the database using the provided ID. If the applicant does not exist, return a 404 error. Update the applicant's status
    applicant = Applicant.query.get_or_404(id)      # with the new value from the form and commit the changes to the database. Finally, redirect back to the list of applicants.
    applicant.status = request.form["status"]
    db.session.commit()
    return redirect(url_for("list_applicants"))     # Redirect to the list of applicants after updating the status
