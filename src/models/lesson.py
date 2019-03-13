#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

class Lesson:

    def __init__(self, matter, description, location, dtstart, dtend):
        self.matter = matter
        self.description = description
        self.location = location
        self.dtstart = dtstart
        self.dtend = dtend

    def print(self, nocolor=False):
        GRN = "" if nocolor else Fore.GREEN
        RED = "" if nocolor else Fore.RED
        RESET_ALL = "" if nocolor else Style.RESET_ALL
        print("- " + GRN + str(self.matter) + RESET_ALL + \
                " | " + RED + str(self.location) + RESET_ALL + \
                " | " + self.dtstart.strftime('%d %b %Y : %H:%M') + \
                " -> " + self.dtend.strftime('%d %b %Y : %H:%M') + \
                " | " + str(self.description))

    def toDict(self):
        l = {}
        l["matter"] = self.matter
        l["location"] = self.location
        l["description"] = self.description
        l["dtstart"] = self.dtstart.strftime('%d %b %Y : %H:%M')
        l["dtend"] = self.dtend.strftime('%d %b %Y : %H:%M')
        return l

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
