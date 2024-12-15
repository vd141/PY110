'''
modify the word_sizes function to exclude non-letters when determining word size
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
        alpha_only = ''.join(char for char in word if char.isalnum())
        word_length_count[len(alpha_only)] = word_length_count.get(len(alpha_only), 0) + 1

    return word_length_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})