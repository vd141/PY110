from convert_string_to_number import string_to_integer

def string_to_signed_integer(number_string):
    if number_string[0] not in ['-', '+']:
        return string_to_integer(number_string)
    else:
        match number_string[0]:
            case '+':
                return string_to_integer(number_string[1:])
            case '-':
                return -1 * string_to_integer(number_string[1:])
            
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True