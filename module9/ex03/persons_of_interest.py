#!/usr/bin/python3

def famous_births(women_scientists):
	for key in sorted(women_scientists, key=lambda x: women_scientists[x]["date_of_birth"]):
		person = women_scientists[key]
		print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
