def sum_square_difference(num):
    '''
    computes the difference between the square of the sum of the first count
    positive integers and the sum of the squares of the first count positive
    integers

    input: count integer
    output: difference integer

    data structures:
        -  none

    algorithm:
        - create a range of the first count positive integers
        - using the range function to get the first count positive integers,
          sum the range, square that value and assign it to as sq_of_sum
        - using a for loop, square each number in the range and add it to the
          sum_of_sq value (initialized at 0)
        - return the sq_of_sum - sum_of_sq
    
    '''

    count_range = range(1, num + 1)

    sq_of_sum = sum(count_range)**2

    sum_of_sq = 0

    for value in count_range:
        sum_of_sq += value**2

    return sq_of_sum - sum_of_sq

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True