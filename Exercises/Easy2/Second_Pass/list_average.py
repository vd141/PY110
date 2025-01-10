def average(list1):
    '''
    takes one argument, a list of integers, and returns the average
    of all the integers in teh list, rounded down to the integer component
    of the average. the lsit will never be empty, and the numbers will always
    be positive integers
    '''

    return sum(list1) // len(list1)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True