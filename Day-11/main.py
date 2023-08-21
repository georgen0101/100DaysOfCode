############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

"""
Blackjack Capstone Project
Dificulty Hard - George
"""
from random import choice
from replit import clear
from art import logo

print("Starting...")

# Dealing the cards randomly
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
house_hand = []

for i in range(2):
    player_hand.append(choice(cards))
    house_hand.append(choice(cards))
# print(player_hand)
# print(house_hand)

print(logo)

def initial_stage():
    # Hands score
    house_score = sum(house_hand)
    player_score = sum(player_hand)
    
    
    # Detect if the house or user have a blackjack
    if sum(house_hand) == 21:
        print("Blackjack 21 - House")
        quit()
    elif sum(player_hand) == 21:
        print("Blackjack 21 - Player")
        quit()
    
    # Detect an ace score over 21
    if player_score > 21:
        if 11 in player_hand:
            index = player_hand.index(11)
            player_hand[index] = 1
            initial_stage()
        else:
            print("Player lost over 21")
            print(f"Your cards: {player_hand} Total score: {player_score}")
            print(f"House first card: {house_hand[0]}")
            quit()

    # Feedback for the player
    print(f"Your cards: {player_hand} Total score: {player_score}")
    print(f"House first card: {house_hand[0]}")
    # Ask for another card?, # Game ends
    new_card = input("hit or pass?")
    
    # Ending
    if new_card == "hit":
        player_hand.append(choice(cards))
        initial_stage()
    elif new_card == "pass":
        if house_score < 16:
            while sum(house_hand) < 16:
                house_hand.append(choice(cards))
                house_score = sum(house_hand)
        elif house_score > 21:
            if 11 in house_hand:
                index = house_hand.index(11)
                house_hand[index] = 1
                over16()
            else:
                print("House lost over 21")
                print(f"Your cards: {player_hand} Total score: {player_score}")
                print(f"House cards: {house_hand}")
                quit()
        # else:
        # Winning conditions
        if player_score == house_score:
            print("Draw")
        elif player_score > house_score:
            print("Player wins")
        elif player_score < house_score:
            print("House wins")
        # Feedback
        print(f"Your cards: {player_hand}, total score {player_score}")
        print(f"House card: {house_hand}, total score {house_score}")
        quit()
        print("Exiting...")
initial_stage()      

