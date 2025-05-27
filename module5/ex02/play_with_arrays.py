#!/usr/bin/python3

Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
New_array = []
i = 0
array_len = len(Original_array)

while (i < array_len):
    if (Original_array[i] > 5):
        New_array.append(Original_array[i] + 2)
    i += 1
print(f"Original array: {Original_array}")
print(f"New array: {New_array}")
