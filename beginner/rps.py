# Project: Rock/Paper/Scissors
# Date: 04.10.2025
# Description: Raw beginner-level RPS game

import random
def RockPaperScissors():
    wins = 0
    draws = 0
    loses = 0
    while True:
        print("Welcome to Rock/Paper/Scissors!")
        enemyrps = random.choice(["Rock","Paper","Scissors"])
        yourps = input("What do you wanna choose? Rock/Paper/Scissors:")
        yrp = yourps.upper()
        if enemyrps == "Rock" and yrp == "ROCK":
            draws += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"Its a draw! Your Draws are {draws} now!")
      
        elif enemyrps == "Rock" and yrp == "PAPER":
            wins += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Won the Round!! Your Wins are {wins} now!")
       
        elif enemyrps == "Rock" and yrp == "SCISSORS":
            loses += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Lost the Round! Your Loses are {loses} now!")
        
        elif enemyrps == "Paper" and yrp == "ROCK":
            loses += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Lost the Round! Your Loses are {loses} now!")
         
        elif enemyrps == "Paper" and yrp == "PAPER":
            draws += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"Its a Draw! Your Draws are {draws} now!")
         
        elif enemyrps == "Paper" and yrp == "SCISSORS":
            wins += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Won the Round! Your Loses are {wins} now!")
        
        elif enemyrps == "Scissors" and yrp == "ROCK":
            wins += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Won the Round! Your Wins are {wins} now!")
           
        elif enemyrps == "Scissors" and yrp == "PAPER":
            loses += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"You Lost the Round! Your Loses are {loses} now!")

        elif enemyrps == "Scissors" and yrp == "SCISSORS":
            draws += 1
            print(f"Enemy Chose {enemyrps.upper()}!")
            print(f"You Chose {yrp}")
            print(f"Its a Draw! Your Draws are {draws} now!")

        stats = input("Do You Wanna See Your Stats? Y/N: ").upper()
        if stats == "Y":
            print(f"Wins - {wins}!")
            print(f"Loses - {loses}!")
            print(f"Draws - {draws}!")
        quit = input("Do You Wanna Quit the Game? Y/N: ").upper()
        if quit == "Y":
            break

RockPaperScissors()
    
