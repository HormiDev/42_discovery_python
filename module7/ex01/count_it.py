#!/usr/bin/python3

import sys

args_len = len(sys.argv)

if (args_len < 2):
    print("none")
else:
    print("parameters:", str(args_len - 1))
    for i in range(1, args_len):
        print(f"{sys.argv[i]}:", str(len(sys.argv[i])))
