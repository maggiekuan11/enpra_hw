import random

def number_guessing():

    goal = random.randint(100, 999)

    max_guesses = 3
    current_guesses = 0

    if current_guesses == max_guesses:
        print("You've run out of guesses :( the correct number was {goal})")

    else:
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
            current_guesses += 1

def main():
    print("Guess a random 3-digit number!")
    number_guessing()

if __name__ == "__main__":
    main()

