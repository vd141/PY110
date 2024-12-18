'''
Tic-tac-toe
'''
import random

ALL_VALID_POSITIONS = {'1', 
                '2', 
                '3', 
                '4', 
                '5', 
                '6', 
                '7', 
                '8', 
                '9',
                }

WINNER

POSITION_ROWS = {
    'ROW_1': 2,
    'ROW_2': 4,
    'ROW_3': 6,
}

def display_welcome():
    print('==> Welcome to Tic-Tac-Toe. This is the starting board:')

def display_board(player_positions = {}, computer_positions = {}):

    board = [
        '==> You: O, Computer: X',
        '==>  - - - ',
        '==> |1|2|3|',
        '==>  - - - ',
        '==> |4|5|6|',
        '==>  - - - ',
        '==> |7|8|9|',
        '==>  - - -',
    ]

    for row_index in POSITION_ROWS.values():
        for position in player_positions:
            if position in board[row_index]:
                board[row_index] = board[row_index].replace(position, 'O')
        for position in computer_positions:
            if position in board[row_index]:
                board[row_index] = board[row_index].replace(position, 'X')

    for row in board:
        print(row)

def valid_input(user_input, player_positions, computer_positions):
    occupied_positions = player_positions.union(computer_positions)

    if user_input not in ALL_VALID_POSITIONS:
        print('==> Value must be an integer from 1-9 inclusive.')
        return False
    if user_input in occupied_positions:
        print('==> Value must be one of the available positions.')
        return False
    
    return True

def get_user_input(player_positions, computer_positions):
    occupied_positions = player_positions.union(computer_positions)

    while True:
        user_input = input('==> Enter an available position:'
                           f'{sorted(ALL_VALID_POSITIONS - occupied_positions)} \n')
        if valid_input(user_input, player_positions, computer_positions):
            return user_input
        
def get_computer_input(player_positions, computer_positions):
    occupied_positions = player_positions.union(computer_positions)
    return random.choice(list(ALL_VALID_POSITIONS - occupied_positions))


def main():
    player_positions = set()
    computer_positions = set()
    display_welcome()
    display_board(player_positions, computer_positions)

    while True:
        player_positions.add(get_user_input(player_positions,
                                            computer_positions))
        computer_positions.add(get_computer_input(player_positions,
                                              computer_positions))
        display_board(player_positions, computer_positions)




main()