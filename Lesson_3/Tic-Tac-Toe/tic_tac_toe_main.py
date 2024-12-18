'''
Tic-tac-toe
'''
import os
import random
import time

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


WINNING_POSITION_COMBOS = [
    {'1', '2', '3',},
    {'1', '5', '9',},
    {'1', '4', '7',},
    {'2', '5', '8',},
    {'3', '6', '9',},
    {'3', '5', '7',},
    {'4', '5', '6',},
    {'7', '8', '9',},
]


POSITION_ROWS = {
    'ROW_1': 2,
    'ROW_2': 4,
    'ROW_3': 6,
}


def display_welcome():
    '''
    Displays welcome message.

    Inputs:
        - none

    Outputs:
        - message to console, return value is None
    '''

    print('==> Welcome to Tic-Tac-Toe. This is the starting board:')


def display_board(player_positions = {}, computer_positions = {}):
    '''
    prints board based on user positions and computer positions

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)

    Outputs:
        - prints board to console, returns None
    '''

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


def valid_positions(user_input, player_positions, computer_positions):
    '''
    returns False if the user input is not an integer from 1-9 (inclusive) or
    if the user input is one of the occupied positions

    Inputs:
        - user input, player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)

    Outputs:
        - boolean
    '''

    occupied_positions = player_positions.union(computer_positions)

    if user_input not in ALL_VALID_POSITIONS:
        print('==> Value must be an integer from 1-9 inclusive.')
        return False
    if user_input in occupied_positions:
        print('==> Value must be one of the available positions.')
        return False
    
    return True


def get_user_input(player_positions, computer_positions):
    '''
    obtains and validates user input

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)
    Outputs:
        - user input
    '''

    occupied_positions = player_positions.union(computer_positions)

    while True:
        user_input = input('==> Enter an available position:'
                           f'{sorted(ALL_VALID_POSITIONS - occupied_positions)} \n')
        if valid_positions(user_input, player_positions, computer_positions):
            return user_input


def get_computer_input(player_positions, computer_positions):
    '''
    computer randomly selects an available position

    Inputs: player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)

    Outputs: computer-selected position
    '''

    print('==> Computer is choosing...')
    time.sleep(5)
    occupied_positions = player_positions.union(computer_positions)
    return random.choice(list(ALL_VALID_POSITIONS - occupied_positions))


def is_winner(positions):
    '''
    given a set of positions (computer or player), returns True if the input
    occupies a winning position

    Inputs: 
        - set of occupied positions
    Outputs:
        - boolean
    '''

    for combo in WINNING_POSITION_COMBOS:
        if positions.intersection(combo) in WINNING_POSITION_COMBOS:
            return True
    return False


def is_board_full(player_positions, computer_positions):
    '''
    returns True if player and computer occupy all positions on the board, False
    otherwise

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)
    Outputs:
        - boolean
    '''
    occupied_positions = player_positions.union(computer_positions)

    return (occupied_positions.intersection(ALL_VALID_POSITIONS) == 
        ALL_VALID_POSITIONS)


def is_play_again():
    '''
    queries user to play again. validates user input

    Input:
        - none
    Output:
        - boolean
    '''

    while True:
        player_input = input('==> Would you like to play again? y/n\n')
        if player_input in ['y', 'yes', 'n', 'no']:
            if player_input in ['y', 'yes']:
                return True
            if player_input in ['n', 'no']:
                return False
        print('==> Please enter y or n.')


def create_fresh_game_board():
    '''
    clears the console, resets computer and user positions, and prints welcome
    message and board

    Inputs:
        - none
    Outputs:
        - tuple of empty player and computer positions
    '''

    os.system('clear')
    player_positions = set()
    computer_positions = set()
    display_welcome()
    display_board(player_positions, computer_positions)
    return (player_positions, computer_positions)


def main():
    (player_positions, computer_positions) = create_fresh_game_board()

    while True:
        player_input = get_user_input(player_positions, computer_positions)
        player_positions.add(player_input)
        os.system('clear')

        print(f'==> You chose {player_input}')
        display_board(player_positions, computer_positions)
        if is_winner(player_positions):
            print('==> Player won!')
            if not is_play_again():
                print('==> Thank you for playing.')
                break
            else:
                (player_positions, computer_positions) = create_fresh_game_board()
                continue

        if is_board_full(player_positions, computer_positions):
            print('==> It\'s a tie!')
            if not is_play_again():
                print('==> Thank you for playing.')
                break
            else:
                (player_positions, computer_positions) = create_fresh_game_board()
                continue

        computer_input = get_computer_input(player_positions, computer_positions)
        computer_positions.add(computer_input)
        os.system('clear')

        print(f'==> Computer chose {computer_input}')
        display_board(player_positions, computer_positions)
        if is_winner(computer_positions):
            print('==> Computer won!')
            if not is_play_again():
                print('==> Thank you for playing.')
                break
            else:
                (player_positions, computer_positions) = create_fresh_game_board()
                continue

        if is_board_full(player_positions, computer_positions):
            print('==> It\'s a tie!')
            if not is_play_again():
                print('==> Thank you for playing.')
                break
            else:
                (player_positions, computer_positions) = create_fresh_game_board()
                continue
            

main()