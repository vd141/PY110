def multiply_items(list1, list2):
    '''
    return a new list where each element is the product of the corresponding
    elements from the two lists
    '''

    return [elem1 * elem2 for elem1, elem2 in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True