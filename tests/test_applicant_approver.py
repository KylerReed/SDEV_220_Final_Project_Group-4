import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory to sys.path so we can import applicant_approval
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the real ApplicantApprover implementation
from applicant_approval import ApplicantApprover


class TestApplicantApprover(unittest.TestCase):
    def setUp(self):
        self.approver = ApplicantApprover()

    def test_get_all_applicants(self):
        # Mock Applicant.query.all() to return a known list
        with patch('applicant_approval.Applicant') as MockApplicant:
            mock_query = MagicMock()
            MockApplicant.query = mock_query
            mock_query.all.return_value = ['app1', 'app2']

            result = self.approver.get_all_applicants()

            self.assertEqual(result, ['app1', 'app2'])
            mock_query.all.assert_called_once()

    def test_get_pending_applicants(self):
        # Mock Applicant.query.filter_by(status='Pending').all()
        with patch('applicant_approval.Applicant') as MockApplicant:
            mock_query = MagicMock()
            MockApplicant.query = mock_query
            mock_filtered = MagicMock()
            mock_query.filter_by.return_value = mock_filtered
            mock_filtered.all.return_value = ['app3']

            result = self.approver.get_pending_applicants()

            self.assertEqual(result, ['app3'])
            mock_query.filter_by.assert_called_once_with(status='Pending')
            mock_filtered.all.assert_called_once()

    def test_approve_applicant(self):
        # Mock Applicant.query.get() and db.session.commit()
        with patch('applicant_approval.Applicant') as MockApplicant, \
             patch('applicant_approval.db') as mock_db:
            mock_applicant_instance = MagicMock()
            MockApplicant.query.get.return_value = mock_applicant_instance

            result = self.approver.approve_applicant(1)

            self.assertTrue(result)
            MockApplicant.query.get.assert_called_once_with(1)
            self.assertEqual(mock_applicant_instance.status, 'Approved')
            mock_db.session.commit.assert_called_once()

    def test_reject_applicant(self):
        # Mock Applicant.query.get() and db.session.commit()
        with patch('applicant_approval.Applicant') as MockApplicant, \
             patch('applicant_approval.db') as mock_db:
            mock_applicant_instance = MagicMock()
            MockApplicant.query.get.return_value = mock_applicant_instance

            result = self.approver.reject_applicant(2)

            self.assertTrue(result)
            MockApplicant.query.get.assert_called_once_with(2)
            self.assertEqual(mock_applicant_instance.status, 'Declined')
            mock_db.session.commit.assert_called_once()

    def test_waitlist_applicant(self):
        # Mock Applicant.query.get() and db.session.commit()
        with patch('applicant_approval.Applicant') as MockApplicant, \
             patch('applicant_approval.db') as mock_db:
            mock_applicant_instance = MagicMock()
            MockApplicant.query.get.return_value = mock_applicant_instance

            result = self.approver.waitlist_applicant(3)

            self.assertTrue(result)
            MockApplicant.query.get.assert_called_once_with(3)
            self.assertEqual(mock_applicant_instance.status, 'Waitlisted')
            mock_db.session.commit.assert_called_once()
if __name__ == '__main__':
    unittest.main()
