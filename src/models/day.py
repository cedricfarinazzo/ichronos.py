#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

class Day:

    def __init__(self, day):
        self.lessons = []
        self.day = day

    def print(self, nocolor=False):
        YEL = "" if nocolor else Fore.YELLOW
        RESET_ALL = "" if nocolor else Style.RESET_ALL
        print(YEL + " => %s " %(self.day) + RESET_ALL)
        for l in self.lessons:
            l.print(nocolor=nocolor)

    def toDict(self):
        d = {}
        d["day"] = str(self.day)
        d["lessons"] = []
        for l in self.lessons:
            d["lessons"].append(l.toDict())
        return d

    def add_lesson(self, lesson):
        self.lessons.append(lesson)
