#!/usr/bin/python3

import sys

args_len = len(sys.argv)

if (args_len != 2):
    print("none")
else:
    parameter = input("What was the parameter? ")
    if (parameter == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")