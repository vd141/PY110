def halvsies(lst):
    '''
    function that takes a list as an argument and returns a list that contains
    two elements, both of which are lists. put the first half of the original
    list elements in the first element of the return value and the second half
    in the second element. if the original list contains an odd number of elements,
    place the middle element in the first half list
    '''

    midpoint = int(len(lst) / 2)

    # [1, 2, 3]
    #  0  1  2

    if len(lst) % 2 == 1:
        return [lst[:midpoint + 1], lst[midpoint + 1:]]
    else:
        return [lst[:midpoint], lst[midpoint:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])