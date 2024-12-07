'''
Create a string from the list's elements

The join method only accepts collections of strings, so we can coerce each element
in the list into a string
'''
numbers = [1, 2, 3, 4]
# goal: string_version = '1234'

string_version = ''.join([str(number) for number in numbers])

'''
What is a set?

an unordered collection of data. it can't be indexed, but membership can be checked.
sets are mutable, but the individual members must be immutable
'''