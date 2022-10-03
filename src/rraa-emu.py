#!/usr/bin/env python3

import re
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


## Registers
b0 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0

## Memory
memory: int = []
sp: int = 0

# Check through each opcode
with open(bin, "rb") as f:
	for line in f:
		for i in range(len(line)):
			match line[i]:
				case 0x22:
					reg = 0
					match line[i+1]:
						case 0x66: b0 = line[i+2]
						case 0x67: b1 = line[i+2]
						case 0x68: b2 = line[i+2]
						case 0x69: b3 = line[i+2]
						case 0x6a: b4 = line[i+2]
						case 0x6b: b5 = line[i+2]
						case 0x6c: b6 = line[i+2]
						case 0x6d: b7 = line[i+2]
						

print(f"{b0} | {b1} | {b2} | {b3} | {b4} | {b5} | {b6} | {b7}")