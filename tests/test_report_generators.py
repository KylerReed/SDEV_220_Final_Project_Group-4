import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from monthly_report import MonthlyReport
from annual_report import AnnualReport

class DummyApplicant:
    def __init__(self, status, year, month):
        self.status = status
        self.applied_on = datetime(year, month, 1)

class TestReportGenerators(unittest.TestCase):

    @patch('report_generator.ReportGenerator._load_volunteer_data')
    @patch('report_generator.ReportGenerator.get_all_applicants')
    def test_monthly_report_generation(self, mock_get_applicants, mock_load_data):
        # Setup dummy data for month 5, year 2024
        app1 = DummyApplicant('Approved', 2024, 5)
        app2 = DummyApplicant('Pending', 2024, 5)
        app3 = DummyApplicant('Declined', 2024, 4) # Different month
        mock_get_applicants.return_value = [app1, app2, app3]

        report = MonthlyReport(5, 2024)
        
        # Mock volunteer hours
        report.volunteers = [MagicMock(hours=10), MagicMock(hours=15)]
        
        output = report.generate_report()
        
        self.assertIn("Reporting Period: 5/2024", output)
        self.assertIn("Total New Applicants: 2", output)
        self.assertIn("Applicants Accepted: 1", output)
        self.assertIn("Total Volunteer Hours Logged to Date: 25", output)

    @patch('report_generator.ReportGenerator._load_volunteer_data')
    @patch('report_generator.ReportGenerator.get_all_applicants')
    def test_annual_report_generation(self, mock_get_applicants, mock_load_data):
        # Setup dummy data for year 2023
        app1 = DummyApplicant('Approved', 2023, 1)
        app2 = DummyApplicant('Declined', 2023, 5)
        app3 = DummyApplicant('Waitlisted', 2023, 8)
        app4 = DummyApplicant('Approved', 2024, 1) # Different year
        mock_get_applicants.return_value = [app1, app2, app3, app4]

        report = AnnualReport(2023)
        
        # Mock volunteer hours
        report.volunteers = [MagicMock(hours=100), MagicMock(hours=50)]
        
        output = report.generate_report()
        
        self.assertIn("Reporting Year: 2023", output)
        self.assertIn("Total Applicants: 3", output)
        self.assertIn("Accepted: 1", output)
        self.assertIn("Declined: 1", output)
        self.assertIn("Waitlisted: 1", output)
        self.assertIn("Acceptance Rate: 33.3%", output)
        self.assertIn("Total Volunteer Hours Logged: 150", output)

if __name__ == '__main__':
    unittest.main()
