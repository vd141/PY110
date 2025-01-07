def triangle(ang1, ang2, ang3):
    '''
    return whether the triangle is right, acute, obtuse, or invalid
    '''

    angles = [ang1, ang2, ang3]

    if sum(angles) != 180:
        return 'invalid'
    if min(angles) <= 0:
        return 'invalid'
    if 90 in angles:
        return 'right'
    if max(angles) < 90:
        return 'acute'
    if max(angles) > 90:
        return 'obtuse'
    

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True