'''
write some code to return a list that contains only the dicts where all numbers are even
'''

expected = [{'e': [8], 'f': [6, 10]}]

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new_lst = []

for elem in lst:
    add_this_dict = True
    for value in elem.values():
        for val_elem in value:
            if val_elem % 2 != 0:
                add_this_dict = False
            if add_this_dict == False:
                break
        if add_this_dict == False:
            break
    if add_this_dict == True:
        new_lst.append(elem)

print(new_lst == expected)