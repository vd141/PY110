def staggered_case(string):
    '''
    takes a string as an argument and returns that string with a staggered
    capitalization scheme. every other character, starting from the first,
    should be capitalized and sohuld be followed by a lowercase or non alphabetic
    character. non alphabetic characters should not be changed, but should be
    counted as characters for determining when to switch between upper and lower
    case
    '''

    capitalize = True
    new_str = ''

    for char in string:
        if capitalize:
            new_str += char.upper()
            capitalize = False
        else:
            new_str += char.lower()
            capitalize = True

    return new_str

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True