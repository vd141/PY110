import copy

# original = [[1], [2], [3]]
# copied = copy.copy(original)

# original[0][0] = 99

# print(copied[0] == [1])

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

'''
the code above is performing a shallow copy. that is, it creates a new outer
list, but all the elements of the new list point to the same objects of the
original. to make changes to the original list without affecting the new one,
the new list should be a deep copy
'''