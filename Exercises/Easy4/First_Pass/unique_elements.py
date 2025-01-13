def unique_from_first(list1, list2):
    '''
    from two lists, determine the elements that are unique to the first list.
    store and return these values in a set
    '''
    return set(list1) - (set(list1) & set(list2))
    

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})