def triangle(side1, side2, side3):
    '''
    input: 3 integer sides
    output: string describing type of triangle

    requirements:
        - a valid triangle has:
            - sum of the 2 shorter sides must be greater than longest side
            - every side must have a length greater than 0
        - equilateral:
            - all 3 sides have the same length
        - isosceles:
            - two sides have the same length, while the third is different
        - scalene:
            - all three sides have different lengths

    if the triangle is valid, determine what type of triangle it is
        - to check validity:
            - check if any of the sides are 0. if so, return 'invalid'
                - if 0 in the list of sides
            - sum of two shorter sides must be lnoger than longest side
                - get longest side by finding the max of the three sides
                - get sum of all three sides and subtract the max from the sum
                    - if the result is less than or equal to the max, return False
        - to check for equilateral, check for equivalence between all three sides
        - to check for isoceles, check that the length of the set of all three sides is 2
        - to check for scalene, check that the length of the set of all three sides is 3
    '''
    if is_valid(side1, side2, side3):
        set_of_sides = set([side1, side2, side3])
        if len(set_of_sides) == 1:
            return 'equilateral'
        if len(set_of_sides) == 2:
            return 'isosceles'
        if len(set_of_sides) == 3:
            return 'scalene'
    else:
        return 'invalid'

def is_valid(side1, side2, side3):
    sides = [side1, side2, side3]
    if 0 in sides:
        return False
    longest = max(sides)
    perim = sum(sides)
    if perim - longest > longest:
        return True
    return False

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True