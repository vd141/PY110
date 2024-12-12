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