import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

WINNING_LIMIT = 21
DEALER_LIMIT = 17

def prompt(message):
    print(f"=> {message}")

def initialize_deck():
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)
    return deck

def total(cards):
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= WINNING_LIMIT:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def busted(player_total):
    return player_total > WINNING_LIMIT

def detect_result(dealer_total, player_total):

    if player_total > WINNING_LIMIT:
        return 'PLAYER_BUSTED'
    elif dealer_total > WINNING_LIMIT:
        return 'DEALER_BUSTED'
    elif dealer_total < player_total:
        return 'PLAYER'
    elif dealer_total > player_total:
        return 'DEALER'
    else:
        return 'TIE'

def display_results(dealer_total, player_total):
    result = detect_result(dealer_total, player_total)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")


def play_again():
    print("-------------")
    valid_inputs = ['y', 'Y', 'Yes', 'yes', 'n', 'N', 'No', 'no']
    while True:
        answer = input('Do you want to play again? (y or n) ')
        if answer in valid_inputs:
            return answer in ['y', 'Y', 'Yes', 'yes']
        print(f'Valid inputs are {', '.join(valid_inputs)}')

def pop_two_from_deck(deck):
    return [deck.pop(), deck.pop()]

def hand(cards):
    return ', '.join(cards)

def grand_output(dealer_cards, dealer_total, player_cards, player_total):
    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {dealer_total}")
    prompt(f"Player has {hand(player_cards)}, for a total of: {player_total}")
    print('==============')

def update_score(player_total, dealer_total, player_score, dealer_score):
    if player_total > dealer_total:
        player_score += 1
    if player_total < dealer_total:
        dealer_score += 1

    return player_score, dealer_score

def match_winner(player_score, dealer_score):
    if player_score >= 3:
        print('Player is the first to reach 3 points! Player wins match.')
        return "Player"
    if dealer_score >= 3:
        print('Dealer is the first to reach 3 points! Dealer wins match.')
        return "Dealer"
    return None

def display_score(player_score, dealer_score):
    print(f'Player score is: {player_score}. Dealer score is: {dealer_score}')

player_score = 0
dealer_score = 0

while True:
    prompt('Welcome to Twenty-One!')

     # initial deal
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)


    prompt(f"Dealer has {dealer_cards[0]} and ?")
    prompt(f"You have: {player_cards[0]} and {player_cards[1]}, for a total of {player_total}.")

    # player turn
    while True:
        player_choice = input("Would you like to (h)it or (s)tay? ")
        if player_choice not in ['h', 's']:
            prompt("Sorry, must enter 'h' or 's'.")
            continue

        if player_choice == 'h':
            player_cards.append(deck.pop())
            prompt('You chose to hit!')
            prompt(f"Your cards are now: {hand(player_cards)}")
            player_total = total(player_cards)
            prompt(f"Your total is now: {player_total}")

        if player_choice == 's' or busted(player_total):
            break

    if busted(player_total):
        grand_output(dealer_cards, dealer_total, player_cards, player_total)
        display_results(dealer_total, player_total)
        dealer_score += 1
        display_score(player_score, dealer_score)
        if match_winner(player_score, dealer_score):
            break
        if play_again():
            continue
    else:
        prompt(f"You stayed at {player_total}")

    # dealer turn
    prompt("Dealer's turn...")

    while dealer_total < DEALER_LIMIT:
        prompt("Dealer hits!")
        dealer_cards.append(deck.pop())
        dealer_total = total(dealer_cards)
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

    if busted(dealer_total):
        prompt(f"Dealer total is now: {dealer_total}")
        grand_output(dealer_cards, dealer_total, player_cards, player_total)
        display_results(dealer_total, player_total)
        player_score += 1
        display_score(player_score, dealer_score)
        if match_winner(player_score, dealer_score):
            break
        if play_again():
            continue
    else:
        prompt(f"Dealer stays at {dealer_total}")

    # both player and dealer stays - compare cards!

    grand_output(dealer_cards, dealer_total, player_cards, player_total)

    display_results(dealer_total, player_total)

    player_score, dealer_score = update_score(player_total, dealer_total,
                                              player_score, dealer_score)

    display_score(player_score, dealer_score)

    if match_winner(player_score, dealer_score):
        break

    if not play_again():
        break

    '''
    do we need to calculate the total() so often?
    - total is currently calculated when: 
        result is being detected -> can get from total in main loop
        after player's initial hand is dealt -> can get from total in main loop
        after a hit -> update total
        after a stay -> can get from total in main loop
        dealer hit while loop -> can get from total in main loop, update total
        if dealer busted -> can get from total in main loop
        if dealer stayed -> can get from total in main loop
        final player results -> can get from total in main loop
        final dealer results -> can get from total in main loop
    '''

    '''
    The last play_again call

    the last play_again call is different from the first two in that a break statement
    follows, whereas a continue statement follows each of the first two calls.

    since the last play_again call is at the end of the main while loop, there is
    no need to continue over the loop if the player decides to continue playing.
    there is no code to run after the last play_again call

    in the other two play_again calls, Python must skip over the remaining code
    (dealer decisions, game result messages) if the player decides to play again
    '''

    '''
    ending the round

    extracted grand output to a function and invoked function when either player
    busts
    '''

    '''
    best of five

    each opponent starts with a score of 0. when one opponent busts the other gains
    a point. opponent also scores when they win with a higher score
    '''

    '''
    more constants

    set constants for winning limit and dealer limit (21 and 17)
    '''

    '''
    improve input handling


    
    '''