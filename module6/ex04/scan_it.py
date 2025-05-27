#!/usr/bin/python3

import sys
import re

args_len = len(sys.argv)

if (args_len == 3):
    result = len(re.findall(sys.argv[1], sys.argv[2]))
    if (result == 0):
        print("none")
    else:
        print(str(result))
else:
    print("none")
