#!/usr/bin/python3

num1 = 0

while (num1 < 11):
    print("Table of "+str(num1)+":", end=" ")
    num2 = 0
    while (num2 < 11):
        result = num1 * num2
        print(str(result), end=" ")
        num2 = num2 + 1
    print()
    num1 = num1 + 1
