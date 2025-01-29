LARGEST_FEATURED = 9876543201

def next_featured(num):
    '''
    featured number is 
        - an odd number that is a multiple of 7
        - all of its digits occur exactly once each
    largest possible featured number is 9876543201
    
    takes an integer as an argument and returns the next featured number
    greater than the integer. issues an error message if there is no next
    featured number

    inputs: an integer
    outputs: an integer

    data structures:
        - none

    algorithms:
    starting from num + 1, check each number to see if it is a multiple of 7
    and if all of its digits occur exactly once each, and if it is odd
        - use mod to check if multiple of 7
        - convert to string and compare string length to length of set of
          string

    to optimize the algorithm, we don't have to check every single number above
    the input. instead once we find an odd multiple of 7, we can check every 14
    numbers from that number
    '''

    check_num = num + 1

    while True:
        if check_num > LARGEST_FEATURED:
            return 'There is no possible number that fulfills those requirements.'
        if check_num % 7 == 0 and check_num % 2 != 0:
            if len(str(check_num)) == len(set(str(check_num))):
                return check_num
            check_num += 14
            continue
        check_num += 1

    

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