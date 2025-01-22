def is_prime(num):
    '''
    returns True or False depending on whether the number is prime
    '''

    if num == 1:
        return False
    if num == 4:
        return False
    # check numbers up to half of the current numbers. if num % number == 0, the
    # number is not prime. if we get to the halfway point and no mod == 0,
    # the number is prime

    # faster algorithm is to use the squareroot instead of the midpoint

    midpoint = num // 2

    for check_me in range(2, midpoint):
        if num % check_me == 0:
            return False
        
    return True


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True