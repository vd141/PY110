'''
return a new list with the same structure, but with the values in each sublist in
ascending order as strings (that is, the numbers shoudl be treated as strings)

expected result;
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []

for nested_list in lst:
    nested_list.sort(key=str)
    new_lst.append(nested_list)

print(new_lst == [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']])

new_comp_lst = [sorted(nested, key=str) for nested in lst]

print(new_comp_lst == [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']])