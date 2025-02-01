def fibonacci(index):
    '''
    first two fibonacci numbers are 1. every subsequent number is the sum of the
    two preceding numbers. so the third fibonacci number is 1 + 1 = 2. the fourth 
    fibonacci number is 2 + 1. 

    requirements:
        - function returns the num (input) th fibonaci number
        - num is assumed to be positive
        - num is assumed to be an integer

    input:
        - integer (fibonacci index)
    output:
        - integer (fibonacci number)

    data structures:
        - none

    algorithm:
        - if the index is 1 or 2, return 1
        - otherwise, calculate the fibonacci number until the input index is reached
        - use a variable to keep track of the current fibonacci index
        - use a variable to keep track of the current and previous addend.
        - update the current and previous addend when a new fibonacci number is
          calculated
        - if index is reached, return the fibonacci number
    '''

    if index in [1, 2]:
        return 1
    
    previous = 1
    current = 1
    current_index = 3

    while True:
        next = current + previous
        previous, current = current, next
        if current_index == index:
            return next
        current_index += 1

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True