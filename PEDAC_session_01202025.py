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