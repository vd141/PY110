def staggered_case(string):
    '''
    modify functino from p1 so it ignores non-alphabetic characters
    when determining whether it should uppercase or lowercase each letter
    '''

    capitalize = True
    new_str = ''

    for char in string:
        if char.isalpha():
            if capitalize:
                new_str += char.upper()
                capitalize = False
            else:
                new_str += char.lower()
                capitalize = True
        else:
            new_str += char

    return new_str

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True