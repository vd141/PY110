'''
return a new list identical in structure to the original but with each number incremented
by 1. do not modify the original data structure. use a comprehension
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_dict = [dict(zip(subdict.keys(), [sub_values + 1 for sub_values in subdict.values()])) for subdict in lst]
print(new_dict)
print(new_dict == [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}])

# alternate method
[{key: value + 1 for key, value in subdict.items()} for subdict in lst]