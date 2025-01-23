def fibonacci(nth):
    '''
    sequence of numbers in which each number is the sum of the previous two nums
    the first two fib numbers are 1 and 1. the third number is 2

    returns the nth fibonacci number

    if nth is 1 or 2, return 1

    if nth is greater than 1 or 2, calculate that number

    keep track of two addends by using the variables f_1 and f_2. f_1 stores
    the last fibonacci number, f_2 stores the second to last fib number

    f_1 initializes at 1, f_2 initializes at 1. if nth is 3, the fib is f_2 + f_1

    if nth is 4, f_2 gets the current value of f_1 and f_1 gets the value of the
    sum of f_1 and f_2
    '''

    if nth in [1, 2]:
        return 1
    
    f_1 = 1
    f_2 = 1
    new_fib = None

    for _ in range(3, nth + 1):
        new_fib = f_1 + f_2
        f_2 = f_1
        f_1 = new_fib

    return new_fib

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