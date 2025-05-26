#!/usr/bin/python3

number =  int(input("Enter a number less than 25\n"))

if (number > 25):
    print("Error")
while (number <= 25):
    print("Inside the loop, my variable is", number)
    number = number + 1