'''
given dict1, write code to produce a list that looks like return_value

colors of fruits and sizes of vegetables should be returned

sizes should be uppercase and colors should be capitalized
'''
expected_value = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_lst = []

for info in dict1.values():
    if info['type'] == 'fruit':
        colors_list = [color.capitalize() for color in info['colors']]
        new_lst.append(colors_list)
    if info['type'] == 'vegetable':
        new_lst.append(info['size'].upper())

print(new_lst == expected_value)