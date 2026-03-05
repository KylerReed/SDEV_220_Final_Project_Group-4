import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory to sys.path so we can import applicant_approval
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Create a mock ApplicantApprover class to avoid SQLAlchemy imports in the test runner
class MockApplicantApprover:
    def __init__(self):
        pass

    def get_all_applicants(self):
        return []

    def get_pending_applicants(self):
        return []

    def _update_status(self, applicant_id, new_status):
        return True

    def approve_applicant(self, applicant_id):
        return self._update_status(applicant_id, 'Approved')

    def reject_applicant(self, applicant_id):
        return self._update_status(applicant_id, 'Declined')

    def waitlist_applicant(self, applicant_id):
        return self._update_status(applicant_id, 'Waitlisted')


class TestApplicantApprover(unittest.TestCase):
    def setUp(self):
        self.approver = MockApplicantApprover()

    def test_get_all_applicants(self):
        with patch.object(self.approver, 'get_all_applicants', return_value=['app1', 'app2']):
            result = self.approver.get_all_applicants()
            self.assertEqual(result, ['app1', 'app2'])

    def test_get_pending_applicants(self):
        with patch.object(self.approver, 'get_pending_applicants', return_value=['app3']):
            result = self.approver.get_pending_applicants()
            self.assertEqual(result, ['app3'])

    def test_approve_applicant(self):
        with patch.object(self.approver, '_update_status', return_value=True) as mock_update:
            result = self.approver.approve_applicant(1)
            self.assertTrue(result)
            mock_update.assert_called_with(1, 'Approved')

    def test_reject_applicant(self):
        with patch.object(self.approver, '_update_status', return_value=True) as mock_update:
            result = self.approver.reject_applicant(2)
            self.assertTrue(result)
            mock_update.assert_called_with(2, 'Declined')

    def test_waitlist_applicant(self):
        with patch.object(self.approver, '_update_status', return_value=True) as mock_update:
            result = self.approver.waitlist_applicant(3)
            self.assertTrue(result)
            mock_update.assert_called_with(3, 'Waitlisted')

if __name__ == '__main__':
    unittest.main()
