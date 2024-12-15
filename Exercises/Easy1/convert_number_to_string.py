'''
make the conversion without using the str() function
'''

INT_TO_STRING = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

def integer_to_string(integer):
    '''
    append each digit to a list. str join method to convert the list into a string
    '''
    int_list = []
    previous_divmod = None
    current_divmod = divmod(integer, 10)

    while current_divmod != previous_divmod:
        int_list.append(INT_TO_STRING[current_divmod[1]])
        previous_divmod = current_divmod
        current_divmod = divmod(current_divmod[0], 10)

    int_list.reverse()
    if len(int_list) > 1:
        int_list.pop(0)


    return ''.join(int_list)


# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True