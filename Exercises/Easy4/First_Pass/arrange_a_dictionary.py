def order_by_value(dict1):
    '''
    given a dict, return its keys sorted by the values associated with each key
    '''

    def sort_by_value(key):
        return dict1[key]
    
    return sorted(dict1, key=sort_by_value)


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True