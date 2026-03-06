from datetime import datetime
from volunteerTracker import Volunteer

class AnnualReport:
  """ Generates an annual recap of volunteer activity """

  @staticmethod
  def generate(year: int):
    volunteers = Volunteer.getAllVolunteers()

    report = {
      "year": year,
      "total_hours": 0,
      "volunteer_count": 0,
      "details": []
    }

  for volunteer in volunteers:
    yearly_hours = 0

    for record in volunteer.hours:
      date = datetime.strptime(record["date"], "%Y-%m-%d")

      if date.year == year:
        yearly_hours += record["hours"]

    if yearly_hours > 0:
      report["volunteer_count"] += 1
      report["total_hours"] += yearly_hours

      report["details"].append({
        "name": volunteer.name,
        "hours": yearly.hours
      })
  return report

if __name__ == "__main__":
  year = int(input("Enter year: "))

  report = AnnualReport.generate(year)

  print("\nAnnual Volunteer Report")
  print("----------------------")
  print(f"Year: {report["year"]}")
  print(f"Total Volunteers: {report["volunteer_count"]}")
  print(f"Total Hours: {report["total_hours"]}\n")

  for v in report["details"]:
    print(f"{v["name"]} - {v["hours"]} hours")



