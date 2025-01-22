memo = {
        1: 1,
        2: 1,
    }

def fibonacci(nth):
    '''
    to implement memoization, use a dict to store previously calculated values.
    store the first two 
    '''
    
    #if memo[n-1] exists, grab the value. otherwise, calculate it
    # if memo[n-2] exists, grab the value. otherwise, calculate it

    if nth <= 2:
        return memo[nth]
    elif nth in memo:
        return memo[nth]

    memo[nth] = memo.get(nth - 1, fibonacci(nth - 1)) + memo.get(nth - 2, fibonacci(nth - 2))

    return memo[nth]



print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(120))