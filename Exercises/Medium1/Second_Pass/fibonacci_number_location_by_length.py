import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    '''
    returns the index of the first fibonacci number whose digit count equals 
    length

    input: positive int
    output: fibonacci number meeting requirement

    data structures: 
        - none at the moment

    algorithm:
        - if the input is 1, return 1
        - otherwise, begin calculating fibonacci numbers (can reuse earlier fib
          fxn)
        - use procedural fibonacci calculation
        - use str() to convert fibonacci output to an iterable with a length
        - evaluate the string's length. if it is equal to the input, return
          the integer version of the fibonacci number
    '''

    if length == 1:
        return 1
    
    previous = 1
    current = 1
    index = 3

    while True:
        next = previous + current
        if len(str(next)) == length:
            return index
        previous, current = current, next
        index += 1



print(find_fibonacci_index_by_length(2))

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