import argparse
import parse
from models import *

def main():
	group = 'INFOS4A1-1'
	weeks = parse.get_current_week(group)
	for w in weeks:
		print(w)
	
if __name__ == '__main__':
	main()