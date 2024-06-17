import random

def number_guessing():

    goal = random.randint(100, 999)

    max_guesses = 10
    current_guesses = 0

    print("Guess a random 3-digit number!")

    while max_guesses < current_guesses:
        guess = int(input(f"Guess {current_guesses + 1}: "))

        if guess < 100 or guess > 999:
            print("Please enter a 3-digit number.")
        
        elif guess == goal:
            print("Correct!")

        else:
            if guess < goal:
                print("The number is higher")

            else:
                print("The number is lower")

