def interleave(list1, list2):
    '''
    combines two lists passed as arguments and returns a new liste that
    contains all elements from both list arguments, with each element taken
    in alternation
    '''

    return_list = []

    for pair in zip(list1, list2):
        return_list.extend(pair)

    return return_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True