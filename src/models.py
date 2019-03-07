#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

class Week:
	
	def __init__(self, week, nocolor=False):
		self.days = []
		self.week = week
		self.nocolor = nocolor
		
	def __str__(self):
		CYAN = "" if self.nocolor else Fore.CYAN
		out = CYAN + " ---- Week N°%d ---- " %(self.week) + Style.RESET_ALL + "\n\n"
		for d in self.days:
			out += str(d) + "\n\n"
		return out
		
	def add_day(self, day):
		self.days.append(day)

class Day:

	def __init__(self, day, nocolor=False):
		self.lessons = []
		self.day = day
		self.nocolor = nocolor
		
	def __str__(self):
		YEL = "" if self.nocolor else Fore.YELLOW
		out = YEL + " => %s " %(self.day) + Style.RESET_ALL + "\n"
		for l in self.lessons:
			out += str(l) + "\n"
		return out
		
	def add_lesson(self, lesson):
		self.lessons.append(lesson)
	

class Lesson:
	
	def __init__(self, matter, description, location, dtstart, dtend, nocolor=False):
		self.matter = matter
		self.description = description
		self.location = location
		self.dtstart = dtstart
		self.dtend = dtend
		self.nocolor = nocolor
		
	def __str__(self):
		GRN = "" if self.nocolor else Fore.GREEN
		RED = "" if self.nocolor else Fore.RED
		return "- " + GRN + str(self.matter) + Style.RESET_ALL + \
		" | " + RED + str(self.location) + Style.RESET_ALL + \
		" | " + self.dtstart.strftime('%d %b %Y : %H:%M') + \
		" -> " + self.dtend.strftime('%d %b %Y : %H:%M') + \
		" | " + str(self.description)
		
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
		