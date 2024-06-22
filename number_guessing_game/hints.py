def higher_lower(guess, goal):
    if guess < goal:
        print("The number is higher.")
    else:
        print("The number is lower.")

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
        print("The number is even.")
    else:
        print("The number is odd.")