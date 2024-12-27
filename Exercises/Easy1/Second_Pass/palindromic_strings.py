def is_palindrome(string):
    '''
    write a function that returns true if the argument is a palindrome and False otherwise

    requirements:
        - case matters and all characters matter
    '''
    return string[::-1] == string

def is_real_palindrome(string):
    '''
    function should be case-insensitive

    should ignore all non-alphanumeric letters
    '''

    stripped = ''

    for char in string:
        if char.isalnum():
            stripped += char

    return stripped.lower() == stripped[::-1].lower()


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True