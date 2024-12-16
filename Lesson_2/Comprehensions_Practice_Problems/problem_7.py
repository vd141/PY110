'''
return a list of the same structure, but only containing the numbers that are
multiples of 3
'''
expected_result = [[], [3, 12], [9], [15, 18]]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [[element for element in sublist if (element % 3 == 0)] for sublist in lst]

print(new_lst == expected_result)