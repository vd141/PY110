def digit_list(integer):
    '''
    takes a positigve integer and returns a list of digits in the number
    '''

    list_of_digits = list(str(integer))
    return [int(elem) for elem in list_of_digits]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True