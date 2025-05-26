#!/usr/bin/python3

string = input()
i = 0
strlen = len(string)

while i < strlen:
    character = string[i]
    if 'a' <= character <= 'z':
        print(chr(ord(character) - 32), end="")
    elif 'A' <= character <= 'Z':
        print(chr(ord(character) + 32), end="")
    else:
        print(character, end="")
    i += 1
print()