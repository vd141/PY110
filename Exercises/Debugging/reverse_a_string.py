def reverse_string(string):
    # for char in string:
    #     string = char + string

    # return string
    return string[::-1]

print(reverse_string('hello'))
print(reverse_string("hello") == "olleh")
'''
as the for loop iterates, each subsequent character is being added to the
beginning of the string. the for loop only iterates for the length of the
original string object, so the for loop adds all of the characters in reverse
order to the original string before ending. the original string value is still
contained in the variable.

the easiest way to rewrite this function would be to use string indexing

return string[::-1]
'''