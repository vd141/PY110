'''
Select key-value pairs where value is 'Fruit'
'''
produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce):
    fruits = {}
    for good in produce:
        if produce[good] == 'Fruit':
            fruits.update({good: produce[good]})
    return fruits

select_fruit(produce)
print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

def double_numbers(numbers):
    for index, _ in enumerate(numbers):
        numbers[index] *= 2
    return numbers

'''
suppose we wanted to transform the numbers based on their position in the list rather
than their value? Try coding a solution that doubles the numbers that have odd indexes
'''

def double_odd_indexes(numbers):
    '''
    input: list of numbers
    output: list of numbers whose odd indexes are doubled versions of the input list
    '''

    doubled_odd_indexes = []

    for index, value in enumerate(numbers):
        if index % 2 == 1:
            doubled = numbers[index] * 2
            doubled_odd_indexes.append(doubled)
        else:
            same_value = numbers[index]
            doubled_odd_indexes.append(same_value)
    
    return doubled_odd_indexes

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_indexes(my_numbers)) # 1, 8, 3, 14, 2, 12


def multiply(numbers, factor):
    multiplied = []

    for number in numbers:
        multiplied.append(number * factor)

    return multiplied


my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]