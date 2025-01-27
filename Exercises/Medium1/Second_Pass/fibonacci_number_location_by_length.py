import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    '''
    finds the first fibonacci index that has a number of length length

    calculate a fibonacci number

    convert number to string

    compare string length to length input

    if equal, return the number

    if not, calculate the next fibonacci number and perform the above steps again
    '''

    n_2 = 1
    n_1 = 1
    index = 3

    if length == 1:
        return length

    while True:
        current = n_1 + n_2

        if len(str(current)) == length:
            return index
        n_2, n_1, index = n_1, current, index + 1

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