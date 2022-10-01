#!/usr/bin/env python3

from enum import Enum
import sys

MAGIC_NUMBER = 0x72726161 # rraa in hex

LDA = 0x22
JMP = 0xe8
ADD = 0x2f
SUB = 0x2e
DIV = 0x2d
MUL = 0x2c

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


# Continue as normal, everything should be ok.
