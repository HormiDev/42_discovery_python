#!/usr/bin/python3

import sys

def add_one(number):
    number += 1

var = 10

if (len(sys.argv) == 1):
    print(var)
    add_one(var)
    print(var)
