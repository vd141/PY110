'''
Requirements:
    - standard 52 card deck with 4 suits
    - objective of the game is to get as close to 21 as possible without going over
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
            - keys are strings, values are values. value of ace will be list [1, 11]
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

import pprint

def initialize_card_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']
    values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    names = [f'{face_name} of {suit}' for suit in suits
                                      for face_name in face_names]
    return {name: values[index] for index, name in enumerate(names)}
    

    

def deal_card():
    pass

def evaluate_hand_total():
    pass

def choose_ace_value():
    pass

def hit():
    pass

def stay():
    pass

def main():
    deck = initialize_card_deck()


main()