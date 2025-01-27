def triangle(side1, side2, side3):
    '''
    takes the lengths of the three sides of a triangle as arguments and returns
    one of the following four strings representing the triangle's classification
        - equilateral
        - isoceles
        - scalene
        - invalid

    store sides in a set

    a valid triangle has:
        - sum of the lengths of the two shortest sides > length of the longest
          side
            - use max function to get the longest of the three sides
            - use set operation to get the remaining two sides
            - sum the remaining two sides to determine if it is larger than the
              max
        - every side must have length greater than 0
            - return invalid if one of the lengths is lessthan or equal to 0

    if side1 == side2 == side3, then it is equilateral

    if two sides are of the same length and the third is different, isoceles

    if all three sides have different lengths, it is scalene

    determine if the triangle is valid first
        - if it is, then determine if it is one of the three types
    '''

    if not is_valid(side1, side2, side3):
        return 'invalid'
    
    sides = {side1, side2, side3}

    match len(sides):
        case 1:
            return 'equilateral'
        case 2:
            return 'isosceles'
        case 3:
            return 'scalene'
    


def is_valid(side1, side2, side3):
    if side1 <= 0:
        return False
    if side2 <= 0:
        return False
    if side3 <= 0:
        return False
    sides = [side1, side2, side3]
    longest = max(sides)
    sides.remove(longest)
    if sum(sides) >= longest:
        return True
    return False

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True