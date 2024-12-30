def multiply_list(list1, list2):
    '''
    function that takes two list arguments, each containing a list of numbers,
    and returns a new list that contains the product of each pair of numbers
    from the arguments that have the same index. you may assume the arguments 
    contain the same number of elements
    '''

    new_list = []

    for idx in range(len(list1)):
        new_list.append(list1[idx] * list2[idx])

    return new_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True