'''
write some code to create a list of every vowel (a, e, i, o, u) that appears in
the contained strings, then print it
'''

VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def list_of_vowels2():
    list_of_vowels = []
    
    for list in dict1.values():
        for words in list:
            for char in words:
                if char in VOWELS:
                    list_of_vowels.append(char)

    return list_of_vowels

def list_of_vowels():
    return [char for list in dict1.values()
                   for words in list
                   for char in words if char in VOWELS]

print(list_of_vowels())
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']