import requests
from icalendar import Calendar, Event
from datetime import datetime

class Lesson:
	
	def __init__(self, matter, description, location, dtstart, dtend):
		self.matter = matter
		self.description = description
		self.location = location 
		self.dtstart = dtstart
		self.dtend = dtend
		
	def __str__(self):
		return str(self.matter) + " | " + str(self.location) + " | " + \
		self.dtstart.strftime('%d %b %Y : %H:%M') + " | " + self.dtend.strftime('%d %b %Y : %H:%M') + " | " + \
		str(self.description)
		
	def __eq__(self, other):
		"""Defines behavior for the equality operator, ==."""
		return self.get_date() == other.get_date()
		
	def __ne__(self, other):
		"""Defines behavior for the inequality operator, !=."""
		return not (self == other)
	
	def __lt__(self, other):
		"""Defines behavior for the less-than operator, <."""
		return self.dtstart < other.dtstart
		
	def __gt__(self, other):
		"""Defines behavior for the greater-than operator, >."""
		return self.dtstart > other.dtstart
		
	def __le__(self, other):
		"""Defines behavior for the less-than-or-equal-to operator, <=."""
		return (self < other) or (self == other)
	
	def __ge__(self, other):
		"""Defines behavior for the greater-than-or-equal-to operator, >=."""
		return (self > other) or (self == other)
		
	def get_day(self):
		return self.dtstart.strftime('%d %b %Y')

	def get_date(self):
		return self.dtstart.strftime('%d %b %Y : %H:%M')
		
def main():
	url = 'https://ichronos.net/feed/INFOS4A1-1.ics'
	r = requests.get(url)
	week = []
	if r.status_code == 200:
		text = r.text
		gcal = Calendar.from_ical(text)
		for component in gcal.walk():
			if component.name == "VEVENT":
				matter = component.get('summary')
				description = component.get('description')
				location = component.get('location')
				
				tsr = component.decoded('dtstart')
				te = component.decoded('dtend')
				lesson = Lesson(matter, description, location, tsr, te)
				week.append(lesson)
			
		week.sort()
		print("    Current week")
		day = ""
		for c in week:
			if day != c.get_day():
				day = c.get_day()
				print(" => " + day)
			print(c)
	else:
		print("Error")

	
if __name__ == '__main__':
	main()