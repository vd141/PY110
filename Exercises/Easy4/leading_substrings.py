def leading_substrings(string):
    '''
    returns a list of substrings of the input string. each substring begins with
    the first letter of the word. list is ordered from shortest to longest

    loop through the final index of each substring that
    '''

    return [string[:final_idx + 1] for final_idx in range(len(string))]

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('abc'))
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])