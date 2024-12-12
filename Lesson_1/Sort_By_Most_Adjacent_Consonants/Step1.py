'''
1. Understanding the Problem

Inputs: list of strings
Outputs: sorted list based on the highest number of adjacent consonants a string contains
         (descending?)

Explicit requirements:
    - if two strings contain the same highest number of adjacent consonants, they
      should retain their original order in relation to each other
    - consonants are considered adjacent if they are next to each other in the same word
      or if there is a space between two consonants in adjacent words

Implicit requirements:
    - function must be able to parse strings containing multiple words separated
      by spaces (only spaces, or all whitespaces?)

Questions:
    - should the sorted list be in ascending order or descending order?
    - are two consonants considered adjacent if they are separated by a whitespace
      that is not a space? (\n, for example)
    - should we assume the input list has at least one element?
    - should we assume the input list has only strings?
    - will the strings have non alphabetic non-whitespace characters such as commas and numbers?
        - if so, how should these be treated?
'''