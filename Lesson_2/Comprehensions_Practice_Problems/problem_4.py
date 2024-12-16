'''
write some code that defines a dictionary where the key is the first item in each sublist
and the value is the second
'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {nested[0]: nested[1] for nested in lst}

print(new_dict == # Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
})