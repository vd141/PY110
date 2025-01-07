def sum_(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_(numbers, 2) == 20)

'''
python thinks there is a recursive call to the function happening on the return
line. sum() is a built in python function, so i would rename the sum function to
something else
'''