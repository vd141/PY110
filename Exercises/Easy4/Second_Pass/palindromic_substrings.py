from all_substrings import substrings

def palindromes(full_string):
    '''
    returns a list of all palindromic substrings of a string. each substring must consist of
    a sequence of characters that reads the same forward and backward. substrings in the
    returned list should be sorted by their order of appearance in the input string.
    duplicate substrings should be included multiple times.

    get all substrings using substrings()

    then loop through substring list and select only substrings whose reversed values are equivalent to
    the original


    '''

    all_substrings = substrings(full_string)

    return [substring for substring in all_substrings if (substring == substring[::-1] and len(substring) >= 2)]


print(palindromes('abcd') == [])                  # True
print(palindromes('madam'))
print(palindromes('madam') == ['madam', 'ada'])   # True
print(palindromes('hello-madam-did-madam-goodbye'))
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True