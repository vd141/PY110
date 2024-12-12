'''
5. Code

'''

def sort_by_consonant_count(strings):
    strings.sort(key=number_of_adjacent_consonants, reverse=True)
    return strings

def number_of_adjacent_consonants(string):
    '''
    Determine the number of adjacent consonants in a string.
    '''
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')
    VOWELS = set('aeiou')
    CONSONANTS = ALPHABET.difference(VOWELS)

    consonant_count = 0
    max_consonant_count = 0

    for character in string:
        if character in CONSONANTS:
            consonant_count += 1
            if consonant_count >= max_consonant_count:
                max_consonant_count = consonant_count
        elif character.isalpha():
            consonant_count = 0

    return max_consonant_count if max_consonant_count >= 2 else 0

# print(number_of_adjacent_consonants('abe') == 0) # True
# print(number_of_adjacent_consonants('aberdeen') == 2) # True
# print(number_of_adjacent_consonants('mylo zyloto') == 3) # True
# print(number_of_adjacent_consonants('bring the rock') == 4) # True
# print(number_of_adjacent_consonants('') == 0) # True

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']