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
        user_input = validate_input(number)
        five_inputs.append(user_input)
    
    return five_inputs
        

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
        
def validate_input(number):
    '''
    reprompt user to enter input again if the input cannot be coerced to a float
    or an int
    '''
    while True:
        try:
            user_input = int(input(f'Enter the {number}{suffix(number)} number: '))
            user_input = float(input(f'Enter the {number}{suffix(number)} number: '))
            return user_input
        except ValueError:
            print('Input must be a float or an integer number.')


    
ask_for_six()