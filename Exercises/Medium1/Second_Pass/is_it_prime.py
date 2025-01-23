def is_prime(number):
    '''
    returns True if number is prime, False otherwise

    Requirements: 
        - a prime number is a positive number
        - evenly divisible by only itself and one
        - 1 is not prime

    cycle through all numbers from 2 to the square root of the number to see if
    the number is divisible by any. if it is, return False. otherwise, if the 
    square root is reached and no other factor divides the number, return True
    '''

    if number == 1:
        return False

    for factor in range(2, int(number**(1/2) + 1)):
        if number % factor == 0:
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