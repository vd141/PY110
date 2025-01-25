fib_dict = {
    1: 1,
    2: 1,
}

def fibonacci(n):
    '''
    using memoization

    create a dict to store base cases

    store this dict outside the function and update it in the function

    if n in fib dict, return the value

    if n not in the fib dict, calculate the value and store it in fib_dict

    '''

    if n < 1:
        return
    
    if n in fib_dict:
        return fib_dict[n]
    
    fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return fib_dict[n]
    


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(60))