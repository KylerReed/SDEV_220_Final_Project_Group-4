# SDEV 220 Group 4: Final Project 
## Volunteer & Alumni Management/Registration System 

### Client: Leadership Lafayette

### Project Scope and Details
The end goal of our System is to give Leadership Lafayette an easy-to-use and integrated system that tracks participant and application status, exports data to files for information storage, sets up scheduled events, sends out reminders, tracks volunteer hours, and generates summary reports for the organization.

The main purpose of the System is to track volunteer hours and create an event scheduling/notification system, along with a Participant Database with a reporting tool.

### Core Features
- Add new applicants with key details (name, email, phone, applied date).
- Update applicant status (Pending, Approved, Declined, Waitlisted).
- Track volunteer names and hours.
- Generate summary reports (monthly and annual) calculating volunteer hours and applicant acceptance rates.
- Export data to CSV/Text files for external use.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KylerReed/SDEV_220_Final_Project_Group-4.git
   cd SDEV_220_Final_Project_Group-4
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Running the Application:**
   Run the main Graphical User Interface (GUI), which also automatically starts the background web server for the Admin Login (Applicant Tracker):
   ```bash
   python main.py
   ```
   - Click **"Volunteer Hours"** to manage volunteer logging.
   - Click **"Admin Login"** to open the web browser and manage pending applications.

### Testing Instructions

We have built-in `unittest` suites to verify that the logic for approving applicants and calculating total reports works correctly without syntax or runtime errors.

To run the automated tests, ensure your virtual environment is activated and run:
```bash
python -m unittest discover tests
```

### New Modules Included
- `applicant_approval.py`: Logic module containing `ApplicantApprover` class for managing the database status of applicants.
- `report_generator.py`: Base OO class connecting the volunteer data and applicant data.
- `monthly_report.py`: Subclass generating reporting metrics for a specific month.
- `annual_report.py`: Subclass generating reporting metrics and acceptance rates for a given year.
