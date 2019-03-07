import requests
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
import humanize

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
				
		print("    Current week")
		for c in week:
			print(c)
	else:
		print("Error")

	
if __name__ == '__main__':
	main()