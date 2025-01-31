'''
Alphabet Symmetry
Consider the word "abode".
The letter `a` is in position 1 and `b` is in position 2.
In the alphabet, `a` and `b` are also in positions 1 and 2.

The letters `d` and `e` in "abode" occupy the positions they would occupy in the alphabet, which are positions 4 and 5. 

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) // [4, 3, 1]

Input will consist of alphabetic characters, both uppercase and lowercase. No spaces.

--------------------------------------------------------------------------------

requirements:
    - does the input always have a string in it?
    - do strings only contain alphabetic characters?
    - will strings ever be empty?

counts the number of in-place characters in a given string

input: list of alphabetic strings
output: list of counts of in-place letters for each string

data structures:
    - alphabet string

algorithms:
  - initialize an empty output list
  - loop through the list to parse each string
  - initialize a counter variable to equal 0
  - go through each character of the string
  - compare each character to the alphabet string using indexing
  - convert each character to the same case 
  - if characters match, increment our counter
  - at the end of the string, append the counter to the output list
  - repeat above steps for next string

  - can use a helper function to return the count of each string



'''

ALPHABET = 'abcdefghijklmnopqrstuv'

def solve(messages):
    return [count_in_place(string) for string in messages]

def count_in_place(string):
    
    counter = 0

    for idx, char in enumerate(string):
        if ALPHABET[idx].casefold() == char.casefold():
            counter += 1
    
    return counter


print(count_in_place('abode'))

# Python test cases
print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True
