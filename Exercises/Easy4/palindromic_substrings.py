from all_substrings import substrings

def palindromes(string):
    '''
    returns all palindromic substrings of a string

    grab all substrings, only check if substring length >= 2 is a palindrome

    '''
    all_substrings = substrings(string)
    all_substrings = [substring for substring in all_substrings if
                      len(substring) >= 2]
    
    return [substring for substring in all_substrings if substring ==
            substring[::-1]]



print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

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