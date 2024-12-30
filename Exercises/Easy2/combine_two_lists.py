def interleave(lst1, lst2):
    '''
    takes two lists as arguments and returns a new list that contains all
    elements from both list arguments, with each element taken in alternation

    both lists are non empty and have the same number of elements
    '''

    # return_list = []

    # for idx, _ in enumerate(lst1):
    #     return_list.append(lst1[idx])
    #     return_list.append(lst2[idx])

    # return return_list

    # with zip function

    zipped = zip(lst1, lst2)

    return [el for tup in zipped for el in tup]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

