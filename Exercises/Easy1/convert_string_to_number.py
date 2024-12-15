'''
write a function that takes a string of digits and returns the appropriate number
as an integer. you may not use any of the standard conversion functions available
in python, such as int. your function should calculate the result by using the
characters in the string

assume all characters are numeric
'''

def string_to_integer(num_string):
    '''
    run ord function on single character string
    convert unicode version of string to digit: string 1 is unicode 49
    unicode:
        - 0: 48
        - 1: 49
        ...
        - 9: 57
    
    subtract 48 from ord() output to get true value
    if length of the string is 4, we multiply the true value by 10^(len(str) - current_digit)
    then add that to the integer
    '''
    OFFSET = 48

    final_number = 0

    nth_digit = 1
    for digit in num_string:
        true_value = ord(digit) - OFFSET
        factor = 10**(len(num_string) - nth_digit)
        final_number += true_value * factor
        nth_digit += 1

    return final_number

def hexadecimal_to_integer(number_string):
    HEX_TO_DECIMAL = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }

    running_total = 0
    hexponent = 0

    for char in number_string[::-1]:
        running_total += HEX_TO_DECIMAL[char] * 16**hexponent
        hexponent += 1
    
    return running_total
