'''
add a sign to the beginning of the string
'''

from convert_a_number_to_a_string import integer_to_string

def signed_integer_to_string(integer):
    if integer > 0:
        return '+' + integer_to_string(integer)
    if integer < 0:
        return '-' + integer_to_string(-1 * integer)
    return integer_to_string(integer)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True