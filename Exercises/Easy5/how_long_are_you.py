def word_lengths(words=''):
    '''
    takes a string as an argument and returns a list that contains every word
    from the string, with each word followed by a space and the word's length.
    if the argument is an empty string or if no argument is passed, the function
    should return an empty list
    '''

    list_of_words = words.split()

    for idx, word in enumerate(list_of_words):
        list_of_words[idx] = word + ' ' + str(len(word))

    return list_of_words

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True