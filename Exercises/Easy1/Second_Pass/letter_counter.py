def word_sizes(string):
    '''
    write a function that takes a string of zero or more space-separated words
    and returns a dictionary that shows the number of words of different sizes

    sizes: count

    update to exclude non-letters (''.isalpha())
    '''

    counts = {}

    words = string.split()

    # use the dictionary get method to update the dictionary

    for word in words:
        stripped_word = ''
        for char in word:
            if char.isalpha():
                stripped_word += char
        counts[len(stripped_word)] = counts.get(len(stripped_word), 0) + 1

    return counts

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