def rotate_rightmost_digits(number, count):
    '''
    rotates the last 'count' digits of a number. to perform the rotation, 
    move the first of the digits that you want to rotate to the end and
    shift the remaining digits to the left

    convert the number to a string
    use string slicing with the count variable to get the number we want to
    rotate (the substring)
    use string slicing to with the count variable to get the number we do not
    want  to rotate (to be used later)
    rotate the substring by concatenating the first substring of the substring
    to the remaining chars of the substring
    concatenate this new substring to the unrotated chars
    convert this new string to an int
    return int
    '''

    number_str = str(number)
    unrotated = number_str[:-count]
    rotate_me = number_str[-count:]
    rotated = rotate_me[1:] + rotate_me[0]
    return int(unrotated + rotated)

# rotate_rightmost_digits(735291, 2)  # True
# rotate_rightmost_digits(735291, 3)  # True
# rotate_rightmost_digits(735291, 1)  # True
# rotate_rightmost_digits(735291, 4)  # True
# rotate_rightmost_digits(735291, 5)  # True
# rotate_rightmost_digits(735291, 6)  # True
# rotate_rightmost_digits(1200, 3)    # True

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True