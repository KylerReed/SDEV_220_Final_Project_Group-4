"""
events.py 
Handles creation and management of events for the final project.
"""

from datetime import datetime

class Event:
  def __init__(self, title, date, location, description=""):
    self.title = title
    self.date = self._format_date(date)
    self.location = location
    self.description = description

  def _format_date(self, date_str):

    try:
      return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
      raise ValueError("Date must be in YYYY-MM-DD format")

  def __str__(self):

    return (
      f"Event: {self.title}\n"
      f"Date: {self.date.strftime("%Y-%m-%d")}\n"
      f"Location: {self.location}\n"
      f"Description: {self.description}\n"
    )


class EventManager:
  """Handles storing and managing events"""

  def __init__(self):
    self.events = []

  def add_event(self, title, date, location, description=""):
    """ Adds a new event """
    event = Event(title, date, location, description)
    self.events.append(event)
    print(f"Event '{title}' added successfully.")

  def lists_events(self):
    """ Displays all events """
    if not self.events:
      print("No events scheduled.")
      return

    for i, event in enumerate(self.events, start=1):
      print(f"\nEvent #{i}")
      print(event)

  def remove_event(self, title):
    """ Removes an Event """
    for event in self.events:
      if event.title.lower() == title.lower():
        return event
    return None
    
    
    
      
