def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
print(append_to_list(4))

'''
the lst variable isn't being assigned to an empty list each time the function is
run
'''