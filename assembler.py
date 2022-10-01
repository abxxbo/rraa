#!/usr/bin/env python3

import sys


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
