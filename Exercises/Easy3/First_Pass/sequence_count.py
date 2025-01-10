def sequence(int1, int2):
    '''
    the first argument is a count, and the second is the starting number of a
    sequence that your function will create. the function should return a list
    containing the same number of elements as the count argument. the value of
    each element should be a multiple of the starting number


    '''

    new_list = []
    running_sum = int2

    for _ in range(int1):
        new_list.append(running_sum)
        running_sum += int2
    
    return new_list

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True