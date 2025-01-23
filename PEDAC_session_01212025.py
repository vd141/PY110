'''
PEDAC Notes
"""
P - Understanding the Problem:
- Goal: understand what you're being asked to do
  - Read the problem description
  - Identify expected input and output
  - Establish rules/requirements/define the boundaries of the problem
  - Ask clarifying questions
  - Take your time on this step!

E - Examples and Test Cases:
- Goal: further expand and clarify understanding about what you're being asked to do 
  - Use examples/test cases to confirm or refute assumptions made about the problem in the previous step

D - Data Structures:
- Goal: begin to think logically about the problem
  - What data structures could we use to solve this problem?
    - What does our data look like when we get it? (input)
    - What does our data look like when we return it? (output?)
    - What does our data need to look like in the intermediate steps?

A - Algorithm:
- Goal: write out steps to solve the given problem in plain English
  - A logical sequence of steps for accomplishing a task/objective
  - Start high level, but make sure you've thought through and have provided sufficient detail for working through the most difficult parts of the problem
  - Stay programming-language-agnostic
  - Can create substeps for different parts or separate concerns into a helper method
  - You can (and should) revisit your algorithm during the implementation stage if you need to refine your logic
  - Before moving onto implementing the algorithm, check it against a few test cases

C - Implementing a Solution in Code:
- Goal: translate the algorithm into your programming language of choice
  - Code with intent. Avoid hack and slash 
- TEST FREQUENTLY
  - Use the REPL or run your code as a file
  - When testing your code, always have an idea in place of what you're expecting
  - If you find that your algorithm doesn't work, return there FIRST if needed and THEN fix your code
"""
'''


"""
We're receiving a set of messages in code. The messages are sets of text strings, like:
"alakwnwenvocxzZjsf"
Write a method to decode these strings into numbers. The decoded number should be the number of lowercase characters between the first two uppercase characters. If there aren't two uppercase characters, the number should be 0.

Test cases:
print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])
"""

'''
Inputs: list of messages (strings)
Outputs: list of numbers

requirements:
    - each number is the number of lowercase characters between the first two uppercase characters
    - if there aren't 2 uppercase characters, the number should be zero

a list of messages can be any length
a message can be any length

helper function to calculate the number for each message
    - loop through each character of the message
    - initialize two index variables (indexes of the two uppercase characters) to None
    - if the character is upper, reassign the first index variable to that index
    - if the character is upper, reassign the second index variable to that index
    - break the loop after second index variable has been reassigned
    - after looping through the message, check to see if either of the index variables are None
    - if either of the index variables are None, then return 0
    - if both index variables have been reinitialized, then we use string slicing
    - to grab the substring between both indexes
    - get the lnegth of that substring and return that

in the main function, loop through each of the input lists elements. then run the helper function 
on each message



'''

def decode(messages):
    return [decode_message(message) for message in messages]

def decode_message(message):
    first_index = None
    second_index = None

    for idx, char in enumerate(message):
        if char.isupper() and first_index is None:
            first_index = idx
        elif char.isupper() and second_index is None:
            second_index = idx
            break
        
    if None in [first_index, second_index]:
        return 0
        
    real_message = message[first_index + 1: second_index]

    return len(real_message)

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])

'''
string slicing not needed

update high level algorithm if new insights gained in later steps
'''