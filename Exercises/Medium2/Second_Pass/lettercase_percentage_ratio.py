DECIMAL_FACTOR = 100

def letter_percentages(input_string):
    '''
    takes a string and returns a dictionary containing the 3 properties:
        - percentage of characters in the sting that are lowercase
        - percentage of characters that are uppercase
        - percentage of characters that are neither

    numeric percentages are values that lie between 0.00 and 100.00

    input is a string
    output is a dict with key/value pairs corresponding to the percentage of 
    lowercase, uppercase, and neither
    
    data structures:
        - input is a string
        - output is a dict

    loop through the string
        - if character is lowercase, increase lowercase count by 1
        - if character is uppercase, increase uppercase count by 1
        - else, increase neither count by 1

    divide each count by the length of the string to get the decimal value. 

    convert each decimal value to our intended range by multiplying by 100

    use an f-string as the value to save to each
    '''

    stats = {}
    lowercase = 0
    uppercase = 0
    neither = 0

    for char in input_string:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        else:
            neither += 1

    lower_decimal = (lowercase / len(input_string)) * DECIMAL_FACTOR
    upper_decimal = (uppercase / len(input_string)) * DECIMAL_FACTOR
    neither_decimal = (neither / len(input_string)) * DECIMAL_FACTOR

    stats['lowercase'] = f'{lower_decimal:.2f}'
    stats['uppercase'] = f'{upper_decimal:.2f}'
    stats['neither'] = f'{neither_decimal:.2f}'

    return stats

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)