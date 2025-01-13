VOWELS = 'aeiouAEIOU'

def remove_vowels(list_of_strings):
    '''
    takes a list of strings and returns a list of the same string values, but
    with all vowels removed
    '''

    removed_vowels = []

    for string_ in list_of_strings:
        new_word = ''
        for char in string_:
            if char not in VOWELS:
                new_word += char
        removed_vowels.append(new_word)

    return removed_vowels

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True