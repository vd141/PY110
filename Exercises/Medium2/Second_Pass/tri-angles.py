def triangle(ang1, ang2, ang3):
    '''
    right: one angle is exactly 90
    acute: all three angles are less than 90
    obtuse: one angle is greater than 90

    requirements:
        - a valid triangle:
            - sum of angles must be exactly 180 degrees
            - every angle must be greater than 0
    '''

    if not is_valid(ang1, ang2, ang3):
        return 'invalid'
    
    angles = [ang1, ang2, ang3]
    
    if 90 in angles:
        return 'right'
    
    if len([angle for angle in angles if angle < 90]) == 3:
        return 'acute'
    
    if len([angle for angle in angles if angle > 90]) == 1:
        return 'obtuse'


def is_valid(ang1, ang2, ang3):
    if sum([ang1, ang2, ang3]) != 180:
        return False
    if ang1 <= 0:
        return False
    if ang2 <= 0:
        return False
    if ang3 <= 0:
        return False
    return True

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True