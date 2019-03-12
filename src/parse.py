#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, sys, time
from icalendar import Calendar
from models import *
import os, tempfile

def get_lessons(url, ext=".ics", nocolor=False, verbose=False, cache=True):
    url = url + ext
    urlf = url.replace("https", "")
    urlf = urlf.replace("http", "")
    urlf = urlf.replace("://", "")
    urlf = urlf.replace("/", "_")
    filcache = os.path.join(tempfile.gettempdir(), urlf)
    
    isCached = False
    isDownload = False
    text = ""

    if cache and os.path.exists(filcache):
        lastupdate_file = os.path.getctime(filcache)
        difftime = time.time() - lastupdate_file
        if difftime < 3600 * 24:
            if verbose:
                print("[+] cache file: " + filcache)
            with open(filcache, 'r') as f:
                text = f.read()
            isCached = text != ""
    
    if not isCached:
        if verbose:
            print("[+] url: " + url)
        tstart = time.time()
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            print("Failed to establish a new connection: [Errno 11001] getaddrinfo failed")
            sys.exit(1)
        if verbose:
            print("[+] Get page in " + ("%.3f" % (time.time() - tstart))	+ " seconds")
            print("[+] Header: ")
            for key, value in r.headers.items():
                print("[+]     %s: %s" % (key, value))
            print("[+]     %s: %d o" % ("Raw size", len(r.content)))
            print("[+] status_code: " + str(r.status_code))
        text = r.text
        isDownload = text != "" and r.status_code == 200
        if cache and r.status_code == 200:
            if verbose:
                print("[+] cache file created: " + filcache)
            with open(filcache, 'w') as f:
                f.write(r.text)
    
    lessons = []
    if isDownload or isCached:
        try:
            gcal = Calendar.from_ical(text)
        except ValueError:
            print("Wrong group name")
            sys.exit(1)
        for component in gcal.walk():
            if component.name == "VEVENT":
                matter = component.get('summary')
                description = component.get('description')
                location = component.get('location')

                tsr = component.decoded('dtstart')
                te = component.decoded('dtend')
                lesson = Lesson(matter, description, location, tsr, te, nocolor=nocolor)
                lessons.append(lesson)
        return lessons
    return None

def parse(lessons, nocolor=False, verbose=False):
    lessons.sort()
    if lessons == []:
        return []

    sday = ""
    day = None
    weeks = []
    week_cur = 0
    weeks.append(Week(lessons[0].dtstart.isocalendar()[1], nocolor=nocolor))

    for c in lessons:
        if c.dtstart.isocalendar()[1] != weeks[week_cur].week:
            if day is not None:
                weeks[week_cur].add_day(day)
            sday = c.get_day()
            day = Day(sday, nocolor=nocolor)
            week_cur += 1
            weeks.append(Week(c.dtstart.isocalendar()[1], nocolor=nocolor))
        if sday != c.get_day():
            if day is not None:
                weeks[week_cur].add_day(day)
            sday = c.get_day()
            day = Day(sday, nocolor=nocolor)
        day.add_lesson(c)
    if day.lessons != []:
        weeks[week_cur].add_day(day)

    return weeks

def get_current_week(group, nocolor=False, verbose=False):
    url = 'https://ichronos.net/feed/' + group
    lessons = get_lessons(url, nocolor=nocolor, verbose=verbose)
    if lessons is None:
        print("An error occured")
        sys.exit(1)
    return parse(lessons, nocolor=nocolor, verbose=verbose)

def get_custom_week(group, week, nocolor=False, verbose=False):
    url = 'https://ichronos.net/ics/' + group  + '/' + week
    lessons = get_lessons(url, nocolor=nocolor, verbose=verbose)
    if lessons is None:
        print("An error occured")
        sys.exit(1)
    return parse(lessons, nocolor=nocolor, verbose=verbose)

