TRIANGLE_SUM_ANGLE = 180

def triangle(ang1, ang2, ang3):
    '''
    right: one angle is a right angle (exactly 90 deg)
    acute: all three angles are less than 90 deg
    obtuse: one angle is greater than 90 deg

    valid triangle:
        - sum of angles must be exactly 180 deg
        - every angle must be greater than 0

    if the triangle is valid, determine what type of triangle it is

    input: 3 angles
    output: string of triangle type

    Data structures:
        - list of angles

    to determine validity:
        - evaluate sum of angles
        - check to see if angles are greater than 0

    right:
        - check if 90 is in the list of angles
    acute:
        - check if angle is less than 90 deg (use subfunction)
        - subfunction evaluates one angle and returns true if it is less than 90 deg
        - use a list comprehension of the subfunction evaluating each angle
        - use all() to determine if the subfunctino returned true for all angles
    obtuse:
        - check if angle is greater than 90 deg(use subfunction)
        - subfunction evaluates one angle and returns true if it is greater than 90 deg
        - use a list comprehension of the subfxn evaluating each angle
        - use any() to determine if the subfunction returned True for any angle

    '''

    list_angles = [ang1, ang2, ang3]

    if is_valid(list_angles):
        if is_right(list_angles):
            return 'right'
        if all([is_acute(angle) for angle in list_angles]):
            return 'acute'
        if any([is_obtuse(angle) for angle in list_angles]):
            return 'obtuse'
    else:
        return 'invalid'

def is_valid(list_angles):
    if sum(list_angles) != TRIANGLE_SUM_ANGLE:
        return False
    if any([not valid_angle(angle) for angle in list_angles]):
        return False
    return True
    
def valid_angle(angle):
    if angle > 0:
        return True
    return False

def is_right(list_angles):
    if 90 in list_angles:
        return True
    return False

def is_acute(angle):
    return True if angle < 90 else False

def is_obtuse(angle):
    return True if angle > 90 else False

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True