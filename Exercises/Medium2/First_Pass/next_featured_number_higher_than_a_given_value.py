MAX_FEATURED = 9876543201

def next_featured(num):
    '''
    takes a number as an argument and returns the next featured number greater
    than the integer. issues an error message if there is no next featured number
    '''

    featured_num = num + 1

    while not is_valid(featured_num):
        featured_num += 1
        if featured_num > MAX_FEATURED:
            return "There is no possible number that fulfills those requirements."

    return featured_num

def is_valid(number):
    '''
    a valid number is
        - odd
        - multiple of 7
        - all of its digits occur exactly once each
    '''
    if number % 2 == 0:
        return False
    if number % 7 != 0:
        return False
    if len(set(str(number))) != len(str(number)):
        return False
    
    return True

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True