def max_rotation(num):
    '''
    rotate the full string, then rotate the next largest substring (from the rear),
    then the next largest substring, and so on until the entire number has been rotated

    convert the entire number to a string
    then run the rightmost rotation function on that string
    then run the rightmost rotation function on the next largest substring
    and so on until the end of the string is reached

    use the rotate_rightmost_digits function from the previous exercise

    count will at first be the length of the entire number. it will be decremented
    each loop iteration until the count is 0
    '''

    rotated_num = num

    for last_digits in range(len(str(num)), 0, -1):
        rotated_num = rotate_rightmost_digits(rotated_num, last_digits)

    return rotated_num

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

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True