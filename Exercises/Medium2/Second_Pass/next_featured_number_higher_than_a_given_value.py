LARGEST_FEATURE = 9876543201

def next_featured(num):
    '''
    inputs: an int
    outputs: an int

    requirements:
        - output must be 
            - odd
            - multiple of 7
            - all digits occur exactly once each
        - returns next featured number greater than the integer

    compare length of str(num) to set(str(num)). if they are the same
    length, all digits are unique

    multiple of 7 can be determined by candidate % 7 == 0

    odd can be determined by candidate % 2 != 0

    starting at num + 1 as the candidate, test each candidate to determine
    if it is a multiple of 7. once a multiple of 7 has been determined,
    determine if it is odd. if it is, test if all digits occur exactly once. if not,
    increment candidate by 7. 
    '''

    candidate = num + 1

    while candidate < LARGEST_FEATURE:
        if candidate % 7 == 0:
            if candidate % 2 != 0:
                if len(str(candidate)) == len(set(str(candidate))):
                    return candidate
                candidate += 14
            candidate += 7
        candidate += 1
    
    return "There is no possible number that fulfills those requirements."

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