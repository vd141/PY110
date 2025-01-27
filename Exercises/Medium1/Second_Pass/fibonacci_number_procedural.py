def fibonacci(num):
    '''
    keep track of the two fibonacci numbers needed for the next fibonacci number

    one number will be called previous
    the other will be called current

    next will be calculated from the sum of previous and current

    previous then gets current and current then gets next

    return current

    the first calculated value of next is the 3rd number in the sequence

    the first two fibonacci numbers are 1 and 1

    increment the index after we calculate the next fibonacci number. if the
    index matches num, then we return the fibonaci number
    '''

    previous = 1
    current = 1
    index = 3

    if num in [1, 2]:
        return 1

    while True:
        next = previous + current
        previous, current = current, next
        if index == num:
            return next
        index += 1

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