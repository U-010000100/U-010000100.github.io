# The perfect guess
import random
import datetime
import os
class delay():
    def one_second_delay():
        a = datetime.datetime.today()
        b = str(a)
        c = b[17:21]
        second_ = c[0:2]
        if second_=="59":
            second = "00"
        else:
            second__ = int(second_)
            second___ = second__+1
            second____ = str(second___)
            if len(second____)==1:
                second = f"0{second____}"
            else:
                second = second____
        miliseconds = c[2:4]
        upto_time = second+miliseconds
        while 1==1:
            d = datetime.datetime.today()
            e = str(d)
            f = e[17:21]
            if f==upto_time:
                break
            else:
                continue
    def two_second_delay():
        delay.one_second_delay()
        delay.one_second_delay()
blank = '''















































\n'''
hardness = None
def hardness_selector():
    global hardness
    while (True):
        print("Select the level of hardness:-")
        print("Easy (Range : 1 to 10)    / 1\nMedium (Range : 1 to 100) / 2\nHard (Range : 1 to 1000)  / 3")
        level = input("Choose (Name or number) : ")
        level_ = level.lower()
        if level_=="exit":
            exit()
        elif level_=="1" or level_.startswith("e"):
            hardness = "easy"
            print(blank)
            break
        elif level_=="2" or level_.startswith("m"):
            hardness = "medium"
            print(blank)
            break
        elif level_=="3" or level_.startswith("h"):
            hardness = "hard"
            print(blank)
            break
        else:
            print("Try again.")
            delay.one_second_delay()
            print(blank)
def game():
    print(blank)
    print("The Perfect Guess\nGuess the right number :)")
    while (True):
        number = 0
        delay.two_second_delay()
        print(blank)
        hardness_selector()
        print("Enjoy the game :)")
        delay.one_second_delay()
        print(blank)
        if hardness=="easy":
            number = random.randint(1, 10)
        elif hardness=="medium":
            number = random.randint(1, 100)
        elif hardness=="hard":
            number = random.randint(1, 1000)
        else:
            print("Repair code.")
            exit()
        user_guess = None
        guesses = 0
        print("Number has been selected.")
        while user_guess!=number:
            user_guess = input("What the number can be : ")
            if user_guess=="exit":
                exit()
            try:
                user_guess = int(user_guess)
            except Exception:
                print("Please type only number.")
                print(blank)
                continue
            else:
                pass
            if user_guess>number:
                print(blank)
                print("Your guess is greater than the number.")
                delay.two_second_delay()
                guesses += 1
            elif user_guess<number:
                print(blank)
                print("Your guess is smaller than the number")
                delay.two_second_delay()
                guesses += 1
            elif user_guess==number:
                print(blank)
                print("You guessed the right number.")
                print(f"The number is {number}")
                delay.two_second_delay()
                guesses += 1
            else:
                print("Repair the code.")
                exit()
        cwd = os.getcwd()
        os.mkdir(f"{cwd}/TGP_scores")
        path_1 = f"{cwd}/Easy_score.txt"
        path_2 = f"{cwd}/Medium_score.txt"
        path_3 = f"{cwd}/Hard_score.txt"
        if hardness=='easy':
            try:
                with open(path_1, "r") as file:
                    score = file.read()
            except FileNotFoundError:
                with open(path_1, "w") as file:
                    file.write("")
                score = None
            except Exception:
                print("Repair the code.")
                exit()
            else:
                try:
                    score = int(score)
                except Exception:
                    with open(path_1, "w") as file:
                        file.write("")
                    score = None
                else:
                    pass
            hi_score = score
        elif hardness=='medium':
            try:
                with open(path_2, "r") as file:
                    score = file.read()
            except FileNotFoundError:
                with open(path_2, "w") as file:
                    file.write("")
                score = None
            except Exception:
                print("Repair the code.")
                exit()
            else:
                try:
                    score = int(score)
                except Exception:
                    with open(path_2, "w") as file:
                        file.write("")
                    score = None
                else:
                    pass
            hi_score = score
        elif hardness=='hard':
            try:
                with open(path_3, "r") as file:
                    score = file.read()
            except FileNotFoundError:
                with open(path_3, "w") as file:
                    file.write("")
                score = None
            except Exception:
                print("Repair the code.")
                exit()
            else:
                try:
                    score = int(score)
                except Exception:
                    with open(path_3, "w") as file:
                        file.write("")
                    score = None
                else:
                    pass
            hi_score = score
        else:
            print("Repair the code")
            exit()
        score_made = guesses
        if hi_score==None:
            high_score = "None"
        else:
            high_score = hi_score
        print(blank)
        if high_score=="None":
            print("You made a new high score!")
            print("Score : ",score_made)
            score_made_ = str(score_made)
            if hardness=="easy":
                with open(path_1, "w") as file:
                    file.write(score_made_)
            elif hardness=="medium":
                with open(path_2, "w") as file:
                    file.write(score_made_)
            elif hardness=="hard":
                with open(path_3, "w") as file:
                    file.write(score_made_)
            else:
                print("Repair the code.")
                exit()
        elif high_score>score_made:
            print("You made a new high score!")
            print("Your Score : ",score_made)
            print("Last Score : ",high_score)
            score_made_ = str(score_made)
            if hardness=="easy":
                with open(path_1, "w") as file:
                    file.write(score_made_)
            elif hardness=="medium":
                with open(path_2, "w") as file:
                    file.write(score_made_)
            elif hardness=="hard":
                with open(path_3, "w") as file:
                    file.write(score_made_)
            else:
                print("Repair the code.")
                exit()
        elif high_score<score_made:
            print("Your score was lower than the last high score.")
            print("Your Score : ",score_made)
            print("Last Score : ",high_score)
        else:
            print("Repair the code.")
            exit()
        delay.two_second_delay()
        delay.one_second_delay()
        print(blank)
        exit_ = False
        while 1==1:
            print("Want to play again ? [Yes/No]")
            input_ = input("Type : ")
            input__ = input_.lower()
            if input__.startswith('y'):
                print(blank)
                exit_ = False
                break
            elif input__.startswith('n'):
                print(blank)
                print("Thanks for playing!")
                delay.one_second_delay()
                exit_ = True
                break
            elif input__=="exit":
                exit()
            else:
                print(blank)
                print("Try again.")
                delay.one_second_delay()
                print(blank)
        if exit_==False:
            continue
        else:
            break
game()