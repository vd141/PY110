'''
swap the first and last characters of every word in the sentence

- every word contains at least one letter
- the string will always contain at least one word
- assume that each string contains nothing but words and spaces and that there are
  no leading, trailing, or repeated spaces
'''

def swap(string):
    '''
    split sentence into list of words using string split method

    for each word, create new string and add it to the new list of words

    use string join method to join new list of words
    '''
    words = string.split()
    swapped_words = []
    for word in words:
        if len(word) > 1:
            swapped_word = word[-1] + word[1:len(word) - 1] + word[0]
            swapped_words.append(swapped_word)
        else:
            swapped_words.append(word)

    return ' '.join(swapped_words)



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True