#!/usr/bin/env python3

import sys, re

MAGIC_NUMBER = 0x72726161 # rraa in hex

LDA = 0x22
JMP = 0xe8
ADD = 0x2f
SUB = 0x2e
DIV = 0x2d
MUL = 0x2c

NOP = 0xf2


EXC = 0x72
INT = 0x27


class Opcode:
    # Example of flags for the opcode class
    # OP       => LDA
    # REG      => b2
    # VAL      => 26
    def __init__(self, op, reg, val):
        self.op  = op
        self.reg = reg
        self.val = val
    
    def WriteOpcodeToOut(op, reg, val, output_file):
        b: bytearray = [reg, op, 0, val]
        print(b)
        with open(output_file, "ab") as bin_file:
            bin_file.write(bytearray(b))

# Variables to use later on
NO_KRNL_FLAG = False # Assume false by default
file = ""
output_bin = "a.out"


# Check arguments to set variables above.
for i in range(len(sys.argv)):
    if sys.argv[i] == "--no-krnl":
        NO_KRNL_FLAG = True
    elif sys.argv[i] == "--source":
        file = sys.argv[i+1]
    elif sys.argv[i] == "--output":
        output_bin = sys.argv[i+1]
    else:
        continue


# We cannot output our binary to our input file, this
# will most likely lead to some problems.
if output_bin == file:
    print("I cannot write a binary to the input file.")
    sys.exit(0x7f)


def RaiseError(errno: str) -> None:
	print(f"Error in {file}: {errno}")
	sys.exit(2)


# Continue as normal, everything should be ok.

# Zero it out
with open(output_bin, "wb") as bffn:
	bffn.close()

# Write magic bytes
with open(output_bin, "ab") as b22afbbb:
    skfd: bytearray = [0x72, 0x72, 0x61, 0x61]
    b22afbbb.write(bytearray(skfd))


with open(file) as f:
	for line in f:
		# Ignore any comment
		if line[0] == '@':
			break

		line = line.replace('\n', '').replace('\r', '')
		tok = re.split(r'[, ]',line)

		if '' in tok: tok.remove('')

		try:
			opcode = tok[0].upper()
		except:
			pass		# line is empty



		match opcode:
			case "LDA":
				if tok[2] != "<-": RaiseError("arrow misconfigured")
				reg = 0
				match tok[1]:
					case "b0": reg = 0x66
					case "b1": reg = 0x67
					case "b2": reg = 0x68
					case "b3": reg = 0x69
					case "b4": reg = 0x6a
					case "b5": reg = 0x6b
					case "b6": reg = 0x6c
					case "b7": reg = 0x6d

				Opcode.WriteOpcodeToOut(0x22, reg, int(tok[3]), output_bin)

			case "JMP":
				Opcode.WriteOpcodeToOut(0xe8, int(tok[1][2:], base=16), 0, output_bin)
			
			case "ADD":
				reg = 0
				match tok[1][0:2]:
					case "b0": reg = 0x66
					case "b1": reg = 0x67
					case "b2": reg = 0x68
					case "b3": reg = 0x69
					case "b4": reg = 0x6a
					case "b5": reg = 0x6b
					case "b6": reg = 0x6c
					case "b7": reg = 0x6d

				if tok[2][1] == "x":
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2f, reg, int(tok[2][2:], base=16)]))
				else:
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2f, reg, int(tok[2])]))

			case "SUB":
				reg = 0
				match tok[1][0:2]:
					case "b0": reg = 0x66
					case "b1": reg = 0x67
					case "b2": reg = 0x68
					case "b3": reg = 0x69
					case "b4": reg = 0x6a
					case "b5": reg = 0x6b
					case "b6": reg = 0x6c
					case "b7": reg = 0x6d

				if tok[2][1] == "x":
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2e, reg, int(tok[2][2:], base=16)]))
				else:
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2e, reg, int(tok[2])]))


			case "DIV":
				reg = 0
				match tok[1][0:2]:
					case "b0": reg = 0x66
					case "b1": reg = 0x67
					case "b2": reg = 0x68
					case "b3": reg = 0x69
					case "b4": reg = 0x6a
					case "b5": reg = 0x6b
					case "b6": reg = 0x6c
					case "b7": reg = 0x6d

				if tok[2][1] == "x":
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2d, reg, int(tok[2][2:], base=16)]))
				else:
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2d, reg, int(tok[2])]))


			case "MUL":
				reg = 0
				match tok[1][0:2]:
					case "b0": reg = 0x66
					case "b1": reg = 0x67
					case "b2": reg = 0x68
					case "b3": reg = 0x69
					case "b4": reg = 0x6a
					case "b5": reg = 0x6b
					case "b6": reg = 0x6c
					case "b7": reg = 0x6d

				if tok[2][1] == "x":
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2c, reg, int(tok[2][2:], base=16)]))
				else:
					with open(output_bin, "ab") as nop_write:
						nop_write.write(bytearray([0x2c, reg, int(tok[2])]))
								

			case "NOP":
				with open(output_bin, "ab") as nop_write:
					nop_write.write(bytearray([0xf2]))


			# TODO: implement AND, OR, and XOR.
			# These should check if val1 is a register, if not,
			# throw an error


			case "EXC":
				exc_num = 0
				if tok[1][1] == 'x': # hex
					exc_num = int(tok[1][2:], base=16)
				else:
					exc_num = int(tok[1])
				with open(output_bin, "ab") as f:
					f.write(bytearray([EXC, exc_num]))


			case _:
				break