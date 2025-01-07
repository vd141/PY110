def multiply_list(lst):
    # for item in lst:
    #     item *= 2

    # return lst
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])

'''
item's new value is not being captured in the list. we can address this by
writing a list comprehension
'''

