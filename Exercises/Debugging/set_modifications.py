data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)

'''
the set's size changes whenever an item is removed. so the for loop iterates
over a changing object, which is an error as considered by the python interpreter

another way to filter down the elements of data_set is to use a set comrehension
with a selection criteria of item % 2 == 0
'''

data_set = {item for item in data_set if item % 2 != 0}