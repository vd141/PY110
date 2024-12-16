'''
compute and display the total age of the family's male members
'''
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

running_total = 0

for member in munsters:
    if munsters[member]['gender'] == 'male':
        running_total += munsters[member]['age']

print(running_total)

## list comprehension: return a list with all the ages, then sum the list

print(sum(munsters[member]['age'] for member in munsters if munsters[member]['gender'] == 'male'))