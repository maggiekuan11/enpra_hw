import random

goal = random.randint(100, 999)

max_guesses = 3
current_guesses = 0

def compare_digits(guess):

    goal_str = str(goal)
    guess_str = str(guess)

    for i in range(3):
        if guess_str[i] < goal_str[i]:
            print("↑")
        elif guess_str[i] == goal_str[i]:
            print("=")
        else:
            print("↓")

def number_guessing():

    global current_guesses

    while current_guesses < max_guesses:
        try:
            guess = int(input(f"Guess {current_guesses + 1}: "))

            if guess < 100 or guess > 999:
                print("Please enter a 3-digit number.")
        
            elif guess == goal:
                print("Correct!")
                break

            else:
                current_guesses += 1
                if current_guesses == max_guesses:
                    print(f"You've run out of guesses :( The correct number was {goal}")
                    break
                if guess < goal:
                    print("The number is higher.")
                else:
                    print("The number is lower.")

                hint2 = input("Want another hint? (y/n) ")
                if hint2 == "y":
                    compare_digits(guess)
                elif hint2 == "n":
                    pass
                else:
                    print("Please type y or n.")

        except ValueError:
            print("Invalid input. Please enter a valid 3-digit number.")

        

def main():
    print("Guess a random 3-digit number!")
    number_guessing()

if __name__ == "__main__":
    main()

