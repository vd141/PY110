def fibonacci(number):
    '''
    each number is the sum of the previous two numbers
    '''

    fib_dct = {
        1: 1,
        2: 1,
    }

    for fib_entry in range(3, number + 1):
        fib_dct.update({fib_entry: fib_dct[fib_entry - 1] + fib_dct[fib_entry - 2]})

    return fib_dct[number]

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