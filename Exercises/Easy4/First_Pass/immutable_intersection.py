def intersection(list1, list2):
    '''
    transforms two lists into frozen sets and finds their common elements
    '''

    frz1 = frozenset(list1)
    frz2 = frozenset(list2)

    return frz1.intersection(frz2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True