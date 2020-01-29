#!/usr/bin/env python3

"""Main."""

import sys
from cpu import CPU

cpu = CPU()

# Need to perform sys argv to determine which program needs to be loaded
if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

program = []
try:
    with open(sys.argv[1]) as f:

        for line in f:
            comment_split = line.split("#")
            num = comment_split[0].strip()
            if num == '':
                continue
            value = int(num, 2)
            program.append(value)

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)

cpu.load(program)
cpu.run()
