def word_to_digit(message):
    '''
    takes a string as an argument and returns that string with every occurrence
    of a number word

    assume message is separated by only spaces. iterate through each word after
    splitting the message. if the word is a numeric word, replace it with its
    number form. join all split words
    '''

    # split_message = message.split()

    # for idx, word in enumerate(split_message):
    #     match word:
    #         case 'one':
    #             split_message[idx] = '1'
    #         case 'two':
    #             split_message[idx] = '2'
    #         case 'three':
    #             split_message[idx] = '3'
    #         case 'four':
    #             split_message[idx] = '4'
    #         case 'five':
    #             split_message[idx] = '5'
    #         case 'six':
    #             split_message[idx] = '6'
    #         case 'seven':
    #             split_message[idx] = '7'
    #         case 'eight':
    #             split_message[idx] = '8'
    #         case 'nine':
    #             split_message[idx] = '9'

    # return ' '.join(split_message)

    message = message.replace('zero', '0')
    message = message.replace('one', '1')
    message = message.replace('two', '2')
    message = message.replace('three', '3')
    message = message.replace('four', '4')
    message = message.replace('five', '5')
    message = message.replace('six', '6')
    message = message.replace('seven', '7')
    message = message.replace('eight', '8')
    message = message.replace('nine', '9')

    return message

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True