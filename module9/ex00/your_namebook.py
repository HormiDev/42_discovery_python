#!/usr/bin/python3

def array_of_names(persons):
    array = []
    persons_len = len(persons)
    i = 0
    while (i < persons_len):
        array.append(persons)


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))