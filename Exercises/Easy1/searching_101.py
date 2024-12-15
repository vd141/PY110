'''
Program that solicits six numbers from the user and prints a message that describes
wheether the sixth number appears among the first five

inputs: 6 inputs from user
outputs: message that describes whether the sixth number appears among the first five

data structure: list to store five user inputs
algorithm: prompt the user 6 times, storing the first 5 inputs in a list.
           use a for loop to prompt the user
'''

def ask_for_five():
    '''
    ask for five inputs. ask for first 5 in a for loop. return a list of inputs
    '''
    five_inputs = []

    for number in range(1,6):
        user_input = get_first_five_input(number)
        five_inputs.append(user_input)

    return five_inputs

def ask_for_sixth():
    '''
    ask for the sixth input. 
    '''
    pass

def suffix(number):
    '''
    Returns the correct suffix based on an input number:
    st, nd, rd, th
    '''
    match number:
        case 0:
            return 'th'
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _ if number >= 4:
            return 'th'

def valid_numerical_input(user_input):
    '''
    reprompt user to enter input again if the input cannot be coerced to a float
    or an int
    '''
    try:
        user_input = int(user_input)
        return True
    except ValueError:
        print('Input must be an integer.')
        return False

def get_first_five_input(number):
    '''
    prompts user for input using input string
    '''
    while True:
        user_input = input(f'Enter the {number}{suffix(number)} number: ')
        if valid_numerical_input(user_input):
            return float(user_input)

'''print(ask_for_five())'''

'''
simple version
'''
numbers = []

numbers.append(input('Enter the 1st number: '))
numbers.append(input('Enter the 2nd number: '))
numbers.append(input('Enter the 3rd number: '))
numbers.append(input('Enter the 4th number: '))
numbers.append(input('Enter the 5th number: '))

numbers_list = ', '.join(numbers)

# last_number = input('Enter the last number: ')

# if last_number in numbers:
#     print(f'{last_number} is in {numbers_list}.')
# else:
#     print(f'{last_number} is not in {numbers_list}.')
