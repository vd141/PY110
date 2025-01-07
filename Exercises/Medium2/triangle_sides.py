def triangle(side1, side2, side3):
    '''
    to be a valid triangle, the sum of the lengths of the two shortest sides
    must be greater than the length of the longest side, and every side must
    have a length greater than 0. if either of these conditions is not satisfied,
    the triangle is invalid
    '''

    sorted_sides = sorted([side1, side2, side3])

    if min(sorted_sides) <= 0:
        return 'invalid'
    if side1 == side2 == side3:
        return 'equilateral'
    if sorted_sides[0] + sorted_sides[1] <= sorted_sides[2]:
        return 'invalid'
    if len(set(sorted_sides)) == 2:
        return 'isosceles'
    return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True