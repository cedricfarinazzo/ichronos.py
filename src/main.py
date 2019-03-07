#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__project__ = "ichronos.py"
__author__ = "Cédric FARINAZZO"
__copyright__ = "Copyright 2019"
__credits__ = ["Cédric FARINAZZO"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Cédric FARINAZZO"
__email__ = "cedric.farinazzo@gmail.com"


import argparse
from colorama import init
init()
import parse
from models import *

def main():
	argp = argparse.ArgumentParser(prog=__project__, description="A simple ichronos parser write in python3", \
	epilog="By " + __maintainer__ + " <" + __email__ + ">\n")

	argp.add_argument("group", help=" Group name of your class (ex: INFOS4A1-1)", type=str)
	argp.add_argument("-v", "--verbosity", dest='verbose', default=False, help="increase output verbosity", action="store_true")
	argp.add_argument("-w", "--week", help="Week id (see more here: https://ichronos.net/about)", type=int)
	argp.add_argument('--nocolor', dest='nocolor', default=False, action='store_true', help='Argument to disable colored output')
	argp.add_argument('--version', action='version', version='%(prog)s ' + __version__)
	
	args = argp.parse_args()

	if args.week is None:
		weeks = parse.get_current_week(args.group, nocolor=args.nocolor, verbose=args.verbose)
		for w in weeks:
			print(w)
	else:
		weeks = parse.get_custom_week(args.group, str(args.week), nocolor=args.nocolor, verbose=args.verbose)
		for w in weeks:
			print(w)

if __name__ == '__main__':
	main()