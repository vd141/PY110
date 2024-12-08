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