def word_to_digit(message):
    '''
    takes a string as an argument and returns that string with every occurrence of a "number word"
    converted to its corresponding digit character

    the string does not contain any punctuation

    initialize a list of number words corresponding to their index
    create a list of words from the message (str.split())
    loop through list
    if the word is in the list of number words, get the index of the number word
    store each word in a new list and join the list after the loop
    '''

    number_words = ['zero',
                    'one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight',
                    'nine',
                    ]
    
    new_words = []
    
    for word in message.split():
        if word in number_words:
            new_words.append(str(number_words.index(word)))
            continue
        new_words.append(word)

    return ' '.join(new_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True