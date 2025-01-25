def fibonacci(n):
    '''
    fibonacci sequence, recursively

    base case: if n is 1 or 2, return 1
    '''

    if n < 1:
        return
    
    if n in [1, 2]:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(60))