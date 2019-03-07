from datetime import datetime

class Week:
	
	def __init__(self, week):
		self.days = []
		self.week = week
		
	def __str__(self):
		out = " ---- Week N°%d ---- " %(self.week) + "\n\n"
		for d in self.days:
			out += str(d) + "\n\n"
		return out
		
	def add_day(self, day):
		self.days.append(day)

class Day:

	def __init__(self, day):
		self.lessons = []
		self.day = day
		
	def __str__(self):
		out = " => %s " %(self.day) + "\n"
		for l in self.lessons:
			out += str(l) + "\n"
		return out
		
	def add_lesson(self, lesson):
		self.lessons.append(lesson)
	

class Lesson:
	
	def __init__(self, matter, description, location, dtstart, dtend):
		self.matter = matter
		self.description = description
		self.location = location 
		self.dtstart = dtstart
		self.dtend = dtend
		
	def __str__(self):
		return "- " + str(self.matter) + " | " + str(self.location) + " | " + \
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
		