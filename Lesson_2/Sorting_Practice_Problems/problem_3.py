'''
sort the list as string values

[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst_as_str = list(str(elem) for elem in lst)

lst_as_str.sort()

print([int(elem) for elem in lst_as_str])

lst_as_str.sort(reverse=True)

print([int(elem) for elem in lst_as_str])

# alternate, cleaner version

lst.sort(key=str)
print(lst)

lst.sort(key=str, reverse=True)
print(lst)
