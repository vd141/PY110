def swap_name(string):
    '''
    takes a string argument consisting of a first name, space, and last name. the
    function should return a new string consisting of the last name, a comma, and
    the first name
    '''

    splits = string.split()

    return f'{splits[1]}, {splits[0]}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True