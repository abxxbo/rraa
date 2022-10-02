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

stoi_det = False
class Opcode:
		# Example of flags for the opcode class
		# OP			 => LDA
		# REG			=> b2
		# VAL			=> 26
		def __init__(self, op, reg, val):
				self.op	= op
				self.reg = reg
				self.val = val
		
		def WriteOpcodeToOut(op, reg, val, output_file):
				b: bytearray = [reg, op, 0, val]
				print(b)
				with open(output_file, "ab") as bin_file:
						bin_file.write(bytearray(b))
		def WriteOneOpcode(opcode, out):
			with open(out, "ab") as f:
				f.write(bytearray(opcode))

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

def RaiseWarning(warn: str) -> None:
	print(warn)


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

				b_array = []
				try:
					if tok[3][1] == "x":
						b_array = [0x22, reg, int(tok[3][2:], base=16)]
				except:
					b_array = [0x22, reg, int(tok[3])]
				with open(output_bin, "ab") as lda_write:
					lda_write.write(bytearray(b_array))

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

			case "AND":
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
					case _:
						RaiseError("Unknown register.")

				# Cool, now get val2
				val2 = tok[2]
				upd_val2 = 0
				print(val2)
				try:
					if tok[2][1] == "x":
						upd_val2 = int(tok[2][2:], base=16)
					else:
						upd_val2 = int(tok[2])
				except:
					# It's just an integer...
					upd_val2 = int(tok[2])


				# Write to the file
				with open(output_bin, "ab") as f:
					f.write(bytearray([0x72, reg, upd_val2]))

			case "OR":
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
					case _:
						RaiseError("Unknown register.")

				# Cool, now get val2
				val2 = tok[2]
				upd_val2 = 0
				print(val2)
				try:
					if tok[2][1] == "x":
						upd_val2 = int(tok[2][2:], base=16)
					else:
						upd_val2 = int(tok[2])
				except:
					# It's just an integer...
					upd_val2 = int(tok[2])


				# Write to the file
				with open(output_bin, "ab") as f:
					f.write(bytearray([0x73, reg, upd_val2]))


			# TODO: rewrite XOR so that
			# XOR b0, b0 is possible.
			case "XOR":
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
					case _:
						RaiseError("Unknown register.")

				# Cool, now get val2
				val2 = tok[2]
				upd_val2 = 0
				print(val2)
				try:
					if tok[2][1] == "x":
						upd_val2 = int(tok[2][2:], base=16)
					else:
						upd_val2 = int(tok[2])
				except:
					# It's just an integer...
					upd_val2 = int(tok[2])


				# Write to the file
				with open(output_bin, "ab") as f:
					f.write(bytearray([0x74, reg, upd_val2]))


			##### INTERRUPTS #####
			case "STOI": # Stop all interrupts
				stoi_det = True
				Opcode.WriteOneOpcode(0x38, output_bin)

			case "EXC":
				exc_num = 0
				if tok[1][1] == 'x': # hex
					exc_num = int(tok[1][2:], base=16)
				else:
					exc_num = int(tok[1])
				with open(output_bin, "ab") as f:
					f.write(bytearray([EXC, exc_num]))

			case "REEN":
				stoi_det = False
				Opcode.WriteOneOpcode(0x83, output_bin)


			case "INT":
				if stoi_det == True:
					# Throw a warning, however
					# still do the operation
					RaiseWarning("[semantic] You are attempting to raise interrupt when they are off.")
				int_num = 0		# interrupt number
				try:
					if tok[1][1] == 'x': # hex
						int_num = int(tok[1][2:], base=16)
					else:
						int_num = int(tok[1])
				except:
					# it can't be hex
					# so just fall back
					# to number
					int_num = int(tok[1])
				with open(output_bin, "ab") as f:
					f.write(bytearray([INT, int_num]))


			case "HLT":
				with open(output_bin, "ab") as f:
					f.write(bytearray([0xff]))
			case _:
				break