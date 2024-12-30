def average(lst):
    '''
    write a function that takes a list of integers, and returns the average of
    all the integers in the list, rounded down to the integer component of the average.

    the list will never be empty, the numbers will always be positive integers
    '''

    total = sum(lst)
    avg = total / len(lst)

    return int(avg)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True