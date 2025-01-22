def rotate_list(elements):
    import copy
    '''
    rotates a list by moving the first element to the end of the list

    returns a new list, does not mutate the original

    use string slicing to grab the first element and append it to a slice of
    the remaining elements

    return None if argument is not a list

    return an empty list if argument is empty

    return a copy if the list is one element long
    '''

    if not isinstance(elements, list):
        return None
    
    if len(elements) <= 1:
        return copy.deepcopy(elements)

    return elements[1:] + [elements[0]]

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])