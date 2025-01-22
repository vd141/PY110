def fibonacci(nth):
    if nth == 1:
        return 1
    if nth == 2:
        return 1
    
    return fibonacci(nth - 1) + fibonacci(nth - 2)


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True