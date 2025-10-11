# Number Guessing Game - Level 2
# Beginner/Intermediate Python Project
# Date: 2025-10-11
#
# Instructions:
# - The computer picks a random number from 1 to 50
# - You have 5 attempts to guess it
# - Feedback is provided: "Too High" / "Too Low"
# - Tracks Wins and Losses across multiple games
# - Handles invalid input gracefully
# - You can quit after each game by typing Y when prompted

import random as r

Wins = 0
Losses = 0
while True:
    GameOn = True
    Win = False
    Lose = False
    attempts = 0
    max_attempts = 5
    secret_number = r.randint(1,50)
    print("Welcome to the Number Guessing Game!")
    while GameOn:
        try:
            guess = int(input("Guess: "))
            if guess > secret_number:
                attempts += 1
                print("Too High! Try Again!")
                print(f"You Have {max_attempts-attempts} attempts left!")
            elif guess < secret_number:
                attempts += 1
                print("Too Low! Try Again!")
                print(f"You Have {max_attempts-attempts} attempts left!")
            if attempts == max_attempts and guess != secret_number:
                Losses += 1
                GameOn = False
                Lose = True
            if guess == secret_number:
                Wins += 1
                GameOn = False
                Win = True
        except ValueError:
            print("Guess a Valid Number!")
    if GameOn == False and Lose:
        print(f"You Lost the Game! The Number was {secret_number}")
        print(f"Now You Have {Losses} Losses!")
        quit_choice = input("Do You Wanna Quit the Game? Y/N : ").upper()
        if quit_choice == "Y":
            break
        else:
            continue
    elif GameOn == False and Win:
        print("You Won the Game!")
        print(f"Now You Have {Wins} Wins!")
        quit_choice = input("Do You Wanna Quit the Game? Y/N : ").upper()
        if quit_choice == "Y":
            break
        else:
            continue
