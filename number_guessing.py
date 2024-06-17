import random

def number_guessing():

    goal = random.randint(100, 999)

    max_guesses = 10
    current_guesses = 0

    print("Guess a random 3-digit number!")