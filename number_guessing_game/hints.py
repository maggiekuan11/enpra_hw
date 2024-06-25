def higher_lower(guess, goal):
    if guess < goal:
        print("The goal is higher.")
    else:
        print("The goal is lower.")

def compare_digits(guess, goal):

    goal_str = str(goal)
    guess_str = str(guess)

    for i in range(3):
        if guess_str[i] < goal_str[i]:
            print("↑  ", end="")
        elif guess_str[i] == goal_str[i]:
            print("=  ", end="")
        else:
            print("↓  ", end="")
    print()

def even_odd(goal):
    if goal % 2 == 0:
        print("The goal is even.")
    else:
        print("The goal is odd.")