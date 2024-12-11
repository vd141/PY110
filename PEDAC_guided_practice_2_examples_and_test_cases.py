'''
2. examples and test cases:

test cases are provided below

Do the test cases confirm or refute different elements of your original analysis
and mental model? do they answer any of the questions that you had, or do they
perhaps raise further questions?

let's test the assumptions by going through the test cases

add base case for when there is 0 or 1 block

the rest of the test cases seem to work

'''

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True