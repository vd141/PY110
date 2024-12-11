'''
implement a solution in code using all the previous building blocks
'''

def calculate_leftover_blocks(given_blocks):
    
    cumulative_sum = 0
    layer = 0

    while True:
        layer_sum = layer**2
        if (layer_sum + cumulative_sum) >= given_blocks:
            if (layer_sum + cumulative_sum) == given_blocks:
                return 0
            else:
                return (given_blocks - cumulative_sum)
        cumulative_sum += layer_sum
        layer += 1

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True