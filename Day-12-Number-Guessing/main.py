from art import logo
import time
from random import randint
from replit import clear

"""
Guessing The Number - Game
My first Project SOLO project
"""
print("Starting the game...")

invalid_ans = True
while invalid_ans:
    print(logo)
    print("The number could be between 1 and 100.")
    difficulty = input("What difficulty would you like? Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        attemps = 10
        invalid_ans = False
    elif difficulty == "hard":
        attemps = 5
        invalid_ans = False
    else:
        print("Error! Invalid option.")
        print("Restarting...")
        time.sleep(3)
        clear()

random_number = randint(1, 100)
print(f"The answer is: {random_number}")

def guess_checker(random_number, guessed_number):
    if guessed_number == random_number:
        print(f"\nYou guessed it! The number was: {random_number}")
        return 1
    if guessed_number > random_number:
        print("Too high\n Guess again.")
        
    else:
        print("Too low\n Guess again.")

for attempt in range(attemps, 0, -1):
    print(f"You have {attempt} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    game = guess_checker(random_number=random_number, guessed_number=player_guess)
    if game == 1:
        print("Exiting...")
        result = 1
        break

result = 0
if result == 0:
    print("\nYou lost all your attempts, you lose.")
    print("Exiting...")




