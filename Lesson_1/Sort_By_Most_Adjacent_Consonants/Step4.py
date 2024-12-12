'''
4. Algorithms


'''

'''
loop through the original string
    determine the number of adjacent consonants in a string
    store the number of adjacent consonants in a dict
sort the keys in the dict by value (descending)
    store each key in a new list

the challenge will be to sort the dict keys
    - we know as of python 3.7, dicts store keys by order of insertion
    - loop through the dict and sort by value (descending)

determine the number of adjacent consonants in a string
    - inputs: string
    - outputs: max number of adjacent consonants

    algorithm: loop through string characters
        - initialize consonant count to 0
        - initialize max consonant count to 0
        - if character is consonant, increase the consonant count by 1
        - if consonant count is greater than max consonant count, update max consonant count
        - if the character is a non-consonant (but not a space), reset consonant count to 0
        - if the character is a space, continue to the next loop iteration (do nothing)

        - at the end of the loop, if the max consonant count is 1, return 0. if the 
          max consonant count is greater than or equal to 2, return that number

test cases:
    'abe': 0
    'aberdeen': 2
    'mylo zyloto: 3
    'bring the rock': 3
'''