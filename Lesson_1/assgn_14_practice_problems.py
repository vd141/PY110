'''
How would you count the number of occurrences of 'banana' in the tuple?
'''
fruits = ("apple", "banana", "cherry", "date", "banana")
fruits.count('banana')

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))

# length is 5 because elements of sets are unique


'''
Given two sets, how would you obtain a set that contains all the unique values from
both sets?
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
a.union(b)

'''
What would the following code's output be?
'''
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)
'''
dictionary with names as keys and their indexes as values. their order is preserved
because dicts order their elements by insertion order
'''

'''
calculate the total age. Separately, find the minimum age
'''
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total = 0
for person in ages:
    total += ages[person]
print(total)

# faster way: 
total_age = sum(ages.values())


'''
What would the following code output? Try to answer without running the code
'''
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)
'''
['bear']
'''

'''
Create a dictionary that represents the frequency of occurrence of each letter. the
frequency count should be case-sensitive
'''
statement = "The Flintstones Rock"

occurrences = {}
for letter in statement:
    if letter not in occurrences:
        occurrences[letter] = 1
    else:
        occurrences[letter] += 1

print(occurrences)

# an alternative solution
char_freq = {}
statement = statement.replace(' ', '')
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)