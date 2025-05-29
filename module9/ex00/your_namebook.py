#!/usr/bin/python3

def array_of_names(persons):
    array = []
    items = list(persons.items())
    i = 0
    while i < len(items):
        name, last_name = items[i]
        array.append(name.capitalize() + " " + last_name.capitalize())
        i += 1
    return array

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
