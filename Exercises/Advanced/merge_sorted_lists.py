def merge(list1, list2):
    '''
    takes two sorted lists as arguments and returns a new list that contains all
    the elements from both input lists in ascending sorted order. you may assume
    that the lists contain either all integer values or all string values

    the solution cannot sort the resulting list

    iterate through each element of both lists. each element is a candidate

    compare candidates. if one is less than the other, add that to the list.

    update the candidate that was just added to point to the next value in that
    list

    if one of the indexes reaches the end of its respective list, append the rest
    of the remaining list to the new list
    '''

    merged = []

    list1_idx = 0
    list2_idx = 0

    while True:
        if not list1 or not list2:
            merged.extend(list1)
            merged.extend(list2)
            break
        if list1[list1_idx] < list2[list2_idx]:
            merged.append(list1[list1_idx])
            list1_idx += 1
        else:
            merged.append(list2[list2_idx])
            list2_idx += 1
        if list1_idx >= len(list1):
            merged.extend(list2[list2_idx:])
            break
        if list2_idx >= len(list2):
            merged.extend(list1[list1_idx:])
            break

    return merged

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)