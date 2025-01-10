def multiply_list(list1, list2):
    '''
    takes two list arguments, each containing a list of numbers, and returns
    a new list that contains the product of each pair of numbers from the args
    that have the same index. assume each argument is the same length
    '''

    return [list1[idx] * list2[idx] for idx in range(len(list1))]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True