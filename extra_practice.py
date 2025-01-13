'''
Create a string from the list's elements

The join method only accepts collections of strings, so we can coerce each element
in the list into a string
'''
numbers = [1, 2, 3, 4]
# goal: string_version = '1234'

string_version = ''.join([str(number) for number in numbers])

'''
What is a set?

an unordered collection of data. it can't be indexed, but membership can be checked.
sets are mutable, but the individual members must be immutable
'''

'''
Is it best practice to use a float as a dictionary key?

It does not because of floating point precision issues.
'''

'''
What is a hashable object?

A hash can be created from a hashable objects. Hashable objects include immutable
data types that do not have mutable elements:
- ranges
- strings
- floats (not best practice to use these)
- ints
- frozen sets
- tuples (if tuples don't have mutable elements)

Non-hashable objects:
- dicts (keys are hashed)
- lists
- sets (elements are hashed but the set itself is mutable)
'''

'''
set methods

-add -> adds the argument to the set
-update -> accepts a collectible. adds each element of collectible to the set
-remove -> removes object, raises KeyError if object does not exist
-discard -> removes object, does not throw exception if object does not exist
'''

'''
difference between frozenset and set?

frozenset is an immutable set
'''

'''
2 ways to create dicts from other collectibles?
>>> dict from a collection of pairs
>>> dict([('a', 1), ('b', 2), ('c', 3)])

>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> zipped_pairs = zip(keys, values)
>>> dict(zipped_pairs)
{'a': 1, 'b': 2, 'c': 3}
'''

'''
String methods

what is the differnce between str.index() and str.find()?
- str.index returns the starting index of the argument. it throws an exception if
the argument isn't found
- str.find returns the starting index of th argument. it returns -1 if the argument 
isn't found


What does the third argument of str.replace() do?
it specifies the number of times the function will replace the first argument
with the second argument in the parent string

What does this code do?
>>> 'Straße'.swapcase().swapcase()

What does the str.split()'s second parameter do?
specifies the number of splits to perform

How can you split each character in the string 'abacus'?
list('abacus')

What does str(None) return?
'None'

what does the str() function do to its argument when the argument is a collectible?
it returns a string that denotes the collectible's literal representation

What does this code do?
>>> str(frozenset([1, 2, 3]))

it coerces its argument to a string representing a frozenset 'literal'. 
it also changes frozenset's argument from a list literal into a set literal
'''

'''
what does a dict's setdefault method do?

it takes two arguments, a key and a value. if the key already exists in the dictionary,
then the method returns its existing value. if the key does not exist, it creates
a key value pair and returns the value
'''

'''
how would we create a dictionary the records the number of occurences of each letter
of a string?
'''
a_string = 'the quick brown fox jumps over the lazy dog'
occurences = {}
for letter in a_string:
    occurences.setdefault(letter, 0)
    occurences[letter] += 1

print(occurences)

'''
what is the difference between the pop and popitem dictionary methods?

the pop method takes a key as an argument, deletes the key value pair from the dict, 
and returns the value. it raises an exception if the key does not exist. the second 
argument can be used as the return value if the key does not exist

the popitem method takes no arguments and returns a keyerror if the dict is empty. 
it returns the last key-value pair in the dict as a tuple
'''

'''
what is the difference between the | and |= operators when used with dicts?
| returns a new dict that is a "concatenation" of its operands
|= concatenates the two dicts by mutating its left operand

if a key-value pair is shared between the two dicts, the value in the left operand
is overwritten with the value in the right operand
'''

'''
set comparisons
issubset, issuperset, <=, >=, <, >
'''

'''
set operations
union, |, intersection, &, difference, and -

does the union method mutate the set?
it does not
'''

'''
set methods:
 add, remove, discard, pop, clear
 add adds an element to the set and does not do anything if the element is already in
 remove removes an element from the set and throws an error if the argument is not in the set
 discard removes an element from the set and does not throw an error if the argument is not in
 pop removes an arbitrary element from the set. raises a keyerror if the set is empty
 clear empties the set of elements


disjoint method

returns boolean based on whether the sets share no elements (True) or not do (False)
In other words, returns True if the intersection is empty
'''

'''
what happens if a dictionary is converted into a set?

only the dictionary's keys are stored in the set
'''

'''
unpacking collectibles and dicts
* unary operator unpacks most collectibles except dicts and strings
** unary operator unpacks dicts
'''

'''
other uses of the ** unary operator: keyword arguments

keyword arguments are function arguments that contain a variable name assigned to a value

def a_function(**kwargs)

inside the function, kwargs becomes a dictionary containing all the variable/value pairs
as key/value pairs
'''

'''
list sort method
'''

'''
Given two sets, how would you obtain a set that contains all the unique values from
both sets?
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
a.union(b)

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

'''
Create a dictionary that represents the frequency of occurrence of each letter. the
frequency count should be case-sensitive
'''
statement = "The Flintstones Rock"

'''
What does the following code print and why?
'''
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

'''
return a new list identical in structure to the original but with each number incremented
by 1. do not modify the original data structure. use a comprehension
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_dict = [dict(zip(subdict.keys(), [sub_values + 1 for sub_values in subdict.values()])) for subdict in lst]
print(new_dict)
print(new_dict == [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}])

'''
all_substrings.py problem from Easy4
palindromic_substrings.py problem from Easy4
'''