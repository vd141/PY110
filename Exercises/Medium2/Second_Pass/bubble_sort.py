def bubble_sort(lst1):
    '''
    input: unsorted list
    output: sorted list (mutates input)

    requirements:
        - list contains at least two elements

    data structures:
        - mutate list in place

    algorithm:
        - keep track of two consecutive indexes
        - keep track of a sorted boolean. initial value is False
        - iterate through the list to compare the values of each index
        - if the pair of values is unsorted, sort the pair
            - set the sorted boolean to True
        - increment both indexes until the first index is 2 less than the length of the list
        - once all the values have been compared in a pass, check to see if the sorted boolean
          is false. if it is, the list is sorted and can be returned. if it isn't, reset the indexes
          and run another pass of the sorting algorithm
    '''

    while True:
        idx_1 = 0
        idx_2 = 1
        sorted = False

        for _ in range(len(lst1) - 1):
            if lst1[idx_1] > lst1[idx_2]:
                lst1[idx_1], lst1[idx_2] = lst1[idx_2], lst1[idx_1]
                sorted = True
            idx_1 += 1
            idx_2 += 1
        
        if sorted is False:
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