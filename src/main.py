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
__website__ = "https://github.com/cedricfarinazzo/ichronos.py"


import argparse
import json
from colorama import init
init()
from utils import *
from models import *

def main():
    argp = argparse.ArgumentParser(prog=__project__, description="A simple ichronos parser write in python3", \
            epilog="By " + __maintainer__ + " <" + __email__ + ">\n")

    argp.add_argument("group", help=" Group name of your class (ex: INFOS4A1-1)", type=str)
    argp.add_argument("-v", "--verbosity", dest='verbose', default=False, help="increase output verbosity", action="store_true")
    argp.add_argument("-w", "--week", help="Show the schedule of the week. Argument: Week id (see more here: https://ichronos.net/about)", type=int)
    argp.add_argument("-t", "--today", default=False, action='store_true', help="Show today's schedule")
    argp.add_argument('--json', dest='json', default=False, action='store_true', help='Json output format')
    argp.add_argument('--nocache', dest='nocache', default=False, action='store_true', help='Disable cache system')
    argp.add_argument('--nocolor', dest='nocolor', default=False, action='store_true', help='Argument to disable colored output')
    argp.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    args = argp.parse_args()
    
    if args.today and args.week is not None:
        argp.print_help()
        return
    
    config = {"nocolor": args.nocache, "verbose": args.verbose, "cache": not args.nocache}
    
    weeks = None
    if args.week is None:
        weeks = get_current_week(args.group, config)
    else:
        weeks = get_custom_week(args.group, config)

    if args.json:
        j = []
        for w in weeks:
            j.append(w.toDict())
        print(json.dumps(j))
    else:
        for w in weeks:
            w.print(nocolor=config["nocolor"])

if __name__ == '__main__':
    main()
