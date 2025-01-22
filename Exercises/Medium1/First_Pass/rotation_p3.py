from rotation_p2 import rotate_rightmost_digits

def max_rotation(num):
    '''
    get the maximum rotation of the input number
    '''

    num_str = str(num)

    for idx in range(len(num_str), 1, -1):
        num = rotate_rightmost_digits(num, idx)

    return num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True