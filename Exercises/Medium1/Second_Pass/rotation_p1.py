def rotate_list(elements):
    '''
    rotates a list by moving the first element to the end of the list. does not
    mutate the original list

    return an empty list if the input is an empty list.

    return None if the input is not a list

    create a copy of the original list

    pop the first element of the list and append it to the back
    '''

    if elements == []:
        return []
    
    if not isinstance(elements, list):
        return

    new_list = elements.copy()
    new_list.append(new_list.pop(0))

    return new_list




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