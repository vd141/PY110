def get_key_value(my_dict, key):
    # if my_dict[key]:
    #     return my_dict[key]
    # else:
    #     return None
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

'''
the code is currently checking the truthiness of my_dict[key]. this isn't quite
the same as checking to see if the key is in the dict. to do that, we can replace
if my_dict[key] with
if key in my_dict
'''

