def repeater(string):
    '''
    takes a string, doubles every character as a string, then returns result as
    a new string
    '''

    new_str = ''

    for char in string:
        new_str += char * 2
    
    return new_str

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True