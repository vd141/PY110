import string

def double_consonants(string_):
    '''
    function that takes a string, doubles every consonant in the string, and returns
    the result as a new string. the functino should not double vowels, digits, 
    punctuation, or whitespace
    '''

    unallowed = (['a', 'e', 'i', 'o', 'u'] + list(string.digits) + 
                 list(string.punctuation) + list(string.whitespace))

    new_str = ''

    for char in string_:
        if char not in unallowed:
            new_str += char * 2
        else:
            new_str += char

    return new_str

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")