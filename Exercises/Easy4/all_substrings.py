from leading_substrings import leading_substrings

def substrings(string):
    '''
    write a function that returns a list of all substrings of a string. 
    '''

    substrings = []

    for starting_index in range(len(string)):
        input_string = string[starting_index:]
        substrings.extend(leading_substrings(input_string))

    return substrings


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde'))
print(substrings('abcde') == expected_result)  # True