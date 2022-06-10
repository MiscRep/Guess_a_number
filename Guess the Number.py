# Guess the Number

import random

num_guess = 0

print("Welcome to the Guess the Number game!\n") # Welcomes the user to the game

player_name = input("What should I call you? Please enter your name and press [ENTER]\n")

print(f"Nice to meet you {player_name}! Lets start the game.\n")

rand_num = random.randint(1,20)