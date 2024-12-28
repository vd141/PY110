'''
write a function that converts a non-negative integer to the string representation
of that integer

the divmod function is helpful
'''

CODE_POINT_DIFFERENCE = 48

def integer_to_string(integer):
    '''
    using the divmod function, i pass in the integer as the first argument and 10 
    as the second

    the second element of the tuple output is the resulting digit

    the first digit of the tuple output is the first argument for the next call of
    divmod

    convert digit to string by taking the chr() of that digit + the code point
    difference (48)


    '''

    if integer == 0:
        return chr(48)

    running_string = ''

    while integer != 0:
        integer, digit = divmod(integer, 10)
        str_digit = chr(digit + CODE_POINT_DIFFERENCE)
        running_string = str_digit + running_string

    return running_string

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True