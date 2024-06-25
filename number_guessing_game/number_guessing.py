import hints

def number_guessing(goal, max_guesses, current_guesses, max_points):
    current_points = max_points

    while current_guesses < max_guesses:
        try:
            guess = int(input(f"Guess {current_guesses + 1}: "))

            if guess < 100 or guess > 999:
                print("三桁の筋を入力してください。")
        
            elif guess == goal:
                print("正解!")
                print(f"Points = {current_points} / {max_points}")
                break

            else:
                current_guesses += 1
                if current_guesses == max_guesses:
                    print(f"推測の回数が尽きました :( 正解の数字は {goal}でした。")
                    print(f"Points = {current_points} / {max_points}")
                    break

                hints.higher_lower(guess, goal)

                hint2 = input("もう一つのヒントが欲しい? (y/n) ")
                while hint2 != "y" and hint2 != "n":
                    print("「y」か「n」を入力してください。")
                    hint2 = input("もう一つのヒントが欲しい? (y/n) ")
                if hint2 == "y":
                    current_points -= 1
                    hints.compare_digits(guess, goal)

                    hint3 = input("第三のヒントが欲しい? (y/n) ")
                    while hint3 != "y" and hint3 != "n":
                        print("「y」か「n」を入力してください。")
                        hint3 = input("第三のヒントが欲しい? (y/n) ")

                    if hint3 == "y":
                        current_points -= 1
                        hints.even_odd(goal)
                    else:
                        pass
                        
                else:
                    pass
                

        except ValueError:
            print("Invalid input. 三桁の数字を入力してください。")