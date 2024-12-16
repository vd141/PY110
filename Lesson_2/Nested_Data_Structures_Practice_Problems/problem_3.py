'''
given the following code, what will the final values of a and b be? try to answer
without running the code
'''
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2 # [4, [5, 8]]
lst[1][0] -= a # [4, [3, 8]]
print(lst)