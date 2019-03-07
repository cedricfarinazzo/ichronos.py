import requests
from icalendar import Calendar, Event
from datetime import datetime
from models import *

def get_lessons(url, ext=".ics"):
	url = url + ext
	r = requests.get(url)
	lessons = []
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
				lessons.append(lesson)
		return lessons
	return None
			
def parse(lessons):
	lessons.sort()
	if lessons == []:
		return []
	
	sday = ""
	day = None
	weeks = []
	week_cur = 0
	weeks.append(Week(lessons[0].dtstart.isocalendar()[1]))
	
	for c in lessons:
		if c.dtstart.isocalendar()[1] != weeks[week_cur].week:
			if day is not None:
				weeks[week_cur].add_day(day)
			sday = c.get_day()
			day = Day(sday)
			week_cur += 1
			weeks.append(Week(c.dtstart.isocalendar()[1]))
		if sday != c.get_day():
			if day is not None:
				weeks[week_cur].add_day(day)
			sday = c.get_day()
			day = Day(sday)
		day.add_lesson(c)

	return weeks
	
def get_current_week(group):
	url = 'https://ichronos.net/feed/' + group
	lessons = get_lessons(url)
	if lessons is None:
		pass
	return parse(lessons)
	
def get_custom_week(group, week):
	url = 'https://ichronos.net/ics/' + group  + '/' + week
	lessons = get_lessons(url)
	if lessons is None:
		pass
	return parse(lessons)




	
