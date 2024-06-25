def higher_lower(guess, goal):
    if guess < goal:
        print("正解の数字はもっと大きいです。")
    else:
        print("正解の数字はもっと小さいです。")

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
        print("正解の数字は偶数です。")
    else:
        print("正解の数字は奇数です。")