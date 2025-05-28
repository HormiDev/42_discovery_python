#!/usr/bin/python3

import sys
import re

args_len = len(sys.argv)

if (args_len == 2):
    result = len(re.findall("z", sys.argv[1]))
    if (result == 0):
        print("none")
    else:
        i = 0
        while (i < result):
            print("z", end="")
            i += 1
        print()
else:
    print("none")
