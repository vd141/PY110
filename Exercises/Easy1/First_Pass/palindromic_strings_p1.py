'''
return True if string is a palindrome, False otherwise
'''

# def is_palindrome(string):
#     '''
#     to reverse a string, convert to list, reverse, then use string join method
#     '''
#     listed_string = list(string)
#     listed_string.reverse()
#     reversed_string = ''.join(listed_string)
#     return True if (string == reversed_string) else False

'''
easier way
'''

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('banana'))
print(is_palindrome('abba'))