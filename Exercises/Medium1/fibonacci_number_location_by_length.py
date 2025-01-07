import sys

sys.set_int_max_str_digits(50_000)

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

def find_fibonacci_index_by_length(num):
    '''
    run the fibonacci sequence with increasing numbers until the str length of
    the output matches what we want
    '''
    iterator = 1
    while len(str(fibonacci(iterator))) < num:
        iterator += 1
    return iterator


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)