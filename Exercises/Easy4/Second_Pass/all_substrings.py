from leading_substrings import leading_substrings

def substrings(full_string):
    '''
    returns a list of all substrings of a string

    call the leading substrings function on each substring of the full_string

    to get each substring of the full string, increment from idx = range(len(full_string)) of full_string[idx:]
    '''

    substring_list = []

    for idx in range(len(full_string)):
        substring_list.extend(leading_substrings(full_string[idx:]))

    return substring_list

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True