'''
sort the list so that the sub-lists are ordered based on the sum of the odd numbers
that they contain. the original list shouldn't be mutated
'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum(list_):
    return sum([num for num in list_ if num % 2 == 1])

print(sorted(lst, key=odd_sum) == [[1, 8, 3], [1, 6, 7], [1, 5, 3]])