def bubble_sort(lst1):
    '''
    sorts (and mutates) and input list
    input list contains at least two elements

    input: list of at least two elements
    output: sorted list

    requirements:
        - types of elements in list: integers, strings
    
    data structures:
        - the list we are sorting

    algorithm:
        - loop through the list and compare two elements at a time
        - swap the elements if they are out of place
        - repeat above steps until no elements have been swapped
            - we don't know how many times we will have to repeat the above steps (while loop)
        - keep track of whether elements have been swapped

    '''

    while True:
        swapped = False
        for ind1 in range(0, len(lst1) - 1):
            ind2 = ind1 + 1
            if lst1[ind1] > lst1[ind2]:
                lst1[ind2], lst1[ind1] = lst1[ind1], lst1[ind2]
                swapped = True
        if swapped == False:
            return lst1
            
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True