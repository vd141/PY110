from convert_number_to_string import integer_to_string

def signed_integer_to_string(integer):
    if integer > 0:
        return '+' + integer_to_string(integer)
    elif integer < 0:
        return '-' + integer_to_string(integer / -1)
    else:
        return '0'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

print(integer_to_string(-11))