'''
Difference of Two
The objective is to return all pairs of numbers from a given array of numbers that have a difference of 2.
The result array should be sorted in ascending order of values.
Assume there are no duplicate numbers in the array.
The order of the numbers in the input array should not matter.

Inputs: list of numbers
Outputs: list of lists. each inner list contains a pair of numbers from the input
that have a difference of two

Requirements:
    - result array sorted in ascending order
    - assume no duplicate numbers in array
    - order of numbers from the input array should not matter
    - elements in input can be used in multiple sublists
    - each sublist only contains a pair of numbers, no more

Examples:
    - see below

Data structures:
    - child list (create a new one for every pair)
    - parent list

Algorithm:
    - sort the list to ensure that each child list we create is already sorted
    - loop through the list to check each element
    - if the element's +2 exists in the list, we have a pair
        - add the pair to a empty child list
        - add the child list to the parent list
    - if it doesn't exist, continue onto the next element without adding anything
    to a list
    - return the parent list
    
**Victor**
Algorithm (create all possible pairs from list first):
  - sort list first
  - use a nested for loop to create all possible pairs
  - append all possible pairs to a full list
  - loop through each element (sublist) of the full list
    - check if there is a difference of 2 between the first and second value of that element
  - if there is, add that element to a final set (set removes duplicates)
  - convert final set to list and return that list
'''



# Python Test cases
print(differenceOfTwo([1, 2, 3, 4]) == [[1, 3], [2, 4]])
print(differenceOfTwo([4, 1, 2, 3]) == [[1, 3], [2, 4]])
print(differenceOfTwo([1, 23, 3, 4, 7]) == [[1, 3]])
print(differenceOfTwo([4, 3, 1, 5, 6]) == [[1, 3], [3, 5], [4, 6]])
print(differenceOfTwo([2, 4]) == [[2, 4]])
print(differenceOfTwo([1, 4, 7, 10, 13]) == [])

