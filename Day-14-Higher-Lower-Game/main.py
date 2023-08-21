# Import random, replit(clear), game data and art.
from art import logo, vs
import random
from game_data import data
from replit import clear

print("Starting...")
# Print the logo of the game "Higher Lower"
print(logo)

# Track the score
player_score = 0

# List of dictionaries to use the random function
accounts = list(data)

# Create a while loop and the condition not player_lose
lose = False
while not lose:
    # Get the random accounts from the list
    if player_score == 0:
        account_a = random.choice(accounts)
    else:
        account_a = account_b
    account_b = random.choice(accounts) 
    
    # Messages
    message_a = f'Compare A: {account_a["name"]}, {account_a["description"]}, {account_a["country"]}.'
    
    message_b = f'Compare B: {account_b["name"]}, {account_b["description"]}, {account_b["country"]}.'

    # Displaying the info to the player
    print(message_a)
    print(vs)
    print(message_b)

    invalid_letter = True
    while invalid_letter:
        # Ask the user for input
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
        if player_choice != 'a' and player_choice != 'b':
            print("Error! Invalid letter")
        else:
            invalid_letter = False
    
    # Conditions
    # Checking which account has more followers
    if account_a["follower_count"] > account_b["follower_count"]:
        most_followers = "a"
    else:
        most_followers = "b"
    
    # Clear the screen
    clear()
    print(logo)

    # Checking if the player_choice is correct.
    if player_choice == most_followers:
        player_score += 1
        print(f"You're right! Current score: {player_score}")
    else:
        # End the game
        print(f"Sorry, that's wrong. Final score: {player_score}")
        lose = True

print("Exiting...")


