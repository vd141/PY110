from merge_sorted_lists import merge
from pprint import pp

def merge_sort(lst):
    '''
    split lst into sublists until every sublist contains only one value

    this function will not mutate the original list

    how deep into the lst do we go?
    '''

    sorted_lst = lst[:]

    divided = divide(sorted_lst)

    merge_me = divided[0]

    while len(merge_me) == 2:
        merge_me = merge_me[0]
        if merge(merge_me)


def divide(lst):
    '''
    split lst into sublists until every sublist contains only one value

    get midpoint of current list (len(lst) // 2)

    new list is [lst[:midpoint] lst[midpoint:]]

    perform divide on each sublist if the length of the sublist is greater than 1
 
    '''

    midpoint = len(lst) // 2

    new_list = [lst[:midpoint], lst[midpoint:]]

    if len(new_list[0]) > 1:
        new_list[0] = divide(new_list[0])
    if len(new_list[1]) > 1:
        new_list[1] = divide(new_list[1])

    return new_list

lst = [9, 2, 7, 6, 8, 5, 0, 1]             # initial list
print(divide(lst) == [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]])

