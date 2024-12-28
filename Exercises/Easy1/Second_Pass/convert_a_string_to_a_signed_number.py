import convert_a_string_to_a_number as s

def string_to_signed_integer(string):
    if string[0] in ['+', '-']:
        unsigned_string = string[1:]
        if string[0] == '+':
            return s.string_to_integer(unsigned_string)
        return -s.string_to_integer(unsigned_string)
    return s.string_to_integer(string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True