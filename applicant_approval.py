import os
import sys

# Add applicant_tracker to sys.path to allow importing models
current_dir = os.path.dirname(os.path.abspath(__file__))
applicant_tracker_dir = os.path.join(current_dir, 'applicant_tracker')
if applicant_tracker_dir not in sys.path:
    sys.path.insert(0, applicant_tracker_dir)

from app import app
from models import db, Applicant

class ApplicantApprover:
    """
    Class responsible for managing applicant statuses.
    Connects to the applicant_tracker database.
    """
    def __init__(self):
        self.app = app
        
    def get_all_applicants(self):
        """Returns a list of all applicants in the database."""
        with self.app.app_context():
            return Applicant.query.all()

    def get_pending_applicants(self):
        """Returns a list of applicants with 'Pending' status."""
        with self.app.app_context():
            return Applicant.query.filter_by(status='Pending').all()

    def _update_status(self, applicant_id, new_status):
        """Helper method to update an applicant's status."""
        with self.app.app_context():
            applicant = Applicant.query.get(applicant_id)
            if applicant:
                applicant.status = new_status
                db.session.commit()
                return True
            return False

    def approve_applicant(self, applicant_id):
        """Changes applicant status to 'Approved'."""
        return self._update_status(applicant_id, 'Approved')

    def reject_applicant(self, applicant_id):
        """Changes applicant status to 'Declined'."""
        return self._update_status(applicant_id, 'Declined')

    def waitlist_applicant(self, applicant_id):
        """Changes applicant status to 'Waitlisted'."""
        return self._update_status(applicant_id, 'Waitlisted')

if __name__ == "__main__":
    # Example usage
    approver = ApplicantApprover()
    applicants = approver.get_all_applicants()
    print(f"Total applicants: {len(applicants)}")
