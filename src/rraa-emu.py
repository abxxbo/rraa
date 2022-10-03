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
stack: int = []
sp: int = 0

alr_exec = False # When JMP is detected, this flag will be
								 # be set, and then jump.

def rraa_exit():
	print(f"{b0} | {b1} | {b2} | {b3} | {b4} | {b5} | {b6} | {b7}")
	exit(0)

class Interrupt:
	def __init__(self, int_no) -> None:
		self.int_no = int_no
		pass

	def ThrowInterrupt(int_no: int) -> None:
		match int_no:
			case 1:	# Serial output
				match b0:
					case 0x00:	# Write b1 to stdout
						print(chr(b1))

					case _:
						pass

			case _:
				pass
			


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
						case 0x66: b0 //= line[i+2]
						case 0x67: b1 //= line[i+2]
						case 0x68: b2 //= line[i+2]
						case 0x69: b3 //= line[i+2]
						case 0x6a: b4 //= line[i+2]
						case 0x6b: b5 //= line[i+2]
						case 0x6c: b6 //= line[i+2]
						case 0x6d: b7 //= line[i+2]
					
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
				case 0xca: # PUSHB
					print(line[i+1])
					match line[i+1]:
						case 0x66: stack[sp] = b0
						case 0x67: stack[sp] = b1
						case 0x68: stack[sp] = b2
						case 0x69: stack[sp] = b3
						case 0x6a: stack[sp] = b4
						case 0x6b: stack[sp] = b5
						case 0x6c: stack[sp] = b6
						case 0x6d: stack[sp] = b7
						case _: 	 stack[sp] = line[i+1]

					b0 = 0
					b1 = b0
					b2 = b1
					b3 = b2
					b4 = b3
					b5 = b4
					b6 = b5
					b7 = b6				
					

				### Bitwise ###

				### Interrupts ###
				case 0x27:		# INT
					int_no = line[i+1]
					Interrupt.ThrowInterrupt(int_no)