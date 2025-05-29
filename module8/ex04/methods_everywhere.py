#!/usr/bin/python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while(len(string) < 8):
        string = string + "Z"
    print(string)

i = 1
argv_len = len(sys.argv)

if (argv_len == 1):
    print("none")
else:
    while(i < argv_len):
        strlen = len(sys.argv[i])
        if (strlen > 8):
            shrink(sys.argv[i])
        elif (strlen < 8):
            enlarge(sys.argv[i])
        else:
            print(sys.argv[i])
        i += 1
