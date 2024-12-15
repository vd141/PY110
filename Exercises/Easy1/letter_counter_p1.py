'''
Write a function that takes a string consisting of zero or more space-separated words
and returns a dictionary that shows the number of words of different sizes

words consist of any sequence of non-space characters
'''

def word_sizes(string):
    '''
    get length of each individual word. get each individual word by splitting
    the input string

    for each word, get its length. if the dictionary already has its length, add
    1 to the existing value

    if the diciontary does not have 1 in its length, initialize the key-value pair
    and add 1 to its value
    '''
    words = string.split()
    word_length_count = {}

    for word in words:
        word_length_count[len(word)] = word_length_count.get(len(word), 0) + 1

    return word_length_count
    



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})