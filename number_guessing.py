import random
import hints

goal = random.randint(100, 999)

max_guesses = 3
current_guesses = 0

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

                hints.higher_lower(guess, goal)

                hint2 = input("Want another hint? (y/n) ")
                if hint2 == "y":
                    hints.compare_digits(guess, goal)

                    hint3 = input("Want a 3rd hint? (y/n) ")
                    if hint3 == "y":
                        hints.even_odd(goal)
                    elif hint3 == "n":
                        pass
                    else:
                        print("Please enter 'y' or 'n'.")
                        
                elif hint2 == "n":
                    pass
                else:
                    print("Please enter 'y' or 'n'.")

        except ValueError:
            print("Invalid input. Please enter a valid 3-digit number.")

def main():
    print("Guess a random 3-digit number!")
    number_guessing()

if __name__ == "__main__":
    main()

#For the second hint: ↑ means guess higher, ↓ means guess lower, = means correct number.

