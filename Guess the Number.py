# Guess the Number

import random

num_guess = 0

print("Welcome to the Guess the Number game!\n") # Welcomes the user to the game

player_name = input("What should I call you? Please enter your name and press [ENTER]\n")

print(f"Nice to meet you {player_name}! Lets start the game.\n")

rand_num = random.randint(1,20)

print(f"Now {player_name} you will have to guess a number between 1 - 20. You will have 5 guesses.\n")

for num_guess in range(5):
    player_guess = int(input("Please guess a whole number between 1 - 20 and press [Enter]\n"))

    if player_guess < rand_num:
        print("That number is too low. Try again")
    elif player_guess > rand_num:
        print("That numer is too high. Try again")
    else:
        break

if player_guess == rand_num: # Did the player guess the number correctly?
    num_guess += 1
    print(f"Congrats {player_name} you guessed the correct number! You used {num_guess} guesses\n")
else:
    print(f"Sorry {player_name} you did not guess the correct number. The number was {rand_num}.\n")