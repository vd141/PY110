'''
return True if palindrome, False otherwise

Function should be case-insensitive, and should ignore all non-alphanumeric characters

simplify things by calling the is_palindomre function
'''

def is_real_palindrome(string):
    '''
    reverse string

    remove non alphanumeric characters from both strings
    use string method to join a comprehension

    casefold both strings
    '''

    reversed_string = string[::-1]

    string_alphanum = ''.join(char for char in string if char.isalnum())

    reversed_string_alphanum = ''.join(char for char in reversed_string if char.isalnum())

    return string_alphanum.casefold() == reversed_string_alphanum.casefold()







print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True