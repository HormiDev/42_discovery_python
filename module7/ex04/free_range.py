#!/usr/bin/python3

import sys

args_len = len(sys.argv)
array = []

if (args_len != 3):
    print("none")
else:
    if (int(sys.argv[1]) <= int(sys.argv[2])):
        for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
            array.append(i)
    else:
        for i in range(int(sys.argv[1]), int(sys.argv[2]) - 1, -1):
            array.append(i)
    print(array)