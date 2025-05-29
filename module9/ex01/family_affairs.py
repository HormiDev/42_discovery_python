#!/usr/bin/python3

def find_the_redheads(persons):
    iterable = filter(lambda person: person[1] == "red", persons.items())
    return [name for name, _ in iterable]

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
