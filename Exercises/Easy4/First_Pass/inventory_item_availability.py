from inventory_then_transactions import transactions_for

def is_item_available(id, transactions):
    '''
    returns True or False based on whether or not an inventory item
    is available

    gets relevant transactions using transactions_id

    then calculates the sum of the quantity

    return sum >= 0
    '''

    id_transactions = transactions_for(id, transactions)

    running_sum = 0

    for transact in id_transactions:
        if transact['movement'] == 'in':
            running_sum += transact['quantity']
        else:
            running_sum -= transact['quantity']

    return running_sum > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True