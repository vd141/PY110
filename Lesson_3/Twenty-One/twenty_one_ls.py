import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

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
        if sum_val <= 21:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def busted(player_total):
    return player_total > 21

def detect_result(dealer_total, player_total):

    if player_total > 21:
        return 'PLAYER_BUSTED'
    elif dealer_total > 21:
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
    answer = input('Do you want to play again? (y or n) ')
    return answer == 'y'

def pop_two_from_deck(deck):
    return [deck.pop(), deck.pop()]

def hand(cards):
    return ', '.join(cards)

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
        display_results(dealer_total, player_total)
        if play_again():
            continue
    else:
        prompt(f"You stayed at {player_total}")

    # dealer turn
    prompt("Dealer's turn...")

    while dealer_total < 17:
        prompt("Dealer hits!")
        dealer_cards.append(deck.pop())
        dealer_total = total(dealer_cards)
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

    if busted(dealer_total):
        prompt(f"Dealer total is now: {dealer_total}")
        display_results(dealer_total, player_total)
        if play_again():
            continue
    else:
        prompt(f"Dealer stays at {dealer_total}")

    # both player and dealer stays - compare cards!

    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {dealer_total}")
    prompt(f"Player has {hand(player_cards)}, for a total of: {player_total}")
    print('==============')

    display_results(dealer_total, player_total)

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

