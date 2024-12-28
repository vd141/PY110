'''
given a string of words separated by spaces, write a function that swaps the first
and last letters of every word


'''

def swap(string):
    words = string.split()

    swapped_sentence = []

    for word in words:
        swapped_sentence.append(swap_letters(word))
    
    return ' '.join(swapped_sentence)

def swap_letters(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]

print(swap('Oh what a wonderful day it is'))  # True
print(swap('Abcde'))            # True
print(swap('a'))                    # True

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True