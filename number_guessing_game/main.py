import random
import number_guessing

goal = random.randint(100, 999)

max_guesses = 5
current_guesses = 0
max_points = 10

def main():
    print("Welcome to Number Guessing Game! If you are unsure of anything, please read the README.")
    print("ようこそ数字当てゲームへ! 何か不明な点があれば、READMEを読んでください。")
    print()
    print("Let's begin: Guess a random 3-digit number!")
    print("始めましょう: ランダムな三桁の数字を当ててみてください!")
    number_guessing.number_guessing(goal, max_guesses, current_guesses, max_points)

if __name__ == "__main__":
    main()

