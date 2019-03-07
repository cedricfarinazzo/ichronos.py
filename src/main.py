import argparse
import parse
from models import *

def main():
	argp = argparse.ArgumentParser(description="A simple ichronos parser write in python3", \
	epilog="By Cédric FARINAZZO <cedric.farinazzo@gmail.com>\n")
	
	argp.add_argument("group", help=" Group name of your class (ex: INFOS4A1-1)", type=str)
	argp.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
	argp.add_argument("-w", "--week", help="Week id", type=str)
	argp.add_argument("--nocolor", help="Disable colored output", action="store_true")
	
	args = argp.parse_args()
	#print(args)
	
	if args.week is None:
		weeks = parse.get_current_week(args.group)
		for w in weeks:
			print(w)
	else:
		weeks = parse.get_custom_week(args.group, args.week)
		for w in weeks:
			print(w)
	
if __name__ == '__main__':
	main()