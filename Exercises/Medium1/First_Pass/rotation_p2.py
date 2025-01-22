def rotate_rightmost_digits(num1, num2):
    '''
    write a function that rotates the last count digits of a number. to perform
    the rotation, move the first of the digits that you want to rotate to the end
    and shift the remaining digits to the left
    '''
    dont_rotate_me = str(num1)[:-num2]
    rotate_me = str(num1)[-num2:]
    return int(dont_rotate_me + rotate_string(rotate_me))

def rotate_string(string):
    '''
    takes the first element of the string and moves it to the back. if the string
    is length 1 or 0, returns the string
    '''
    if len(string) in [0, 1]:
        return string
    return string[1:] + string[0]

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True