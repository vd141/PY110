'''
Tic-tac-toe
'''
import os
import random
import time
import copy

PLAYER_MARKER = 'o'
COMPUTER_MARKER = 'x'

COMPUTER_THINK_TIME = 1

WINNING_SCORE = 5

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


WINNING_POSITION_COMBOS = (
    {'1', '2', '3',},
    {'1', '5', '9',},
    {'1', '4', '7',},
    {'2', '5', '8',},
    {'3', '6', '9',},
    {'3', '5', '7',},
    {'4', '5', '6',},
    {'7', '8', '9',},
)


POSITION_ROWS = {
    'ROW_1': 2,
    'ROW_2': 4,
    'ROW_3': 6,
}


PLAYERS = {
    'computer',
    'user',
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


def display_board(player_positions = None, computer_positions = None):
    '''
    prints board based on user positions and computer positions

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)

    Outputs:
        - prints board to console, returns None
    '''

    if player_positions is None:
        player_positions = set()
    if computer_positions is None:
        computer_positions = set()

    board = [
        '==> You: o, Computer: x',
        '==> +---+---+---+',
        '==> | 1 | 2 | 3 |',
        '==> +---+---+---+',
        '==> | 4 | 5 | 6 |',
        '==> +---+---+---+',
        '==> | 7 | 8 | 9 |',
        '==> +---+---+---+',
    ]

    for row_index in POSITION_ROWS.values():
        for position in player_positions:
            if position in board[row_index]:
                board[row_index] = board[row_index].replace(position,
                                                            PLAYER_MARKER)
        for position in computer_positions:
            if position in board[row_index]:
                board[row_index] = board[row_index].replace(position,
                                                            COMPUTER_MARKER)

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

    sorted_list = sorted(ALL_VALID_POSITIONS - occupied_positions)
    int_sorted_list = [int(option) for option in sorted_list]

    while True:
        user_input = input('==> Enter an available position:'
                           f'{join_or(int_sorted_list)} \n').strip()
        if valid_positions(user_input, player_positions, computer_positions):
            return user_input


def join_or(lst, primary_delimeters = ', ', last_delimeter = 'or'):
    '''
    takes up to 3 inputs. first input is mandatory, second and third inputs are
    optional. original list remains intact (is not mutated)

    inputs:
        - list of numbers (not yet designed to handle nested data structures)
        - primary delimeter
        - last delimeter
    output:
        - string to print
    '''
    def wrapper(string):
        '''
        wraps the input in a prompt f-string
        '''
        return f'==> "{string}"'

    str_lst = str(lst).strip('[]')

    match len(lst):
        case 0:
            return wrapper("")
        case 1:
            return wrapper(str_lst)
        case 2:
            return wrapper(f'{lst[0]} or {lst[1]}')
        case _:
            primary_delim_inserted = str_lst.replace(', ', primary_delimeters)
            last_elem_index = primary_delim_inserted.rfind(str(lst[-1]))
            last_delim_inserted = wrapper(
                            f'{primary_delim_inserted[:last_elem_index] +
                            f'{last_delimeter} ' +
                            str(lst[-1])}')
            return last_delim_inserted


def get_computer_input_random(player_positions, computer_positions):
    '''
    computer randomly selects an available position

    Inputs: player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)

    Outputs: computer-selected position (string)
    '''

    print('==> Computer is choosing...')
    time.sleep(COMPUTER_THINK_TIME)
    occupied_positions = player_positions.union(computer_positions)
    return random.choice(list(ALL_VALID_POSITIONS - occupied_positions))


def is_winner(player_positions, computer_positions, current_player):
    '''
    given a set of positions (computer or player), returns True if the input
    occupies a winning position

    Inputs: 
        - set of occupied positions
    Outputs:
        - boolean
    '''

    if 'user' in current_player:
        positions = player_positions
    else:
        positions = computer_positions

    for combo in WINNING_POSITION_COMBOS:
        if positions.intersection(combo) in WINNING_POSITION_COMBOS:
            if 'user' in current_player:
                print('==> Player won!')
            if 'computer' in current_player:
                print('==> Computer won!')
            return True
    return False


def board_is_full(player_positions, computer_positions):
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


def play_another_round():
    '''
    queries user to play again. validates user input

    Input:
        - none
    Output:
        - boolean
    '''

    while True:
        player_input = input('==> Would you like to play another round? y/n\n')
        if player_input in ['y', 'yes', 'Y', 'n', 'no', 'N']:
            if player_input in ['y', 'yes']:
                return True
            if player_input in ['n', 'no']:
                return False
        print('==> Please enter y or n.')


def create_fresh_game_board():
    '''
    clears the console, resets computer and user positions, selects first player
    and prints welcome message and board

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
    current_player = choose_starting_player()
    declare_starting_player(current_player)
    return (player_positions, computer_positions, current_player)


def player_updates_board(player_positions, computer_positions):
    '''
    gets user input, updates player positions, clears console, and updates
    console

    side effects: mutates player positions

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)
    Outputs:
        - None
    '''

    player_input = get_user_input(player_positions, computer_positions)
    player_positions.add(player_input)
    os.system('clear')
    print(f'==> You chose {player_input}')
    display_board(player_positions, computer_positions)
    return (player_positions, computer_positions)


def computer_offensive_strategy(player_positions, computer_positions):
    '''
    computer chooses the remaining position if it is one position away from
    winning

    Inputs:
        - player positions, computer positions
    Outputs:
        - True if computer is about to win
    '''
    # offensive strategy
    computer_about_to_win = False

    for combo in WINNING_POSITION_COMBOS:
        remaining_position = combo - computer_positions
        computer_about_to_win = ((len(computer_positions.intersection(combo))
                                  == 2)and
                                player_positions.isdisjoint(remaining_position))
        if computer_about_to_win:
            print('==> Computer is choosing...')
            time.sleep(COMPUTER_THINK_TIME)
            computer_input = combo.difference(computer_positions)
            computer_positions.update(computer_input)
            break

    return computer_about_to_win


def computer_defensive_strategy(player_positions, computer_positions):
    '''
        computer chooses the remaining position if player is one position away
        from winning

    Inputs:
        - player positions, computer positions
    Outputs:
        - True if player is about to win
    '''
    # defensive strategy
    player_about_to_win = False

    for combo in WINNING_POSITION_COMBOS:
        remaining_position = combo - player_positions
        player_about_to_win = ((len(player_positions.intersection(combo)) == 2)
                            and
                            computer_positions.isdisjoint(remaining_position))
        if player_about_to_win:
            print('==> Computer is choosing...')
            time.sleep(COMPUTER_THINK_TIME)
            computer_input = combo.difference(player_positions)
            computer_positions.update(computer_input)
            break

    return player_about_to_win


def computer_picks_spot_five(player_positions, computer_positions):
    '''
        computer chooses the five position if it is empty

    Inputs:
        - player positions, computer positions
    Outputs:
        - True if picks position five
    '''
    # pick spot #5 if available
    spot_five_picked = False
    if '5' not in player_positions.union(computer_positions):
        print('==> Computer is choosing...')
        time.sleep(COMPUTER_THINK_TIME)
        computer_input = '5'
        computer_positions.update(computer_input)
        spot_five_picked = True

    return spot_five_picked


def computer_selects_randomly(player_positions, computer_positions):
    '''
    computer selects randomly from available positions

    Inputs:
        - player_positions, computer_positions
    Outputs:
        - none
    '''
    # random selection
    computer_input = get_computer_input_random(player_positions,
                                               computer_positions)
    computer_positions.add(computer_input)


def computer_updates_board(player_positions, computer_positions):
    '''
    get computer choice, update computer positions, clears console, and update
    console. computer prioritizes (in descending order) an offensive strategy, a
    defensive strategy, picking an empty spot 5, and a random selection strategy

    side effects: mutates computer positions

    Inputs:
        - player_positions (set of player-occupied positions),
            computer_positions (set of computer-occupied positions)
    Outputs:
        - None
    '''

    before_computer_moves = copy.copy(computer_positions)

    computer_has_moved = False

    if not computer_has_moved:
        computer_has_moved = (
            computer_offensive_strategy(player_positions, computer_positions))
    if not computer_has_moved:
        computer_has_moved = (
            computer_defensive_strategy(player_positions, computer_positions))
    if not computer_has_moved:
        computer_has_moved = (
            computer_picks_spot_five(player_positions, computer_positions))
    if not computer_has_moved:
        computer_selects_randomly(player_positions, computer_positions)

    computer_input = str(computer_positions -
                         before_computer_moves).strip('{}\'')

    os.system('clear')
    print(f'==> Computer chose {computer_input}')
    display_board(player_positions, computer_positions)
    return (player_positions, computer_positions)


def execute_farewell_sequence():
    '''
    displays goodbye message for 5 secons, then clears console
    
    Inputs:
        - none
    Outputs:
        - none
    '''

    print('==> Thank you for playing. Goodbye!')
    time.sleep(5)
    os.system('clear')


def choose_starting_player():
    '''
    selects a starting player randomly

    Inputs:
        - none
    Outputs:
        - none
    '''
    first_player = set()
    first_player.add(random.choice(list(PLAYERS)))
    return first_player


def declare_starting_player(player):
    '''
    prints the first starting player (user or computer) and returns the player

    Inputs:
        - none
    Outputs:
        - none
    '''
    player = str(player)
    player = player.strip('{}\'')
    if player == 'computer':
        print('==> The computer is the starting player.')
    else:
        print('==> You are the starting player.')


def switch_turns(player):
    '''
    returns the next player

    Inputs:
        - current player
    Outputs:
        - next player
    '''
    return PLAYERS - player


def initialize_scores():
    '''
    initialize dict containing player and computer scores

    Inputs:
        - none
    Outputs:
        - score dict
    '''
    return {
        'user': 0,
        'computer': 0,
    }


def tally_score(scores, current_player):
    '''
    updates computer/player score when invoked

    Inputs:
        - scores dict
        - current player set e.g. {'user'}
    Outputs:
        - scores dict
    '''
    if 'computer' in current_player:
        scores['computer'] += 1
    if 'user' in current_player:
        scores['user'] += 1

    return scores


def display_score(scores):
    '''
    displays the current score

    Inputs:
        - scores dict
    Outputs:
        - displays scores to console, returns None
    '''
    print(f'==> Score: Computer - {scores['computer']} , '
          f'Player - {scores['user']}')


def match_winner(scores):
    '''
    prints winning message

    Inputs:
        - scores dict
    Outputs:
        - prints message to console, returns boolean
    '''
    if scores['user'] is WINNING_SCORE:
        print('==> You have won the match!')
        return True
    if scores['computer'] is WINNING_SCORE:
        print('==> The computer has won the match!')
        return True
    return False


def play_another_match():
    '''
    queries user to play again. validates user input

    Input:
        - none
    Output:
        - boolean
    '''

    while True:
        player_input = input('==> Would you like to play another match? y/n\n')
        if player_input in ['y', 'Y', 'yes', 'n', 'N,', 'no']:
            if player_input in ['y', 'Y', 'yes']:
                return True
            if player_input in ['n', 'N', 'no']:
                return False
        print('==> Please enter y or n.')


def main():
    '''
    the main function controls game flow

    Inputs:
        - none
    Outputs:
        - No return value. Prints game display and messages to console
    '''

    (player_positions, computer_positions,
     current_player) = create_fresh_game_board()

    scores = initialize_scores()

    while True:
        if 'user' in current_player:
            player_updates_board(player_positions, computer_positions)
        else:
            computer_updates_board(player_positions, computer_positions)

        if is_winner(player_positions, computer_positions, current_player):
            scores = tally_score(scores, current_player)
            display_score(scores)
            if match_winner(scores):
                if play_another_match():
                    (player_positions, computer_positions,
                    current_player) = create_fresh_game_board()
                    scores = initialize_scores()
                    continue
                break
            if not play_another_round():
                break
            (player_positions, computer_positions,
                current_player) = create_fresh_game_board()
            continue

        if board_is_full(player_positions, computer_positions):
            print('==> It\'s a tie!')
            display_score(scores)
            if not play_another_round():
                break
            (player_positions, computer_positions,
                current_player) = create_fresh_game_board()
            continue

        current_player = switch_turns(current_player)

    execute_farewell_sequence()


main()
