def sum_digits(num):
    '''
    write a function that takes one arugment, a positive int, and returns
    the sum of its digits

    convert to string

    convert string to list

    lsit comprehension of strings converted to ints

    sum list
    '''

    num_str = str(num)

    lst_str = list(num_str)

    nums = [int(number) for number in lst_str]

    return sum(nums)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True