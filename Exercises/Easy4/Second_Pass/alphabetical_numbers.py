def alphabetic_number_sort(input_list):
    '''
    takes a list of integers between 0 and 19 and returns a list of those
    integers sorted based on the english word for each number
    '''

    ints_english = ['zero',
                    'one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight',
                    'nine',
                    'ten',
                    'eleven',
                    'twelve',
                    'thirteen',
                    'fourteen',
                    'fifteen',
                    'sixteen',
                    'seventeen',
                    'eighteen',
                    'nineteen']
    
    def sort_by_english(num):
        '''
        returns the english word based on the input num
        '''

        return ints_english[num]
    
    return sorted(input_list, key=sort_by_english)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True