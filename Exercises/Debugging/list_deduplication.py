data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
# print(unique_data == [4, 2, 1, 3]) # order not guaranteed

'''
preserve the order after using a set
'''

# create a new list, using a set as a lookup for existing values

unique_data = set()
new_list = []
for entry in data:
    if entry not in unique_data:
        unique_data.add(entry)
        new_list.append(entry)
unique_data = new_list
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

'''
use a set to keep track of elements that are already in the new list

or just check the list each time we want to add something it

create a new list

add the element from data to the newlist if the element is not already
in the new list

'''