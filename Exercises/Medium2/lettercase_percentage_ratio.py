import string

def letter_percentages(string_):
    '''
    takes a string and returns a dict containing the following three properties:
        - percentage of characters in teh string that are lowercase letters
        - percentage of characters that are uppercase letters
        - percentage of characters that are neither

    each value should be rounded to two decimal points
    '''

    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0
    str_len = len(string_)

    for char in string_:
        if char in string.ascii_lowercase:
            lowercase_count += 1
        elif char in string.ascii_uppercase:
            uppercase_count += 1
        else:
            neither_count += 1

    lowercase_ratio = (lowercase_count / str_len) * 100
    uppercase_ratio = (uppercase_count / str_len) * 100
    neither_ratio = (neither_count / str_len) * 100

    return {
        'lowercase': f'{lowercase_ratio:.2f}',
        'uppercase': f'{uppercase_ratio:.2f}',
        'neither': f'{neither_ratio:.2f}'
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)