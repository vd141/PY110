'''
print the name, age, and gender of each family member
'''
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for member in munsters:
    name = member
    age = munsters[name]['age']
    gender = munsters[name]['gender']
    print(f'{name} is a {age}-year-old {gender}')