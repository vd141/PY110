def minilang(string):
    '''
    
    '''

    register = 0
    stack = []

    commands = string.split()
    
    for command in commands:
        try:
            match command:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register = stack.pop() + register
                case 'SUB':
                    register = register - stack.pop()
                case 'MULT':
                    register = register * stack.pop()
                case 'DIV':
                    register = int(register / stack.pop())
                case 'REMAINDER':
                    register = int(register % stack.pop())
                case 'POP':
                    register = stack.pop()
                case 'PRINT':
                    print(register)
                case _:
                    register = int(command)
        except ValueError as e:
            return e
        except IndexError as e:
            return e
        except ZeroDivisionError as e:
            return e


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

print(minilang('POP'))