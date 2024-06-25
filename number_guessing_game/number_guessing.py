import hints

def number_guessing(goal, max_guesses, current_guesses):

    while current_guesses < max_guesses:
        try:
            guess = int(input(f"Guess {current_guesses + 1}: "))

            if guess < 100 or guess > 999:
                print("三桁の筋を入力してください。")
        
            elif guess == goal:
                print("正解!")
                break

            else:
                current_guesses += 1
                if current_guesses == max_guesses:
                    print(f"推測の回数が尽きました :( 正解の数字は {goal}でした。")
                    break

                hints.higher_lower(guess, goal)

                hint2 = input("もう一つのヒントが欲しい? (y/n) ")
                if hint2 == "y":
                    hints.compare_digits(guess, goal)

                    hint3 = input("第三のヒントが欲しい? (y/n) ")
                    if hint3 == "y":
                        hints.even_odd(goal)
                    elif hint3 == "n":
                        pass
                    else:
                        print("「y」か「n」を入力してください。")
                        
                elif hint2 == "n":
                    pass
                else:
                    print("「y」か「n」を入力してください。")

        except ValueError:
            print("Invalid input. 三桁の数字を入力してください。")