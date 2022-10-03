#!/usr/bin/env python3

from sys import argv, exit

bin = ""

# Check all arguments for binary file.
def show_help():
	print("Usage: rraa-emu.py [--bin] [rraa binary]")
	exit(2)

for i in range(len(argv)):
	if argv[i] == "--help":
		show_help()
	if argv[i] == "--bin":
		bin = argv[i+1]
	else:
		continue
