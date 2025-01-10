def union(list1, list2):
    '''
    takes two lists as arguments and returns a set that contains the union of
    the values from the two lists. You may assume that both arguments will
    always be lists
    '''

    set1 = set(list1)
    set2 = set(list2)

    return set1.union(set2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True