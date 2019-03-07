import argparse
from colorama import init
init()
import parse
from models import *

def main():
	argp = argparse.ArgumentParser(description="A simple ichronos parser write in python3", \
	epilog="By Cédric FARINAZZO <cedric.farinazzo@gmail.com>\n")
	
	argp.add_argument("group", help=" Group name of your class (ex: INFOS4A1-1)", type=str)
	argp.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
	argp.add_argument("-w", "--week", help="Week id", type=str)
	argp.add_argument('--nocolor', dest='nocolor', default=False, action='store_true', help='Argument to disable colored output')
	
	args = argp.parse_args()
	#print(args)
	
	if args.week is None:
		weeks = parse.get_current_week(args.group, nocolor=args.nocolor)
		for w in weeks:
			print(w)
	else:
		weeks = parse.get_custom_week(args.group, args.week, nocolor=args.nocolor)
		for w in weeks:
			print(w)
	
if __name__ == '__main__':
	main()