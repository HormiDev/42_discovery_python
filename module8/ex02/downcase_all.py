#!/usr/bin/python3

import sys

def downcase_it(string):
    return string[:].lower()

args_len = len(sys.argv)
i = 1

if (args_len < 2):
    print("none")
else:
    while (i < args_len):
        print(downcase_it(sys.argv[i]))
        i += 1
