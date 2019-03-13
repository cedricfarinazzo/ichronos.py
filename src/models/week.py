#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

class Week:

    def __init__(self, week):
        self.days = []
        self.week = week
        
    def print(self, nocolor=False):
        CYAN = "" if nocolor else Fore.CYAN
        RESET_ALL = "" if nocolor else Style.RESET_ALL
        print(CYAN + " ---- Week N°%d ---- " %(self.week) + RESET_ALL + "\n")
        for d in self.days:
            d.print(nocolor=nocolor)
            print("\n")

    def toDict(self):
        w = {}
        w["week"] = str(self.week)
        w["days"] = []
        for d in self.days:
            w["days"].append(d.toDict())
        return w

    def add_day(self, day):
        self.days.append(day)