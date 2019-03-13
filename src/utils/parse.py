#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from icalendar import Calendar
from models import *
from utils import *

def get_lessons(data):
    lessons = []
    try:
        gcal = Calendar.from_ical(data)
    except ValueError:
        print("Wrong group name")
        return None
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
    if day.lessons != []:
        weeks[week_cur].add_day(day)

    return weeks

def escape_groupe(group):
    return group.replace('#', '%23')

def get_week(url, config):
    data = schedule_request(url, verbose=config["verbose"], cache=config["cache"])
    if data is None:
        print("An error occured")
        sys.exit(1)
    lessons = get_lessons(data)
    if lessons is None:
        sys.exit(1)
    return parse(lessons)
    
def get_current_week(group, config):
    url = 'https://ichronos.net/feed/' + escape_groupe(group)
    return get_week(url, config)

def get_custom_week(group, config, week):
    url = 'https://ichronos.net/ics/' + escape_groupe(group)  + '/' + week
    return get_week(url, config)
   
def get_today(group, config):
    week = get_current_week(group, config)
    #do some shit
    return week
