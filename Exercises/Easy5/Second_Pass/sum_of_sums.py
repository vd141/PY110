def sum_of_sums(nums):
    '''
    returns the sum of sums of each leading subsequence in that list

    store running sum in running_sum variable (init value is 0)

    use an index to slice the index, returning the numbers we want to sum for each element in the subsequence
    '''

    running_sum = 0

    for idx in range(1, len(nums) + 1):
        running_sum += sum(nums[:idx])
    
    return running_sum



print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True