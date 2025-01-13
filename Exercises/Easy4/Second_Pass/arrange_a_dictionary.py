def order_by_value(my_dict):
    '''
    return a dictionary's keys sorted by the values associated with
    each key
    '''

    def sort_by_value(key):
        return my_dict[key]

    return sorted(my_dict.keys(), key=sort_by_value)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True