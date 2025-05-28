#!/usr/bin/python3

import sys

args_len = len(sys.argv)
i = 1
cont = 0

if (args_len < 2):
    print("none")
    exit(0)
while (i < args_len):
    match sys.argv[i]:
        case _ if not sys.argv[i].endswith("ism"):
            print(sys.argv[i] + "ism")
            cont += 1
    i += 1
if (cont == 0):
    print("none")