from report_generator import ReportGenerator

class AnnualReport(ReportGenerator):
    """Generates a summary report for a specific year."""
    def __init__(self, year: int, organization_name="Leadership Lafayette"):
        super().__init__(organization_name)
        self.year = year

    def generate_report(self, export=False):
        """Generates an annual report string and optionally exports to txt."""
        applicants = self.get_all_applicants()
        
        # Filter applicants by year
        annual_applicants = [
            a for a in applicants 
            if a.applied_on and a.applied_on.year == self.year
        ]

        total_applied = len(annual_applicants)
        accepted = len([a for a in annual_applicants if a.status == 'Accepted' or a.status == 'Approved'])
        declined = len([a for a in annual_applicants if a.status == 'Declined'])
        waitlisted = len([a for a in annual_applicants if a.status == 'Waitlisted'])
        
        acceptance_rate = (accepted / total_applied * 100) if total_applied > 0 else 0
        total_hours = self.get_total_volunteer_hours()

        report_str = f"=== {self.organization_name} Annual Report ===\n"
        report_str += f"Reporting Year: {self.year}\n"
        report_str += f"Total Applicants: {total_applied}\n"
        report_str += f"  - Accepted: {accepted}\n"
        report_str += f"  - Declined: {declined}\n"
        report_str += f"  - Waitlisted: {waitlisted}\n"
        report_str += f"Acceptance Rate: {acceptance_rate:.1f}%\n"
        report_str += f"Total Volunteer Hours Logged: {total_hours}\n"
        report_str += "==============================================="

        if export:
            filename = f"annual_report_{self.year}.txt"
            with open(filename, 'w') as f:
                f.write(report_str)
            print(f"Report exported to {filename}")

        return report_str

if __name__ == "__main__":
    from datetime import datetime
    now = datetime.now()
    report = AnnualReport(now.year)
    print(report.generate_report())
