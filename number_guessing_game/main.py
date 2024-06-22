import random
import number_guessing

goal = random.randint(100, 999)

max_guesses = 3
current_guesses = 0

def main():
    print("Guess a random 3-digit number!")
    number_guessing.number_guessing(goal, max_guesses, current_guesses)

if __name__ == "__main__":
    main()

#For the second hint: ↑ means guess higher, ↓ means guess lower, = means correct number.

