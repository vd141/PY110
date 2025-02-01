LARGEST_FEATURED = 9876543201

def next_featured(num):
    '''
    a featured number is an odd number that is a multiple of 7, with all of its
    digits occurring exactly once

    input: a positive integer
    output: returns next featured number greater than input. or error message if
    no such number exists

    data structure:
        - none atm

    algorithm:
        - loop through all numbers between num + 1 and the LARGEST_FEATURED
            - can optimize by only looping through multiples of 7
            - once we encounter a number that is a multiple of 7, we can update a
            gap variable to change the interview between candidates
        - determine if a number is a featured number (helper function)
    '''
    
    gap = 1
    candidate = num + 1

    while True:
        if is_featured(candidate):
            return candidate
        if candidate > LARGEST_FEATURED:
            return 'There is no possible number that fulfills those requirements.'
        if candidate % 7 == 0:
            gap = 7
        candidate += gap
        

def is_featured(num):
    unique_digits = len(str(num)) == len(set(str(num)))
    mult_of_7 = num % 7 == 0
    odd = num % 2 != 0

    return True if unique_digits and mult_of_7 and odd else False

print(is_featured(7))
    

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