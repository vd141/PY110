'''
P - understand the Problem
    1. write down inputs
    2. write down outputs
    3. write down explicit requirements
    4. write down implicit requirements

E - Examples / Test Cases
    - glean requirements from test cases
    - ask prompter to clarify problem if needed

D - Data Structures
    - 

A - Algorithms
C - Code

'''


"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

'''
inputs: string
outputs: list of palindromic substrings that are 2 or more characters long

explicit requirements:
    - palindromic detection should be case sensitive 'aaAa' is not a palindrome but
      'AaaA' is
    - an empty list is returned when the string is empty or has no palindrome
    - palindrome must be at least 2 characters long

implicit requirements:
    - palindromes can be subsets of other palindromes


This looks like all the requirements based on the problem description and 
test cases. are there any requirements you would like me to add?
'''