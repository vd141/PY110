'''
Requirements:
    - standard 52 card deck with 4 suits
    - objective of the game is to get as close to 21 as possible without going
      over
    - dealer and a player are the opponents
    - each opponent is initially dealt a hand of two cards
    - numbered cards are worth their face value
    - court cards are worth 10
    - ace is worth 1 or 11
        - ace is worth 11 if the total value of hand doesn't exceed 21
        - if it does, ace must take on the lower value
    - player can either hit or stay
    - dealer hit/stay algorithm: dealer hits until the total is at least 17. if
      dealer busts, the player wins
    - when both the player and the dealer stay, it's time to compare the total
      value of the cards to see who has the higher value

    Pseudocode:
        1. Dealer and player are both dealt two random cards each
        2. player makes first move: hit or stay
            - if hit, the total must be 21 or under. otherwise, bust and dealer
              wins
            - player can continue to hit until stay or bust
        3. if player stays, dealer can make a move
            - hit if the total in hand is less than 17
            - if over 21, dealer busts and player wins
            - if total in hand is 17 or over, dealer stays
        4. compare hands and declare winner

    Data structures:
        - set of cards
            - keys are strings, values are values. value of ace will be list [1,
              11]
        - cards in player hand
            - key:value pairs
        - cards in computer hand
            - key:value pairs
        - 
    
    Functions:
        - function to initialize card deck. Card deck will not be a constant as
          its contents will change as opponents hit the deck
        - deal card from original set of cards
        - evaluate hand total
        - evaluate whether ace in hand is 11 or 1
        - hit function - get/validate input and hit
        - stay function - get/validate input and pass turn to next player
        - 
'''
import random
import copy
import time
import os

DEALER_HIT_LIMIT = 17
BUST_LIMIT = 21

def initialize_card_deck():
    '''
    Initializes a dict of 52 cards. Keys are card names and values are card
    values.
    Aces have have a value of 'Ace'

    Inputs:
        - none
    Outputs:
        - dict of 52 cards
    '''

    # suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    suits = ["\u2660",  # Spades (♠)
              "\u2665",  # Hearts (♥)
              "\u2666",  # Diamonds (♦)
              "\u2663"]  # Clubs (♣)
    face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    names = [f'{face_name} of {suit}' for suit in suits
                                      for face_name in face_names]
    return {name: values[index] for index, name in enumerate(names)}


def deal_card(deck):
    '''
    Pops one card from the card deck and returns it as a dict
    
    Inputs:
        - card deck
    Outputs:
        - single card dict
    '''

    selected_card = random.choice(list(deck.keys()))
    selected_card_value = deck.pop(selected_card)
    return {selected_card: selected_card_value}


def initialize_hands(deck):
    '''
    returns initial hands of player and dealer

    Input:
        - none
    Output:
        - player hand, dealer hand
    '''

    dealer_hand = deal_card(deck)
    dealer_hand.update(deal_card(deck))

    player_hand = deal_card(deck)
    player_hand.update(deal_card(deck))

    return (player_hand, dealer_hand)


def evaluate_hand_total(hand):
    '''
    iterates through each of the hand's values. adds the value to the running
    total. if the value is a list (ace), add that to the total number of aces.

    if there are no aces, simply return the running total

    if there is at least one ace, return the running_total + num_aces if the
    sum is greater than or equal to 21

    if the sum is below 21, the function can test the ace values

    in a hand of at least one ace, only one can be 11 with the possibility of 
    the total sum being under 21

    so if one of the aces takes on the value of 11 and the total sum remains
    under 21, we can return that sum

    otherwise, the total sum will be the number of aces + the running total of
    all other cards

    '''

    num_aces = 0
    running_total = 0

    for card_value in hand.values():
        if not isinstance(card_value, str):
            running_total += card_value
        else:
            num_aces += 1

    if num_aces == 0:
        return running_total
    if 11 + (num_aces - 1) + running_total <= BUST_LIMIT:
        return 11 + (num_aces - 1) + running_total
    return num_aces + running_total


def is_bust(hand):
    '''
    determines if the hand's total is a bust

    Inputs:
        - hand of cards
    Outputs:
        - boolean True if bust, False otherwise
    '''

    if evaluate_hand_total(hand) > BUST_LIMIT:
        return True
    return False


def display_dealer_initial_hand(hand):
    '''
    displays the first card of the dealer's hand

    Input:
        - dealer hand
    Output:
        - print to console, returns None
    '''

    first_card = list(hand.keys())[0]
    print(f'==> Dealer has: {first_card} and a hidden card')


def join_and(lst, primary_delimeters = ', ', last_delimeter = 'and'):
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

    str_lst = str(lst).strip('[]').replace('\'', '')

    match len(lst):
        case 0:
            return ""
        case 1:
            return str_lst
        case 2:
            return f'{lst[0]} and {lst[1]}'
        case _:
            primary_delim_inserted = str_lst.replace(', ', primary_delimeters)
            last_elem_index = primary_delim_inserted.rfind(str(lst[-1]))
            last_delim_inserted = f'{primary_delim_inserted[:last_elem_index] +
                            f'{last_delimeter} ' +
                            str(lst[-1])}'
            return last_delim_inserted


def display_player_hand(hand, message):
    '''
    displays all cards in the player's hand and hand's total value
    '''

    full_hand = list(hand.keys())
    string_to_insert = join_and(full_hand)
    hand_total = evaluate_hand_total(hand)
    print(f'==> {message}: {string_to_insert}, totaling {hand_total}.')


def player_choice(player_hand, deck):
    '''
    adds a card to the players hand if the player hits. does nothing if player
    stays. returns the player_hand in both cases.

    Input:
        - player's hand (dict), deck (dict)
    Output:
        - [player's hand]
    '''

    while True:
        choice = input('==> Hit or stay?\n')
        if choice in ['h', 'H', 'hit', 'Hit']:
            player_hand.update(deal_card(deck))
            break
        if choice in ['s', 'S', 'stay', 'Stay']:
            print('==> You stayed.')
            break
        print('==> Please select hit or stay.')

    return player_hand


def dealer_strategy(dealer_hand, deck):
    '''
    if the computer's total hand value is less than 17, it hits. if it is
    greater, it stays

    Input:
        - dealer hand, deck
    Output:
        - dealer hand
    '''
    time.sleep(1)
    print('==> Dealer\'s turn...')
    time.sleep(2)
    if evaluate_hand_total(dealer_hand) < DEALER_HIT_LIMIT:
        new_card = deal_card(deck)
        dealer_hand.update(new_card)
        card = list(new_card.keys())[0]
        print(f'==> Dealer hits and draws: {card}.')
        return dealer_hand
    print('==> Dealer stays.')
    time.sleep(2)
    return dealer_hand


def player_turn(player_hand, deck):
    '''
    displays player hand, allows player to make a H or S choice,
    determines if there is a bust

    returns player hand and dealer_win status
    '''

    dealer_wins = False
    while True:
        display_player_hand(player_hand, 'You have')
        prev_player_hand = copy.copy(player_hand)
        player_hand = player_choice(player_hand, deck)
        if is_bust(player_hand):
            display_player_hand(player_hand, 'You have')
            print('==> Player busts, dealer wins!')
            dealer_wins = True
            break
        if prev_player_hand == player_hand:
            break

    return dealer_wins, player_hand


def computer_turn(dealer_hand, deck, dealer_wins):
    '''
    executes dealer strategy if dealer has not won (bc of player bust)
    determines if dealer busted
    '''

    player_wins = False
    while not dealer_wins:
        prev_dealer_hand = copy.copy(dealer_hand)
        dealer_hand = dealer_strategy(dealer_hand, deck)
        if is_bust(dealer_hand):
            print('==> Dealer busts, player wins!')
            player_wins = True
            break
        if prev_dealer_hand == dealer_hand:
            break

    return player_wins, dealer_hand


def display_game_results(player_hand, dealer_hand, player_wins, dealer_wins):
    '''
    calculates game results and determines winner
    '''
    total_player_hand = evaluate_hand_total(player_hand)
    total_dealer_hand = evaluate_hand_total(dealer_hand)
    print(f'==> Your final hand is: {join_and(list(player_hand.keys()))}. '
          f'The dealer\'s final hand is: {join_and(list(dealer_hand.keys()))}')
    time.sleep(1)
    print(f'==> Player\'s total hand is {total_player_hand}.')
    time.sleep(1)
    print(f'==> Dealer\'s total hand is {total_dealer_hand}.')
    time.sleep(1)
    if (not player_wins) and (not dealer_wins):
        if total_player_hand > total_dealer_hand:
            print('==> Player wins!')
        elif total_dealer_hand > total_player_hand:
            print('==> Dealer wins!')
        else:
            print('==> It\'s a tie!')


def main():
    '''
    game flow
    '''

    os.system('clear')
    deck = initialize_card_deck()
    player_hand, dealer_hand = initialize_hands(deck)
    display_dealer_initial_hand(dealer_hand)

    dealer_wins, player_hand = player_turn(player_hand, deck)
    player_wins, dealer_hand = computer_turn(dealer_hand, deck, dealer_wins)

    display_game_results(player_hand, dealer_hand, player_wins, dealer_wins)


main()
