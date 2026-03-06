from datetime import datetime
from volunteerTracker import Volunteer

class MonthlyReport:
  """ Generates a volunteer report for a requested month. """

  @staticmethod
  def generate(month: int, year: int)
    volunteers = Volunteer.getAllVolunteers()

    report = {
      "month": month,
      "year": year,
      "total_hours": 0,
      "volunteer_count": 0,
      "details": []
    }

    for volunteer in volunteers:
      monthly_hours = 0

       for record in volunteer.hours:
          date = datetime.strptime(record["date"], "%Y-%m-%d")

          if date.month == month and date.year == year:
            monthly_hours += record["hours"]

        if monthly_hours > 0:
          report["volunteer_count"] += 1
          report["total_hours] += monthly_hours

          report["details"].append({
            "name": volunteer.name,
            "hours": monthly_hours
          })

      return report

if __name__ == "__main__":
  month = int(input("Enter month (1-12): "))
  year = int(input("Enter year: "))

  report = MonthlyReport.generate(month, year)

  print("\nMonthly Volunteer Report")
  print("-------------------------")
  print(f"Month: {report["month"]} Year: {report["year"]}")
  print(f"Total Volunteers: {report["total_hours"]}")
  print(f"Total Hours: {report["total_hours"]}\n")

  for v in report["details"]:
    print(f"{v["name"]} - {v["hours"]} hours")
    

