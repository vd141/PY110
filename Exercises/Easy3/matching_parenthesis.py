def is_balanced(string, opening_char='('):
    '''
    takes a string as an argument and returns true if all the parentheses in the
    string are fully balanced

    loop through the string. for every open parenthesis, add a one to a
    counter. for every closed parenthesis, subtract a one from the counter

    return True if the final counter value is 0, otherwise return False

    how do 
    '''

    closing_chars = {
        '(': ')',
        '{': '}',
        '[': ']',
        '"': '"',
        '\'': '\'',
    }

    closing_char = closing_chars[opening_char]

    counter = 0

    if closing_char not in ['\'', '"']:
        for char in string:
            if counter == 0 and char == closing_char:
                return False
            if char == opening_char:
                counter += 1
            if char == closing_char:
                counter -= 1
    else:
        add_me = 1
        for char in string:
            if char == opening_char:
                counter += add_me
                add_me *= -1


    return (counter == 0)


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
print(is_balanced("What \"is\" this?", '"') == True)        # True
print(is_balanced("What \"is this?", '"') == False)        # True
print(is_balanced("What \{is\} this?", '{') == True)        # True
print(is_balanced("What \{is this?", '{') == False)        # True