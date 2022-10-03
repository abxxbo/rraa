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

alr_exec = False # When JMP is detected, this flag will be
								 # be set, and then jump.

def rraa_exit():
	print(f"{b0} | {b1} | {b2} | {b3} | {b4} | {b5} | {b6} | {b7}")
	exit(0)

# Check through each opcode
with open(bin, "rb") as f:
	for line in f:
		for i in range(len(line)):
			match line[i]:
				case 0x22: # LDA
					match line[i+1]:
						case 0x66: b0 = line[i+2]
						case 0x67: b1 = line[i+2]
						case 0x68: b2 = line[i+2]
						case 0x69: b3 = line[i+2]
						case 0x6a: b4 = line[i+2]
						case 0x6b: b5 = line[i+2]
						case 0x6c: b6 = line[i+2]
						case 0x6d: b7 = line[i+2]

					i += 3

				case 0xe8: # JMP
					# FIXME: This theoretical implementation
					# of JMP does not work.
					if alr_exec == False:
						i = line[i+1]
						alr_exec = True

				### Arithmetic ###
				case 0x2f:		# ADD
					match line[i+1]:
						case 0x66: b0 += line[i+2]
						case 0x67: b1 += line[i+2]
						case 0x68: b2 += line[i+2]
						case 0x69: b3 += line[i+2]
						case 0x6a: b4 += line[i+2]
						case 0x6b: b5 += line[i+2]
						case 0x6c: b6 += line[i+2]
						case 0x6d: b7 += line[i+2]
					
					i += 3
				
				case 0x2e:	# SUB
					match line[i+1]:
						case 0x66: b0 -= line[i+2]
						case 0x67: b1 -= line[i+2]
						case 0x68: b2 -= line[i+2]
						case 0x69: b3 -= line[i+2]
						case 0x6a: b4 -= line[i+2]
						case 0x6b: b5 -= line[i+2]
						case 0x6c: b6 -= line[i+2]
						case 0x6d: b7 -= line[i+2]
					
					i += 3

				case 0x2d:	# DIV
					match line[i+1]:
						case 0x66: b0 /= line[i+2]
						case 0x67: b1 /= line[i+2]
						case 0x68: b2 /= line[i+2]
						case 0x69: b3 /= line[i+2]
						case 0x6a: b4 /= line[i+2]
						case 0x6b: b5 /= line[i+2]
						case 0x6c: b6 /= line[i+2]
						case 0x6d: b7 /= line[i+2]
					
					i += 3

				case 0x2c:	# MUL
					match line[i+1]:
						case 0x66: b0 *= line[i+2]
						case 0x67: b1 *= line[i+2]
						case 0x68: b2 *= line[i+2]
						case 0x69: b3 *= line[i+2]
						case 0x6a: b4 *= line[i+2]
						case 0x6b: b5 *= line[i+2]
						case 0x6c: b6 *= line[i+2]
						case 0x6d: b7 *= line[i+2]
					
					i += 3

				

				### Uncategorized ###
				case 0xf2:	# NOP
					i += 1

				case 0xff:  # HLT
					rraa_exit()
				
				### Stack ###

				### Bitwise ###

				### Interrupts ###