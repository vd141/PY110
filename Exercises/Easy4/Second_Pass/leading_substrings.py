def leading_substrings(string1):
    '''
    takes a string argument and returns a list of substrings of that
    string. each substring should begin with the first letter
    of the word, and the list should be ordered from shortest to longest
    '''

    substrings = []

    for idx in range(1, len(string1) + 1):
        substrings.append(string1[:idx])

    return substrings

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])