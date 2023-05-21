# Stone Paper Scissor
from random import randint
blank = """














































"""
print("An small game of stone paper and scissors")
print("It has three formats :-\nSnake Water Gun (SWG)\nStone Paper Scissors (SPS)\nBomb Building Gun (BBG)")
while 1==1:
    format_ = input("Which format you will choose (---) : ")
    if format_.lower()=='swg':
        game_format = 'SWG'
        break
    elif format_.lower()=='sps':
        game_format = 'SPS'
        break
    elif format_.lower()=='bbg':
        game_format = 'BBG'
        break
    else:
        print("Try Again")
        print(blank)
_format_ = game_format
def computer_player(game_format):
    chance = randint(1, 3)
    if game_format=='BBG':
        if chance==1:
            return 'bb'
        elif chance==2:
            return 'bg'
        elif chance==3:
            return 'gn'
        else:
            print("Repair Code")
            exit()
    elif game_format=='SWG':
        if chance==1:
            return 'sn'
        elif chance==2:
            return 'wr'
        elif chance==3:
            return 'gu'
        else:
            print("Repair Code")
            exit()
    elif game_format=='SPS':
        if chance==1:
            return 'se'
        elif chance==2:
            return 'pp'
        elif chance==3:
            return 'ss'
        else:
            print("Repair Code")
            exit()
    else:
        print("Repair Code")
        exit()
def winner_decider(P, C, game_format):
    if game_format=='SWG':
        if P=='sn' and C=='sn':
            return None
        elif P=='sn' and C=='wr':
            return True
        elif P=='sn' and C=='gu':
            return False
        elif P=='wr' and C=='wr':
            return None
        elif P=='wr' and C=='sn':
            return False
        elif P=='wr' and C=='gu':
            return True
        elif P=='gu' and C=='sn':
            return True
        elif P=='gu' and C=='wr':
            return False
        elif P=='gu' and C=='gu':
            return None
        else:
            print('Repair Code')
    elif game_format=="BBG":
        if P=='bb' and C=='bb':
            return None
        elif P=='bb' and C=='bg':
            return True
        elif P=='bb' and C=='gn':
            return False
        elif P=='bg' and C=='bb':
            return False
        elif P=='bg' and C=='bg':
            return None
        elif P=='bg' and C=='gn':
            return True
        elif P=='gn' and C=='bb':
            return True
        elif P=='gn' and C=='bg':
            return False
        elif P=='gn' and C=='gn':
            return None
        else:
            print('Repair Code')
    elif game_format=="SPS":
        if P=='ss' and C=='ss':
            return None
        elif P=='ss' and C=='pp':
            return True
        elif P=='ss' and C=='se':
            return False
        elif P=='pp' and C=='ss':
            return False
        elif P=='pp' and C=='pp':
            return None
        elif P=='pp' and C=='se':
            return True
        elif P=='se' and C=='ss':
            return True
        elif P=='se' and C=='pp':
            return False
        elif P=='se' and C=='se':
            return None
        else:
            print('Repair Code')
    else:
        print('Repair Code')
def game(game_format):
    number = int(input("Enter how many times you want to play : "))
    print(blank)
    P_score = 0
    C_score = 0
    P_streak = 0
    C_streak = 0
    P_high_streak = 0
    C_high_streak = 0
    for playing in range(0, number):
        print(f'''
Player's Score    : {P_score}
Player's Streak   : {P_streak}
Highest Streak    : {P_high_streak}
Computer's Score  : {C_score}
Computer's Streak : {C_streak}
Highest Streak    : {C_high_streak}
Total Matches     : {playing}
''')
        while 1==1:
            print("Computer's chance : <Chosen>")
            if game_format=='SWG':
                P_move = input("Your chance (sn, wr, gu) : ")
                if P_move=='sn' or P_move=='wr' or P_move=='gu':
                    break
                else:
                    print("Try again.")
                    print(blank)
                    continue
            elif game_format=='BBG':
                P_move = input("Your chanec (bb, bg, gn) : ")
                if P_move=='bb' or P_move=='bg' or P_move=='gn':
                    break
                else:
                    print("Try again.")
                    print(blank)
                    continue
            else:
                P_move = input("Your chance (se, pp, ss) : ")
                if P_move=='se' or P_move=='pp' or P_move=='ss':
                    break
                else:
                    print("Try again.")
                    print(blank)
                    continue
        C_move = computer_player(_format_)
        player_winner = winner_decider(P_move, C_move, _format_)
        print(blank)
        if player_winner==True:
            P_score = P_score+1
            P_streak = P_streak+1
            C_streak = 0
            if P_streak>P_high_streak:
                P_high_streak = P_streak
            else:
                P_high_streak = P_high_streak
            print("You Win :)")
            print(f"You chose : {P_move}")
            print(f"Computer chose : {C_move}")
            input("Press ENTER to continue...")
        elif player_winner==False:
            C_score = C_score+1
            C_streak = C_streak+1
            P_streak = 0
            if C_streak>C_high_streak:
                C_high_streak = C_streak
            else:
                C_high_streak = C_high_streak
            print("You Lose :(")
            print(f"You chose : {P_move}")
            print(f"Computer chose : {C_move}")
            input("Press ENTER to continue...")
        elif player_winner==None:
            print("Tie :|")
            print(f"You chose : {P_move}")
            print(f"Computer chose : {C_move}")
            print("Press ENTER to continue...")
        else:
            print("Repair Code")
        print(blank)
    print(blank)
    print(f'''Player's Score    : {P_score}
Player's Streak   : {P_streak}
Highest Streak    : {P_high_streak}
Computer's Score  : {C_score}
Computer's Streak : {C_streak}
Highest Streak    : {C_high_streak}
Total Matches     : {playing+1}''')
    print("You have completed your game. Hope you enjoyed.")
game(_format_)