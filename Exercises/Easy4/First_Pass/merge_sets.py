def merge_sets(list1, list2):
    '''
    given two lists, convert them to sets and return a new set which is the union
    of both sets
    '''

    set1 = set(list1)
    set2 = set(list2)

    return set1.union(set2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True