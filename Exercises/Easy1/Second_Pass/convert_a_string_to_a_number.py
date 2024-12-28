'''
function that takes a string of digits and returns the appropriate number as an
integer. you may not use any of the standard conversion functions available in
python such as int.
'''

CODE_POINT_DIFFERENCE = 48

def string_to_integer(string):
    '''
    convert to code point
    use the difference between the code point and actual value to arrive at the
    value

    once we have converted to the integer, we need to put the integer in the right
    digits place. so for the first digit of number 4321, 4 is multiplued by 1000.
    the length of the string is 4, so we can put 10 to the power of (4-1 = 3) to arrive at 
    1000. for the second digit, 3, 3 is multiplied by 10 to the power of (4-2 = 2)

    skipping to the last digit, 1, 1 is multiplied by 10 to the power of (4-4 = 0).

    each multiplication is added to the running sum to obtain the final number
    '''

    running_sum = 0
    power_of_10 = len(string) - 1

    for digit in string:
        int_digit = ord(digit) - CODE_POINT_DIFFERENCE
        running_sum += int_digit * 10**power_of_10
        power_of_10 -= 1

    return running_sum

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(string):
    '''
    use a dict to store the hexadecimal values


    '''

    HEX_VALUES = {
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
        'a': 10,
        'B': 11,
        'b': 11,
        'C': 12,
        'c': 12,
        'D': 13,
        'd': 13,
        'E': 14,
        'e': 14,
        'F': 15,
        'f': 15,
    }

    power_of_16 = len(string) - 1
    running_sum = 0

    for digit in string:
        int_digit = HEX_VALUES[digit]
        running_sum += int_digit * 16**power_of_16
        power_of_16 -= 1

    return running_sum

# print(hexadecimal_to_integer('4D9f') == 19871)  # True