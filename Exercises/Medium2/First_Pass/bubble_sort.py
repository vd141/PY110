def bubble_sort(lst1):
    '''
    the function should mutate the list

    inputs: a list
    outputs: a sorted list

    loop through the list, from the first element to the second-to-last element
    if the current element is larger than the next element, swap the elements
    a swap has been made
    increment the index and repeat the swap

    the sort reruns if a swap was made in the previous run. if no swap was made
    the list has been sorted
    '''

    swapped = True

    while swapped == True:
        swapped = False
        for idx in range(len(lst1) - 1):
            current, next = lst1[idx], lst1[idx + 1]
            if current > next:
                lst1[idx], lst1[idx + 1] = next, current
                swapped = True
            
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