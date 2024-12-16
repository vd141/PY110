'''
return a new list with the same structure, but with the values in each sublist
ordered in ascending order. use a comprehension if you can

[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = [sorted(inner) for inner in lst]

print(new_lst == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])

# for loop version

new_lst_for_loop = []
for inner in lst:
    new_lst_for_loop.append(sorted(inner))
print (new_lst_for_loop == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])