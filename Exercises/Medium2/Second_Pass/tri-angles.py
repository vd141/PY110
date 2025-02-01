TRIANGLE_SUM_ANGLE = 180

def triangle(ang1, ang2, ang3):
    '''
    return triangle type (acute, right, obtuse), invalid if otherwise

    an valid triangle:
        - sum of the angles is 180 deg
        - every angle is greater than 0

    an acute triangle
        - has all angles less than 90 deg

    right triangle
        - has one 90 deg angle

    obtuse triangle:
        - has one angle greater than 90 deg

    inputs: 3 angles (integers, positive)
    outputs: string of triangle type

    data structures:
        - none at the moment

    algorithm:
        - determine if triangle is valid (sep function)
            - if sum != 180, invalid
            - if 0 in list of angles, invalid
        - if it is, determine what type of triangle it is
        - check if there is a 90 deg angle, -> right
        - check if there is an angle greater than 90 deg, -> obtuse
        - otherwise, acute 
    '''

    angles = [ang1, ang2, ang3]

    if is_valid(angles):
        if 90 in angles:
            return 'right'
        elif any([angle > 90 for angle in angles]):
            return 'obtuse'
        else:
            return 'acute'
    return 'invalid'

def is_valid(angles):
    if sum(angles) != 180 or 0 in angles:
        return False
    return True


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True