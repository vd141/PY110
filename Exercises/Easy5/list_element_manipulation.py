def multiply_items(list_a, list_b):
    '''
    given two lists of integers of the same length, return a new list
    where each element is the product of the corresponding elements
    from the two lists

    try with zipping
    '''

    return [list_a[idx] * list_b[idx] for idx in range(len(list_a))]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True