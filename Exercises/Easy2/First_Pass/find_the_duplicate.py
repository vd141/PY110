def find_dup(lst):
    '''
    write a function that returns the duplicate value. all other values occur only
    once
    '''

    # sets only contain unique values.
    # algorithmically, we could compare each number in the list to the remaining
    # numbers to find a duplicate.
    
    # assume that the list does have a duplicate number inside

    # for idx, val1 in enumerate(lst[:-1]):
    #     for val2 in lst[idx + 1:]:
    #         if val1 == val2:
    #             return val1
            
    # this is O(N^2) -> naive solution. works, but there are better solutions
    # better solution O(N) is to use a set to store the seen values. lookup from
    # this set is O(N), so we only need to loop through the entire list once O(N)
    seen = set()

    for val in lst:
        if val in seen:
            return val
        seen.add(val)



print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
