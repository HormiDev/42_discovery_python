#!/usr/bin/python3

import sys

args_len = len(sys.argv)

if (args_len > 2):
    while (args_len > 1):
        print(sys.argv[args_len - 1])
        args_len -= 1
else:
    print("none")
