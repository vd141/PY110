def minilang(full_command):
    '''
    
    '''

    register = 0

    stack = []

    commands = full_command.split()

    for command in commands:
        match command:
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = register + stack.pop()
            case 'SUB':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = register - stack.pop()
            case 'MULT':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = register * stack.pop()
            case 'DIV':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = register // stack.pop()
            case 'REMAINDER':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = register % stack.pop()
            case 'POP':
                if stack_empty(stack):
                    return('Stack is empty.')
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                try:
                    register = int(command)
                except:
                    print(f'invalid command: {command}')
                    return

def stack_empty(stack):
    return not stack
            
minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

minilang('adsf')

print(minilang('POP'))