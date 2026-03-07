from report_generator import ReportGenerator
from datetime import datetime

class MonthlyReport(ReportGenerator):
    """Generates a summary report for a specific month and year."""
    def __init__(self, month: int, year: int, organization_name="Leadership Lafayette"):
        super().__init__(organization_name)
        self.month = month
        self.year = year

    def generate_report(self, export=False):
        """Generates a report string and optionally exports it to a text file."""
        applicants = self.get_all_applicants()
        
        # Filter applicants by month/year (assuming applied_on is accessible)
        monthly_applicants = [
            a for a in applicants 
            if a.applied_on and a.applied_on.month == self.month and a.applied_on.year == self.year
        ]

        total_applied = len(monthly_applicants)
        accepted = len([a for a in monthly_applicants if a.status == 'Accepted' or a.status == 'Approved'])
        
        # We can't track *monthly* hours easily from volunteerTracker since it just tracks total hours, 
        # so we will report on the *current total* hours as of this month.
        total_hours = self.get_total_volunteer_hours()

        report_str = f"--- {self.organization_name} Monthly Report ---\n"
        report_str += f"Reporting Period: {self.month}/{self.year}\n"
        report_str += f"Total New Applicants: {total_applied}\n"
        report_str += f"Applicants Accepted: {accepted}\n"
        report_str += f"Total Volunteer Hours Logged to Date: {total_hours}\n"
        report_str += "----------------------------------------------"

        if export:
            filename = f"monthly_report_{self.month}_{self.year}.txt"
            with open(filename, 'w') as f:
                f.write(report_str)
            print(f"Report exported to {filename}")

        return report_str

if __name__ == "__main__":
    now = datetime.now()
    report = MonthlyReport(now.month, now.year)
    print(report.generate_report())
