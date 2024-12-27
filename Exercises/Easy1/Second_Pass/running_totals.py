def running_total(list):
    '''
    function takes a list and returns a list with a running total in place of each
    element

    keep the original list

    create a new list

    loop through the original list and add it to the running total. append the 
    running total to the new list

    running_total is initialized to 0
    '''

    running_total = 0

    new_list = []

    for element in list:
        running_total += element
        new_list.append(running_total)

    return new_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True