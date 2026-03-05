import os
import sys
import pickle

# Setup paths to import models correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
applicant_tracker_dir = os.path.join(current_dir, 'applicant_tracker')
if applicant_tracker_dir not in sys.path:
    sys.path.insert(0, applicant_tracker_dir)

from app import app
from models import Applicant

class ReportGenerator:
    """
    Base class for generating reports. 
    Connects to both the applicant database and the volunteer tracker data.
    """
    def __init__(self, organization_name="Leadership Lafayette"):
        self.organization_name = organization_name
        self.app = app
        self.volunteers = []
        self._load_volunteer_data()

    def _load_volunteer_data(self):
        """Loads volunteer data from the serialized list in data.pkl"""
        data_path = os.path.join(os.path.dirname(__file__), "data.pkl")
        if os.path.exists(data_path):
            try:
                with open(data_path, 'rb') as file:
                    self.volunteers = pickle.load(file)
            except Exception as e:
                print(f"Error loading volunteer data: {e}")

    def get_total_volunteer_hours(self):
        """Calculates total hours across all volunteers."""
        return sum(v.hours for v in self.volunteers)

    def get_all_applicants(self):
        """Fetches all applicants from the database."""
        with self.app.app_context():
            return Applicant.query.all()

    def generate_report(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement generate_report()")
