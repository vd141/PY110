def rotate_list(list1):
    '''
    rotates the list by moving the first element to the end of the list

    returns none if the input is not a list

    if input is empty, return an empty list

    data structure: 
        - none

    algorithm:
        - check if the input is a list
        - check if the input is empty
        - rotate the list
    '''

    if not isinstance(list1, list):
        return
    
    return list1 if list1 == [] else list1[1:] + [list1[0]]


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