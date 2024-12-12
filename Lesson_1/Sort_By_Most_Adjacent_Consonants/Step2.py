'''
2. Examples and Test Cases

You are provided with the following test cases:

Observations: 
    - strings are sorted in descending order of adjacent consonant count
    - a string must have at least two adjacent consonants to be sorted
    - if strings have an equal number of adjacent consonants, they retain their relative order

    The test cases answer the question of whether the list should be in ascending
    or descending order. But, a few questions remain:

    - are two consonants considered adjacent if they are separated by a whitespace
      that is not a space? (\n, for example)
    - should we assume the input list has at least one element?
    - should we assume the input list has only strings?
    - will the strings have non alphabetic non-whitespace characters such as commas and numbers?
        - if so, how should these be treated?
    - is y considered a consonant?

    these remainign questions should be asked of the interviewer. but for the purposes
    of this written exercise, i will assume:
        - input strings will only have one type of whitespace: a space
        - input list has at least one element
        - input list has only strings
        - strings will not contain special characters such as commas and numbers

Updated (additional) requirements:
    - strings are sorted in descending order of adjacent consonant count
    - a string must have at least two adjacent consonants to be sorted
    - if strings have an equal number of adjacent consonants, they retain their relative order
    - input strings will only have one type of whitespace: a space
    - input list has at least one element
    - input list has only strings
    - strings will not contain special characters such as commas and numbers
    - y will be considered a consonant
'''
def sort_by_consonant_count(my_list):
    pass

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

