#!/usr/bin/python3

import sys

def greetings(name=None):
    if (name is None):
        print("Hello, noble stranger.")
    elif not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print("Hello,", name, end=".\n")

if (len(sys.argv) == 1):
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)
