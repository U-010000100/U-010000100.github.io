# OX (Version 3)
import random
import datetime
class game():
    """Main Class Containing All The Functions And Values."""
    decided_game_mode = ""
    AI_assistance = None
    Rules_assistance_1 = None
    Rules_assistance_2 = None
    Chance_of_2 = ""
    P1_score = 0
    P1_streak = 0
    P1_high_streak = 0
    P2_score = 0
    P2_streak = 0
    P2_high_streak = 0
    Total_2_player_matches = 0
    Chance_of_1 = ""
    P_score = 0
    P_streak = 0
    P_high_streak = 0
    C_score = 0
    C_streak = 0
    C_high_streak = 0
    Total_1_player_matches = 0
    P1_name = ""
    P2_name = ""
    Player_name = ""
    Computer_name = ""
    game_mode = ""
    P = ""
    C = ""
    P1 = ""
    P2 = ""
    Winner_1 = None
    Winner_2 = None
    block1 = "1"
    block2 = "2"
    block3 = "3"
    block4 = "4"
    block5 = "5"
    block6 = "6"
    block7 = "7"
    block8 = "8"
    block9 = "9"
    chance = 1
    blank = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'''
    def Symbol_assigner(help_: bool):
        '''Assigns Symbols To Players Or Player And Computer.'''
        g = game
        assistance = help_
        P_symbol = g.P
        C_symbol = g.C
        P1_symbol = g.P1
        P2_symbol = g.P2
        if g.game_mode=="1-Player":
            if P_symbol!="" and C_symbol!="":
                if assistance==True:
                    print("Symbols were used before.")
                    g.one_second_delay()
                else: pass
                print(f"Player   : {g.P}")
                print(F"Computer : {g.C}")
                g.one_second_delay()
                print("Use these sumbols ?")
                ask_symbol = input("[Yes/No] : ")
                asksymbol = ask_symbol.lower()
                if asksymbol=="exit" or asksymbol=="q":
                    g.game_closer()
                else: pass
                y_s = asksymbol.find("y")
                if y_s!=-1: y_s = True
                else: y_s = False
                if y_s==True: pass
                else:
                    print(g.blank)
                    if assistance==True:
                        print("Interchanging symbols.")
                        g.one_second_delay()
                    else: pass
                    if g.P=="O": g.P = "X"; g.C = "O"
                    else: g.P = "O"; g.C = "X"
                    print(f'''You will use "{g.P}" on your chance and computer will use "{g.C}"''')
                    g.one_second_delay()
                    g.one_second_delay()
            else:
                if assistance==True:
                    print("How you want to assign the symbols ?")
                    g.one_second_delay()
                    print("By yourself [Method 1]")
                    g.one_second_delay()
                    print("Let the computer decide [Method 2]")
                    g.one_second_delay()
                    g.one_second_delay()
                else:
                    print("[Method 1] or [Method 2] (For assigning symbols.)")
                    g.one_second_delay()
                ask_1 = input("Method ")
                ask1 = ask_1.lower()
                if ask1=="exit" or ask1=="q": g.game_closer()
                else: pass
                confirmation_1 = ask1.find("1")
                confirmation_2 = ask1.find("f")
                if confirmation_1!=-1: by_self_1 = True
                else:
                    if confirmation_2!=-1: by_self_1 = True
                    else: by_self_1 = False
                if by_self_1==True:
                    while 1==1:
                        print(g.blank)
                        if assistance==True:    
                            print("You are choosing the symbol you want to use.")
                            g.one_second_delay()
                            print("Which symbol you will choose ?")
                            g.one_second_delay()
                        else:
                            print("Choose your symbol.")
                            g.one_second_delay()
                        ask_2 = input("[ O / X ] : ")
                        ask2 = ask_2.lower()
                        if ask2=="exit" or ask2=="q": g.game_closer()
                        else: pass
                        o = ask2.find('o')
                        x = ask2.find('x')
                        if o!=-1:
                            g.P = "O"
                            g.C = "X"
                            g.one_second_delay()
                            print(g.blank)
                            g.one_second_delay()
                            print(f'''You will use "{g.P}" on your chance and computer will use "{g.C}"''')
                            g.one_second_delay()
                            g.one_second_delay()
                            break
                        elif x!=-1:
                            g.P = "X"
                            g.C = "O"
                            g.one_second_delay()
                            print(g.blank)
                            g.one_second_delay()
                            print(f'''You will use "{g.P}" on your chance and computer will use "{g.C}"''')
                            g.one_second_delay()
                            g.one_second_delay()
                            break
                        else:
                            print("Type again.")
                            g.one_second_delay()
                            print(g.blank)
                else:
                    print(g.blank)
                    if assistance==True:
                        print("Computer is choosing the symbol for you.")
                        g.one_second_delay()
                    else: pass
                    symbol = random.randint(1, 2)
                    if symbol==1:
                        g.P = "O"
                        g.C = "X"
                        g.one_second_delay()
                        print(g.blank)
                        g.one_second_delay()
                        print(f'''You will use "{g.P}" on your chance and computer will use "{g.C}"''')
                        g.one_second_delay()
                        g.one_second_delay()
                    else:
                        g.P = "X"
                        g.C = "O"
                        g.one_second_delay()
                        print(g.blank)
                        g.one_second_delay()
                        print(f'''You will use "{g.P}" on your chance and computer will use "{g.C}"''')
                        g.one_second_delay()
                        g.one_second_delay()
        elif g.game_mode=="2-Player":
            if P1_symbol!="" and P2_symbol!="":
                if assistance==True:
                    print("Symbols were used before.")
                    g.one_second_delay()
                else: pass
                print(f"Player-1 : {g.P1}")
                print(f"Player-2 : {g.P2}")
                g.one_second_delay()
                print("Use these sumbols ?")
                ask_symbol = input("[Yes/No] : ")
                asksymbol = ask_symbol.lower()
                if asksymbol=="exit" or asksymbol=="q": g.game_closer()
                else: pass
                y_s = asksymbol.find("y")
                if y_s!=-1: y_s = True
                else: y_s = False
                if y_s==True: pass
                else:
                    print(g.blank)
                    if assistance==True:
                        print("Interchanging symbols.")
                        g.one_second_delay()
                    else: pass
                    if g.P1=="O": g.P1 = "X"; g.P2 = "O"
                    else: g.P1 = "O"; g.P2 = "X"
                    print(f'''{g.P1_name} will use "{g.P1}" on his/her chance and g.{g.P2_name} will use "{g.P2}"''')
                    g.one_second_delay()
                    g.one_second_delay()
            else:
                if assistance==True:
                    print("How you want to assign the symbols ?")
                    g.one_second_delay()
                    print("By yourself [Method 1]")
                    g.one_second_delay()
                    print("Let the computer decide [Method 2]")
                    g.one_second_delay()
                    g.one_second_delay()
                else:
                    print("[Method 1] or [Method 2] (For assigning symbols.)")
                    g.one_second_delay()
                ask_1 = input("Method ")
                ask1 = ask_1.lower()
                if ask1=="exit" or ask1=="q": g.game_closer()
                else: pass
                confirmation_1 = ask1.find("1")
                confirmation_2 = ask1.find("2")
                if confirmation_2!=-1: by_self = False
                elif confirmation_1!=1: by_self = True
                else: by_self = False
                if by_self==True:
                    while 1==1:
                        print(g.blank)
                        if assistance==True:
                            print("You are choosing the symbol you want to use.")
                            g.one_second_delay()
                            print(f"Which symbol you will choose for {g.P1_name} ?")
                            g.one_second_delay()
                        else:
                            print(f"Choose symbol for {g.P1_name}.")
                            g.one_second_delay()
                        ask_2 = input("[ O / X ] : ")
                        ask2 = ask_2.lower()
                        if ask2=="exit" or ask2=="q": g.game_closer()
                        else: pass
                        o = ask2.find('o')
                        x = ask2.find('x')
                        if o!=-1:
                            g.P1 = "O"
                            g.P2 = "X"
                            g.one_second_delay()
                            print(g.blank)
                            g.one_second_delay()
                            print(f'''{g.P1_name} will use "{g.P1}" on his/her chance and {g.P2_name} will use "{g.P2}"''')
                            g.one_second_delay()
                            g.one_second_delay()
                            break
                        elif x!=-1:
                            g.P1 = "X"
                            g.P2 = "O"
                            g.one_second_delay()
                            print(g.blank)
                            g.one_second_delay()
                            print(f'''{g.P1_name} will use "{g.P1}" on his/her chance and {g.P2_name} will use "{g.P2}"''')
                            g.one_second_delay()
                            g.one_second_delay()
                            break
                        else:
                            print("Type again.")
                            g.one_second_delay()
                            print(g.blank)
                else:
                    print(g.blank)
                    if assistance==True:
                        print("Computer is choosing the symbol for Players.")
                        g.one_second_delay()
                    else: pass
                    symbol = random.randint(1, 2)
                    if symbol==1:
                        g.P1 = "O"
                        g.P2 = "X"
                        g.one_second_delay()
                        print(g.blank)
                        g.one_second_delay()
                        print(f'''{g.P1_name} will use "{g.P1}" on his/her chance and {g.P2_name} will use "{g.P2}"''')
                        g.one_second_delay()
                        g.one_second_delay()
                    else:
                        g.P1 = "X"
                        g.P2 = "O"
                        g.one_second_delay()
                        print(g.blank)
                        g.one_second_delay()
                        print(f'''{g.P1_name} will use "{g.P1}" on his/her chance and {g.P2_name} will use "{g.P2}"''')
                        g.one_second_delay()
                        g.one_second_delay()
        print(g.blank)
    def game_winner_decider():
        '''Decides The Winner Of The Game.'''
        g = game
        P = g.P
        C = g.C
        P1 = g.P1
        P2 = g.P2
        b1 = g.block1
        b2 = g.block2
        b3 = g.block3
        b4 = g.block4
        b5 = g.block5
        b6 = g.block6
        b7 = g.block7
        b8 = g.block8
        b9 = g.block9
        if g.game_mode=="1-Player":
            if b1==P and b2==P and b3==P:
                return "Player"
            elif b1==P and b4==P and b7==P:
                return "Player"
            elif b5==P and b1==P and b9==P:
                return "Player"
            elif b5==P and b3==P and b7==P:
                return "Player"
            elif b5==P and b2==P and b8==P:
                return "Player"
            elif b5==P and b4==P and b6==P:
                return "Player"
            elif b9==P and b6==P and b3==P:
                return "Player"
            elif b9==P and b8==P and b7==P:
                return "Player"
            elif b1==C and b2==C and b3==C:
                return "Computer"
            elif b1==C and b4==C and b7==C:
                return "Computer"
            elif b5==C and b1==C and b9==C:
                return "Computer"
            elif b5==C and b3==C and b7==C:
                return "Computer"
            elif b5==C and b2==C and b8==C:
                return "Computer"
            elif b5==C and b4==C and b6==C:
                return "Computer"
            elif b9==C and b6==C and b3==C:
                return "Computer"
            elif b9==C and b8==C and b7==C:
                return "Computer"
            else:
                return None
        elif g.game_mode=="2-Player":
            if b1==P1 and b2==P1 and b3==P1:
                return "Player-1"
            elif b1==P1 and b4==P1 and b7==P1:
                return "Player-1"
            elif b5==P1 and b1==P1 and b9==P1:
                return "Player-1"
            elif b5==P1 and b3==P1 and b7==P1:
                return "Player-1"
            elif b5==P1 and b2==P1 and b8==P1:
                return "Player-1"
            elif b5==P1 and b4==P1 and b6==P1:
                return "Player-1"
            elif b9==P1 and b6==P1 and b3==P1:
                return "Player-1"
            elif b9==P1 and b8==P1 and b7==P1:
                return "Player-1"
            elif b1==P2 and b2==P2 and b3==P2:
                return "Player-2"
            elif b1==P2 and b4==P2 and b7==P2:
                return "Player-2"
            elif b5==P2 and b1==P2 and b9==P2:
                return "Player-2"
            elif b5==P2 and b3==P2 and b7==P2:
                return "Player-2"
            elif b5==P2 and b2==P2 and b8==P2:
                return "Player-2"
            elif b5==P2 and b4==P2 and b6==P2:
                return "Player-2"
            elif b9==P2 and b6==P2 and b3==P2:
                return "Player-2"
            elif b9==P2 and b8==P2 and b7==P2:
                return "Player-2"
            else:
                return None
    def sheet_printer():
        '''Displays The Game Sheet With Statistics.'''
        g = game
        b1 = g.block1
        b2 = g.block2
        b3 = g.block3
        b4 = g.block4
        b5 = g.block5
        b6 = g.block6
        b7 = g.block7
        b8 = g.block8
        b9 = g.block9
        mode = g.game_mode
        if mode=="1-Player":
            sheet = f'''
    ┌───┬───┬───┐        Player's Score    : {g.P_score}
    │ {b1} │ {b2} │ {b3} │        Player's Streak   : {g.P_streak}
    ├───┼───┼───┤        Highest Streak    : {g.P1_high_streak}
    │ {b4} │ {b5} │ {b6} │        Computer's Score  : {g.C_score}
    ├───┼───┼───┤        Computer's Streak : {g.C_streak}
    │ {b7} │ {b8} │ {b9} │        Highest Streak    : {g.C_high_streak}
    └───┴───┴───┘        Total Matches     : {g.Total_1_player_matches}
    '''
        elif mode=="2-Player":
            sheet = f'''
    ┌───┬───┬───┐        Player-1 Score    : {g.P1_score}
    │ {b1} │ {b2} │ {b3} │        Player-1 Streak   : {g.P1_streak}
    ├───┼───┼───┤        Highest Streak    : {g.P1_high_streak}
    │ {b4} │ {b5} │ {b6} │        Player-2 Score    : {g.P2_score}
    ├───┼───┼───┤        Player-2 Streak   : {g.P2_streak}
    │ {b7} │ {b8} │ {b9} │        Highest Streak    : {g.P2_high_streak}
    └───┴───┴───┘        Total Matches     : {g.Total_2_player_matches}
    '''
        print(sheet)
    def Computer_player_game():
        '''1-Player Game Starter.'''
        g = game
        assistance = None
        if g.AI_assistance==None:
            print("Hi, I am your assistant for this game.")
            g.one_second_delay()
            print("I will guide you for first time,")
            g.one_second_delay()
            print("After that, it will be your choice to get assistance :)")
            g.one_second_delay()
            g.AI_assistance = False
            assistance = True
        else:
            ask_1 = input("Need assistance ? [Y/n] : ")
            ask1 = ask_1.lower()
            if ask1=="exit" or ask1=="q": g.game_closer()
            else: pass
            y = ask1.find("y")
            n = ask1.find("n")
            if y!=-1: y = True
            else: y = False
            if n!=-1: n = True
            else: n = False
            if y==True and n==False: assistance = True; g.AI_assistance = False
            elif y==False and n==True: assistance = False; g.AI_assistance = False
            elif y==False and n==False: assistance = False; g.AI_assistance = False
            elif y==True and n==True:
                if y<n: assistance = True; g.AI_assistance = False
                else: assistance = False; g.AI_assistance = False
        g.one_second_delay()
        print(g.blank)
        if assistance==True:
            print("Assign your name and name for computer.")
            g.one_second_delay()
            print("Name should be in limit of 3 to 20 characters.")
            g.one_second_delay()
            print("No special character is allowed (like '@', '#' etc.)")
            g.one_second_delay()
        else: pass
        g.one_second_delay()
        g.name_assigner(assistance)
        g.Symbol_assigner(assistance)
        print(g.blank)
        first_chance = g.chance_assigner(assistance)
        print(g.blank)
        g.Rules_printer()
        g.GAME(first_chance)
    def name_error_finder(name: str):
        '''Verifies The Name For Players In Limits.'''
        error = False
        name = str(name)
        allowed_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ','.']
        limit_1 = len(name)
        limit_2 = len(allowed_characters)
        if limit_1<3: error = True
        else:
            if limit_1>20: error = True
            else:
                for loop_1 in range(limit_1):
                    to_check_character = name[loop_1]
                    for loop_2 in range(limit_2):
                        if allowed_characters[loop_2]==to_check_character: error = False; break
                        else:
                            if loop_2==63: error = True; break
                            else: continue
                    if error==True: error = True; break
                    else:
                        if loop_1==limit_1-1: error = False
                        else: continue
        if error==True: return "True"
        else: return "False"
    def Human_player_game():
        '''2-Player Game Starter.'''
        g = game
        assistance = None
        if g.AI_assistance==None:
            print("Hi, I am your assistant for this game.")
            g.one_second_delay()
            print("I will guide you for first time,")
            g.one_second_delay()
            print("After that, it will be your choice to get assistance :)")
            g.one_second_delay()
            g.AI_assistance = False
            assistance = True
        else:
            ask_1 = input("Need assistance ? [Y/n] : ")
            ask1 = ask_1.lower()
            if ask1=="exit" or ask1=="q": g.game_closer()
            else: pass
            y = ask1.find("y")
            n = ask1.find("n")
            if y!=-1: y = True
            else: y = False
            if n!=-1: n = True
            else: n = False
            if y==True and n==False: assistance = True; g.AI_assistance = False
            elif y==False and n==True: assistance = False; g.AI_assistance = False
            elif y==False and n==False: assistance = False; g.AI_assistance = False
            elif y==True and n==True:
                if y<n: assistance = True; g.AI_assistance = False
                else: assistance = False; g.AI_assistance = False
        g.one_second_delay()
        print(g.blank)
        if assistance==True:
            print("First, tell me the names of players")
            g.one_second_delay()
            print("Name should be in limit of 3 to 20 characters.")
            g.one_second_delay()
            print("No special character is allowed (like '@', '#' etc.)")
            g.one_second_delay()
        else: pass
        g.one_second_delay()
        g.name_assigner(assistance)
        g.Symbol_assigner(assistance)
        print(g.blank)
        first_chance = g.chance_assigner(assistance)
        print(g.blank)
        g.Rules_printer()
        g.GAME(first_chance)
    def Rules_printer():
        '''Displays The Rules Of The Game.'''
        g = game
        mode = g.game_mode
        if mode=="1-Player":
            assistance = g.Rules_assistance_1
            if assistance==None:
                g.Rules_assistance_2 = False
                print("Read the rules :-")
                g.one_second_delay()
                print("The empty block contains number inside it.")
                g.one_second_delay()
                print("You can type the number of block to put your sumbols in it.")
                g.one_second_delay()
                print("You can't type the number of the block used before.")
                g.one_second_delay()
                print("Doing so can cause winning of Computer")
                g.one_second_delay()
                input("Hope you understand, Press ENTER[RETURN]... ")
                print(g.blank)
            else:
                print("Do you want to read the rules ?")
                ask_1 = input("[Yes/No] : ")
                ask1 = ask_1.lower()
                if ask1=="exit" or ask1=="q": g.game_closer()
                else: pass
                y1 = ask1.find('y')
                if y1!=-1: y1 = True
                else: y1 = False
                if y1==True:
                    print(g.blank)
                    print("Rules :-")
                    g.one_second_delay()
                    print("The empty block contains number inside it.")
                    g.one_second_delay()
                    print("You can type the number of block to put your sumbols in it.")
                    g.one_second_delay()
                    print("You can't type the number of the block used before.")
                    g.one_second_delay()
                    print("Doing so can cause winning of Computer.")
                    g.one_second_delay()
                    input("Hope you understand, Press ENTER[RETURN]... ")
                    print(g.blank)
                else: print(g.blank)
        elif mode=="2-Player":
            assistance = g.Rules_assistance_2
            if assistance==None:
                g.Rules_assistance_2 = False
                print("Read the rules :-")
                g.one_second_delay()
                print("The empty block contains number inside it.")
                g.one_second_delay()
                print("Players can type the number of block to put their sumbols in it.")
                g.one_second_delay()
                print("You can't type the number of the block used before.")
                g.one_second_delay()
                print("Doing so can cause winning of another player.")
                g.one_second_delay()
                input("Hope you understand, Press ENTER[RETURN]... ")
                print(g.blank)
            else:
                print("Do you want to read the rules ?")
                ask_1 = input("[Yes/No] : ")
                ask1 = ask_1.lower()
                if ask1=="exit" or ask1=="q": g.game_closer()
                else: pass
                y1 = ask1.find('y')
                if y1!=-1: y1 = True
                else: y1 = False
                if y1==True:
                    print(g.blank)
                    print("Rules :-")
                    g.one_second_delay()
                    print("The empty block contains number inside it.")
                    g.one_second_delay()
                    print("Players can type the number of block to put their sumbols in it.")
                    g.one_second_delay()
                    print("You can't type the number of the block used before.")
                    g.one_second_delay()
                    print("Doing so can cause winning of another player.")
                    g.one_second_delay()
                    input("Hope you understand, Press ENTER[RETURN]... ")
                    print(g.blank)
                else: print(g.blank)
    def statistics_handler(winner: str):
        '''Handles The Statistics.'''
        g = game
        mode = g.game_mode
        if mode=="1-Player":
            g.Total_1_player_matches = g.Total_1_player_matches+1
            if winner=="Player":
                g.P_score = g.P_score+1
                g.P_streak = g.P_streak+1
                g.C_streak = 0
                if g.P_streak>g.P_high_streak: g.P_high_streak = g.P_streak
                else: g.P_high_streak = g.P_high_streak
            elif winner=="Computer":
                g.C_score = g.C_score+1
                g.C_streak = g.C_streak+1
                g.P_streak = 0
                if g.C_streak>g.C_high_streak: g.C_high_streak = g.C_streak
                else: g.C_high_streak = g.C_high_streak
            else: pass
        elif mode=="2-Player":
            g.Total_2_player_matches = g.Total_2_player_matches+1
            if winner=="Player-1":
                g.P1_score = g.P1_score+1
                g.P1_streak = g.P1_streak+1
                g.P2_streak = 0
                if g.P1_streak>g.P1_high_streak: g.P1_high_streak = g.P1_streak
                else: g.P1_high_streak = g.P1_high_streak
            elif winner=="Player-2":
                g.P2_score = g.P2_score+1
                g.P2_streak = g.P2_streak+1
                g.P1_streak = 0
                if g.P2_streak>g.P2_high_streak: g.P2_high_streak = g.P2_streak
                else: g.P2_high_streak = g.P2_high_streak
            else: pass
    def symbol_printer(temp: str, symbol: str):
        '''Puts The Symbol Of The Players In Their Requested Blocks.'''
        g = game
        temp = int(temp)
        if temp==1: g.block1 = symbol
        elif temp==2: g.block2 = symbol
        elif temp==3: g.block3 = symbol
        elif temp==4: g.block4 = symbol
        elif temp==5: g.block5 = symbol
        elif temp==6: g.block6 = symbol
        elif temp==7: g.block7 = symbol
        elif temp==8: g.block8 = symbol
        elif temp==9: g.block9 = symbol
        else: pass
    def GAME(first_chance: str):
        '''The Actual Game.'''
        g = game
        chance = 0
        mode = g.game_mode
        if mode=="1-Player":
            g.Chance_of_1 = first_chance
            Player_mistake = 0
            winner = None
            loop = 1
            while loop==loop:
                if chance==10: print(chance)
                else:
                    if g.Chance_of_1=="Player":
                        g.Chance_of_1 = "Computer"
                        while 1==1:
                            print(g.blank)
                            g.sheet_printer()
                            temp = input(f"{g.Player_name}'s Chance (Type the number of block) : ")
                            if temp=="exit" or temp=="q": g.game_closer()
                            else: pass
                            g.one_second_delay()
                            error = g.temp_error_finder(temp)
                            if error!=0:
                                if Player_mistake<3:
                                    Player_mistake += 1
                                    print(g.blank)
                                    print(f"{g.Player_name} has performed a mistake.")
                                    print("He/She is warned to not perform that mistake again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                else:
                                    print(f"{g.Player_name} has performed mistakes more than 3 times.")
                                    print(f"{g.Computer_name} wins")
                                    winner = "Computer"
                                    break
                            else:
                                g.symbol_printer(temp, g.P)
                                g.one_second_delay()
                                g.chance = g.chance+1
                                break
                    elif g.Chance_of_1=="Computer":
                        g.Chance_of_1 = "Player"
                        print(g.blank)
                        g.sheet_printer()
                        print(f"{g.Computer_name}'s chance...")
                        g.one_second_delay()
                        g.one_second_delay()
                        g.computer_AI(g.P, g.C)
                        g.chance = g.chance+1
                    if winner!=None:
                        if winner=="Player":
                            print(g.blank)
                            g.block1 = g.P
                            g.block2 = g.P
                            g.block3 = g.P
                            g.block4 = g.P
                            g.block5 = g.P
                            g.block6 = g.P
                            g.block7 = g.P
                            g.block8 = g.P
                            g.block9 = g.P
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.Player_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.Player_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=='q': g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        elif winner=="Computer":
                            print(g.blank)
                            g.block1 = g.C
                            g.block2 = g.C
                            g.block3 = g.C
                            g.block4 = g.C
                            g.block5 = g.C
                            g.block6 = g.C
                            g.block7 = g.C
                            g.block8 = g.C
                            g.block9 = g.C
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.Computer_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.Computer_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        else: pass
                    else:
                        winner = g.game_winner_decider()
                        if winner=="Player":
                            print(g.blank)
                            g.winner_block_reseter(winner)
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.Player_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.Player_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else:pass
                        elif winner=="Computer":
                            print(g.blank)
                            g.winner_block_reseter(winner)
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.Computer_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.Computer_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        else:
                            if g.block1!="1":
                                if g.block2!="2":
                                    if g.block3!="3":
                                        if g.block4!="4":
                                            if g.block5!="5":
                                                if g.block6!="6":
                                                    if g.block7!="7":
                                                        if g.block8!="8":
                                                            if g.block9!="9":
                                                                g.Total_1_player_matches = g.Total_1_player_matches+1
                                                                print(g.blank)
                                                                g.sheet_printer()
                                                                print("This game is tie.")
                                                                g.one_second_delay()
                                                                g.one_second_delay()
                                                                g.one_second_delay()
                                                                while 1==1:
                                                                    print(g.blank)
                                                                    ask_1 = input("Play again ? [Yes/No] : ")
                                                                    g.one_second_delay()
                                                                    ask1 = ask_1.lower()
                                                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                                                    else: pass
                                                                    y1 = ask1.find("y")
                                                                    n1 = ask1.find("n")
                                                                    if y1!=-1: loop_play = True; break
                                                                    elif n1!=-1:
                                                                        loop_play = False
                                                                        ask2 = input("Exit ? [Y/N] : ")
                                                                        ask2.lower()
                                                                        if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                                                        else: pass
                                                                        break
                                                                    else: print("Type again."); g.one_second_delay()
                                                                if loop_play==True: g.reset_1(); continue
                                                                elif loop_play==False: g.reset_2(); break
                                                                else: pass
                                                            else: pass
                                                        else: pass
                                                    else: pass
                                                else: pass
                                            else: pass
                                        else: pass
                                    else: pass
                                else: pass
                            else: pass
        elif mode=="2-Player":
            g.Chance_of_2 = first_chance
            Player_1_mistake = 0
            Player_2_mistake = 0
            winner = None
            loop = 1
            while loop==loop:
                if chance==9: print("chance")
                else:
                    if g.Chance_of_2=="Player-1":
                        g.Chance_of_2 = "Player-2"
                        while 1==1:
                            print(g.blank)
                            g.sheet_printer()
                            temp = input(f"{g.P1_name}'s Chance (Type the number of block) : ")
                            g.one_second_delay()
                            error = g.temp_error_finder(temp)
                            if error!=0:
                                if Player_1_mistake<3:
                                    Player_1_mistake += 1
                                    print(g.blank)
                                    print(f"{g.P1_name} has performed a mistake.")
                                    print("He/She is warned to not perform that mistake again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                else:
                                    print(f"{g.P1_name} has performed mistakes more than 3 times.")
                                    print(f"{g.P2_name} wins")
                                    winner = "Player-2"
                                    break
                            else:
                                g.symbol_printer(temp, g.P1)
                                g.one_second_delay()
                                break
                    elif g.Chance_of_2=="Player-2":
                        g.Chance_of_2 = "Player-1"
                        while 1==1:
                            print(g.blank)
                            g.sheet_printer()
                            temp = input(f"{g.P2_name}'s Chance (Type the number of block) : ")
                            if temp=="exit" or temp=="q": g.game_closer()
                            else: pass
                            g.one_second_delay()
                            error = g.temp_error_finder(temp)
                            if error!=0:
                                if Player_2_mistake<3:
                                    Player_2_mistake += 1
                                    print(g.blank)
                                    print(f"{g.P2_name} has performed a mistake.")
                                    print("He/She is warned to not perform that mistake again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                else:
                                    print(f"{g.P2_name} has performed mistakes more than 3 times.")
                                    print(f"{g.P1_name} wins")
                                    winner = "Player-2"
                                    break
                            else:
                                g.symbol_printer(temp, g.P2)
                                g.one_second_delay()
                                break
                    if winner!=None:
                        if winner=="Player-1":
                            print(g.blank)
                            g.block1 = g.P1
                            g.block2 = g.P1
                            g.block3 = g.P1
                            g.block4 = g.P1
                            g.block5 = g.P1
                            g.block6 = g.P1
                            g.block7 = g.P1
                            g.block8 = g.P1
                            g.block9 = g.P1
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.P1_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.P1_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=='q' or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        elif winner=="Player-2":
                            print(g.blank)
                            g.block1 = g.P2
                            g.block2 = g.P2
                            g.block3 = g.P2
                            g.block4 = g.P2
                            g.block5 = g.P2
                            g.block6 = g.P2
                            g.block7 = g.P2
                            g.block8 = g.P2
                            g.block9 = g.P2
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.P1_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.P1_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2; break
                            else: pass
                        else: pass
                    else:
                        winner = g.game_winner_decider()
                        if winner=="Player-1":
                            print(g.blank)
                            g.winner_block_reseter(winner)
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.P1_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.P1_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        elif winner=="Player-2":
                            print(g.blank)
                            g.winner_block_reseter(winner)
                            g.statistics_handler(winner)
                            g.sheet_printer()
                            print(f"{g.P2_name} has won this match.")
                            g.one_second_delay()
                            print(f"Congratulations {g.P2_name} !")
                            g.one_second_delay()
                            g.one_second_delay()
                            g.one_second_delay()
                            winner = None
                            while 1==1:
                                print(g.blank)
                                ask_1 = input("Play again ? [Yes/No] : ")
                                g.one_second_delay()
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find("y")
                                n1 = ask1.find("n")
                                if y1!=-1: loop_play = True; break
                                elif n1!=-1:
                                    loop_play = False
                                    ask2 = input("Exit ? [Y/N] : ")
                                    ask2.lower()
                                    if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                    else: pass
                                    break
                                else: print("Type again."); g.one_second_delay()
                            if loop_play==True: g.reset_1(); continue
                            elif loop_play==False: g.reset_2(); break
                            else: pass
                        else:
                            if g.block1!="1":
                                if g.block2!="2":
                                    if g.block3!="3":
                                        if g.block4!="4":
                                            if g.block5!="5":
                                                if g.block6!="6":
                                                    if g.block7!="7":
                                                        if g.block8!="8":
                                                            if g.block9!="9":
                                                                g.Total_2_player_matches = g.Total_2_player_matches+1
                                                                print(g.blank)
                                                                g.sheet_printer()
                                                                print("This game is tie.")
                                                                g.one_second_delay()
                                                                g.one_second_delay()
                                                                g.one_second_delay()
                                                                while 1==1:
                                                                    print(g.blank)
                                                                    ask_1 = input("Play again ? [Yes/No] : ")
                                                                    g.one_second_delay()
                                                                    ask1 = ask_1.lower()
                                                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                                                    else: pass
                                                                    y1 = ask1.find("y")
                                                                    n1 = ask1.find("n")
                                                                    if y1!=-1: loop_play = True; break
                                                                    elif n1!=-1:
                                                                        loop_play = False
                                                                        ask2 = input("Exit ? [Y/N] : ")
                                                                        ask2.lower()
                                                                        if ask2=="exit" or ask2=="q" or ask2.find('y')>=0: g.game_closer()
                                                                        else: pass
                                                                        break
                                                                    else: print("Type again."); g.one_second_delay()
                                                                if loop_play==True: g.reset_1(); continue
                                                                elif loop_play==False: g.reset_2(); break
                                                                else: pass
                                                            else: pass
                                                        else: pass
                                                    else: pass
                                                else: pass
                                            else: pass
                                        else: pass
                                    else: pass
                                else: pass
                            else: pass
    def computer_AI(P, C):
        '''A.I. Player.'''
        g = game
        chance = g.chance
        b1 = g.block1
        b2 = g.block2
        b3 = g.block3
        b4 = g.block4
        b5 = g.block5
        b6 = g.block6
        b7 = g.block7
        b8 = g.block8
        b9 = g.block9
        if b1=="1": b_1 = None
        elif b1=="O" and P=="O": b_1 = True
        elif b1=="X" and P=="X": b_1 = True
        elif b1=="O" and C=="O": b_1 = False
        elif b1=="X" and C=="X": b_1 = False
        else: b_1 = None
        if b2=="2": b_2 = None
        elif b2=="O" and P=="O": b_2 = True
        elif b2=="X" and P=="X": b_2 = True
        elif b2=="O" and C=="O": b_2 = False
        elif b2=="X" and C=="X": b_2 = False
        else: b_2 = None
        if b3=="3": b_3 = None
        elif b3=="O" and P=="O": b_3 = True
        elif b3=="X" and P=="X": b_3 = True
        elif b3=="O" and C=="O": b_3 = False
        elif b3=="X" and C=="X": b_3 = False
        else: b_3 = None
        if b4=="4": b_4 = None
        elif b4=="O" and P=="O": b_4 = True
        elif b4=="X" and P=="X": b_4 = True
        elif b4=="O" and C=="O": b_4 = False
        elif b4=="X" and C=="X": b_4 = False
        else: b_4 = None
        if b5=="5": b_5 = None
        elif b5=="O" and P=="O": b_5 = True
        elif b5=="X" and P=="X": b_5 = True
        elif b5=="O" and C=="O": b_5 = False
        elif b5=="X" and C=="X": b_5 = False
        else: b_5 = None
        if b6=="6": b_6 = None
        elif b6=="O" and P=="O": b_6 = True
        elif b6=="X" and P=="X": b_6 = True
        elif b6=="O" and C=="O": b_6 = False
        elif b6=="X" and C=="X": b_6 = False
        else: b_6 = None
        if b7=="7": b_7 = None
        elif b7=="O" and P=="O": b_7 = True
        elif b7=="X" and P=="X": b_7 = True
        elif b7=="O" and C=="O": b_7 = False
        elif b7=="X" and C=="X": b_7 = False
        else: b_7 = None
        if b8=="8": b_8 = None
        elif b8=="O" and P=="O": b_8 = True
        elif b8=="X" and P=="X": b_8 = True
        elif b8=="O" and C=="O": b_8 = False
        elif b8=="X" and C=="X": b_8 = False
        else: b_8 = None
        if b9=="9": b_9 = None
        elif b9=="O" and P=="O": b_9 = True
        elif b9=="X" and P=="X": b_9 = True
        elif b9=="O" and C=="O": b_9 = False
        elif b9=="X" and C=="X": b_9 = False
        else: b_9 = None
        if chance==1: g.block5 = C
        elif chance==2:
            if b_5==True:
                unknown_block = random.randint(1, 4)
                if unknown_block==1: u_b = 1
                elif unknown_block==2: u_b = 3
                elif unknown_block==3: u_b = 7
                elif unknown_block==4: u_b = 9
                if u_b==1: g.block1 = C
                elif u_b==3: g.block3 = C
                elif u_b==7: g.block7 = C
                elif u_b==9: g.block9 = C
            elif b_5==None: g.block5 = C
            else: pass
        elif chance==3:
            if b_1==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 3
                elif unknown_block==2: u_b = 7
                if u_b==3: g.block3 = C
                elif u_b==7: g.block7 = C
                else: pass
            elif b_2==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 1
                elif unknown_block==2: u_b = 3
                if u_b==1: g.block1 = C
                elif u_b==3: g.block3 = C
                else: pass
            elif b_3==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 1
                elif unknown_block==2: u_b = 9
                if u_b==1: g.block1 = C
                elif u_b==9: g.block9 = C
                else: pass
            elif b_4==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 1
                elif unknown_block==2: u_b = 7
                if u_b==1: g.block1 = C
                elif u_b==7: g.block7 = C
                else: pass
            elif b_6==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 3
                elif unknown_block==2: u_b = 9
                if u_b==3: g.block3 = C
                elif u_b==9: g.block9 = C
                else: pass
            elif b_7==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 1
                elif unknown_block==2: u_b = 9
                if u_b==1: g.block1 = C
                elif u_b==9: g.block9 = C
                else: pass
            elif b_8==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 7
                elif unknown_block==2: u_b = 9
                if u_b==7: g.block7 = C
                elif u_b==9: g.block9 = C
                else: pass
            elif b_9==True:
                unknown_block = random.randint(1, 2)
                if unknown_block==1: u_b = 3
                elif unknown_block==2: u_b = 7
                if u_b==3: g.block3 = C
                elif u_b==7: g.block7 = C
                else: pass
        elif chance==4:
            if b_5==True:
                if b_1==True and b_9==None: g.block9 = C
                elif b_9==True and b_1==None: g.block1 = C
                elif b_2==True and b_8==None: g.block8 = C
                elif b_8==True and b_2==None: g.block2 = C
                elif b_3==True and b_7==None: g.block7 = C
                elif b_7==True and b_3==None: g.block3 = C
                elif b_4==True and b_6==None: g.block6 = C
                elif b_6==True and b_4==None: g.block4 = C
                else:
                    if b_1==True and b_7==None and b_3==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 3
                        elif unknown_block==2: u_b = 7
                        if u_b==3: g.block3 = C
                        elif u_b==7: g.block7 = C
                        else: pass
                    elif b_3==True and b_1==None and b_9==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 1
                        elif unknown_block==2: u_b = 9
                        if u_b==1: g.block1 = C
                        elif u_b==9: g.block9 = C
                        else: pass
                    elif b_7==True and b_1==None and b_9==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 1
                        elif unknown_block==2: u_b = 9
                        if u_b==1: g.block1 = C
                        elif u_b==9: g.block9 = C
                        else: pass
                    elif b_9==True and b_3==None and b_7==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 3
                        elif unknown_block==7: u_b = 7
                        if u_b==3: g.block3 = C
                        elif u_b==7: g.block7 = C
                        else: pass
                    else: pass
            elif b_5==False:
                if b_1==True and b_3==True and b_2==None: g.block2 = C
                elif b_1==True and b_2==True and b_3==None: g.block3 = C
                elif b_2==True and b_3==True and b_1==None: g.block1 = C
                elif b_1==True and b_7==True and b_4==None: g.block4 = C
                elif b_1==True and b_4==True and b_7==None: g.block7 = C
                elif b_7==True and b_4==True and b_1==None: g.block1 = C
                elif b_7==True and b_9==True and b_8==None: g.block8 = C
                elif b_7==True and b_8==True and b_9==None: g.block9 = C
                elif b_9==True and b_8==True and b_7==None: g.block7 = C
                elif b_9==True and b_3==True and b_6==None: g.block6 = C
                elif b_9==True and b_6==True and b_3==None: g.block3 = C
                elif b_3==True and b_6==True and b_9==None: g.block9 = C
                else:
                    if b_7==None and b_3==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 3
                        elif unknown_block==2: u_b = 7
                        if u_b==3: g.block3 = C
                        elif u_b==7: g.block7 = C
                    elif b_1==None and b_9==None:
                        unknown_block = random.randint(1, 2)
                        if unknown_block==1: u_b = 1
                        elif unknown_block==2: u_b = 9
                        if u_b==1: g.block1 = C
                        elif u_b==9: g.block9 = C
                        else: pass
                    else:
                        if b_1==False and b_9==None: g.block9 = C
                        elif b_9==False and b_1==None: g.block1 = C
                        elif b_3==False and b_7==None: g.block7 = C
                        elif b_7==False and b_3==None: g.block3 = C
                        elif b_2==False and b_8==None: g.block8 = C
                        elif b_8==False and b_2==None: g.block2 = C
                        elif b_4==False and b_6==None: g.block6 = C
                        elif b_6==False and b_4==None: g.block4 = C
                        else:
                            if b_1==None: g.block1 = C
                            elif b_3==None: g.block3 = C
                            elif b_7==None: g.block7 = C
                            elif b_9==None: g.block9 = C
                            else:
                                if b_2==None: g.block2 = C
                                elif b_4==None: g.block4 = C
                                elif b_6==None: g.block6 = C
                                elif b_8==None: g.block8 = C
                                else: pass
        elif chance==5:
            if b_5==False:
                if b_1==False and b_9==None: g.block9 = C
                elif b_9==False and b_1==None: g.block1 = C
                elif b_3==False and b_7==None: g.block7 = C
                elif b_7==False and b_3==None: g.block3 = C
                else:
                    if b_2==True:
                        if b_1==False and b_9==True and b_7==None: g.block7 = C
                        elif b_3==False and b_7==True and b_9==None: g.block9 = C
                    elif b_4==True:
                        if b_1==False and b_9==True and b_3==None: g.block3 = C
                        elif b_7==False and b_3==True and b_9==None: g.block9 = C
                    elif b_6==True:
                        if b_3==False and b_7==True and b_1==None: g.block1 = C
                        elif b_9==False and b_1==True and b_7==None: g.block7 = C
                    elif b_8==True:
                        if b_7==False and b_3==True and b_1==None: g.block9 = C
                        elif b_9==False and b_1==True and b_3==None: g.block3 = C
                    else:
                        if b_1==True and b_7==True and b_4==None: g.block4 = C
                        elif b_1==True and b_3==True and b_2==None: g.block2 = C
                        elif b_9==True and b_7==True and b_8==None: g.block8 = C
                        elif b_9==True and b_3==True and b_6==None: g.block6 = C
                        else:
                            if b_1==False and b_9==None: g.block9 = C
                            elif b_9==False and b_1==None: g.block1 = C
                            elif b_3==False and b_7==None: g.block7 = C
                            elif b_7==False and b_3==None: g.block3 = C
                            elif b_2==False and b_8==None: g.block8 = C
                            elif b_8==False and b_2==None: g.block2 = C
                            elif b_4==False and b_6==None: g.block6 = C
                            elif b_6==False and b_4==None: g.block4 = C
                            else:
                                if b_1==None: g.block1 = C
                                elif b_3==None: g.block3 = C
                                elif b_7==None: g.block7 = C
                                elif b_9==None: g.block9 = C
                                else:
                                    if b_2==None: g.block2 = C
                                    elif b_4==None: g.block4 = C
                                    elif b_6==None: g.block6 = C
                                    elif b_8==None: g.block8 = C
                                    else: pass
            else:
                if b_1==False and b_3==False and b_2==None: g.block2 = C
                elif b_1==False and b_7==False and b_4==None: g.block4 = C
                elif b_9==False and b_7==False and b_8==None: g.block8 = C
                elif b_9==False and b_3==False and b_6==None: g.block6 = C
                else:
                    if b_1==True and b_5==True and b_9==None: g.block9 = C
                    elif b_9==True and b_5==True and b_1==None: g.block1 = C
                    elif b_3==True and b_5==True and b_7==None: g.block7 = C
                    elif b_7==True and b_5==True and b_3==None: g.block3 = C
                    elif b_2==True and b_5==True and b_8==None: g.block8 = C
                    elif b_8==True and b_5==True and b_2==None: g.block2 = C
                    elif b_4==True and b_5==True and b_6==None: g.block6 = C
                    elif b_6==True and b_5==True and b_4==None: g.block4 = C
                    else:
                        if b_1==None: g.block1 = C
                        elif b_3==None: g.block3 = C
                        elif b_7==None: g.block7 = C
                        elif b_9==None: g.block9 = C
                        else:
                            if b_2==None: g.block2 = C
                            elif b_4==None: g.block4 = C
                            elif b_6==None: g.block6 = C
                            elif b_8==None: g.block8 = C
                            else:  pass
        elif chance==6:
            if b_5==False:
                if b_1==False and b_9==None: g.block9 = C
                elif b_9==False and b_1==None: g.block1 = C
                elif b_3==False and b_7==None: g.block7 = C
                elif b_7==False and b_3==None: g.block3 = C
                elif b_2==False and b_8==None: g.block8 = C
                elif b_8==False and b_2==None: g.block2 = C
                elif b_4==False and b_6==None: g.block6 = C
                elif b_6==False and b_4==None: g.block4 = C
                else:
                    if b_1==True and b_3==True and b_2==None: g.block2 = C
                    elif b_1==True and b_2==True and b_3==None: g.block3 = C
                    elif b_2==True and b_3==True and b_1==None: g.block1 = C
                    elif b_1==True and b_7==True and b_4==None: g.block4 = C
                    elif b_1==True and b_4==True and b_7==None: g.block7 = C
                    elif b_7==True and b_4==True and b_1==None: g.block1 = C
                    elif b_7==True and b_9==True and b_8==None: g.block8 = C
                    elif b_7==True and b_8==True and b_9==None: g.block9 = C
                    elif b_9==True and b_8==True and b_7==None: g.block7 = C
                    elif b_9==True and b_3==True and b_6==None: g.block6 = C
                    elif b_9==True and b_6==True and b_3==None: g.block3 = C
                    elif b_3==True and b_6==True and b_9==None: g.block9 = C
                    else:
                        if b_1==None: g.block1 = C
                        elif b_3==None: g.block3 = C
                        elif b_7==None: g.block7 = C
                        elif b_9==None: g.block9 = C
                        else:
                            if b_2==None: g.block2 = C
                            elif b_4==None: g.block4 = C
                            elif b_6==None: g.block6 = C
                            elif b_8==None: g.block8 = C
                            else: pass
            elif b_5==True:
                if b_1==False and b_3==False and b_2==None: g.block2 = C
                elif b_1==False and b_7==False and b_4==None: g.block4 = C
                elif b_9==False and b_3==False and b_6==None: g.block6 = C
                elif b_9==False and b_7==False and b_8==None: g.block8 = C
                else:
                    if b_2==True and b_8==None: g.block8 = C
                    elif b_4==True and b_6==None: g.block6 = C
                    elif b_6==True and b_4==None: g.block4 = C
                    elif b_8==True and b_2==None: g.block2 = C
                    elif b_1==True and b_9==None: g.block9 = C
                    elif b_3==True and b_7==None: g.block7 = C
                    elif b_7==True and b_3==None: g.block7 = C
                    elif b_9==True and b_1==None: g.block1 = C
                    else:
                        if b_1==False:
                            if b_4==None and b_7==None: g.block7 = C
                            elif b_2==None and b_3==None: g.block3 = C
                            else: pass
                        elif b_9==False :
                            if b_6==None and b_3==None: g.block3 = C
                            elif b_8==None and b_7==None: g.block7 = C
                            else:
                                if b_1==True and b_9==None: g.block9 = C
                                elif b_9==True and b_1==None: g.block1 = C
                                elif b_3==True and b_7==None: g.block7 = C
                                elif b_7==True and b_3==None: g.block3 = C
                                elif b_2==True and b_8==None: g.block8 = C
                                elif b_8==True and b_2==None: g.block2 = C
                                elif b_4==True and b_6==None: g.block6 = C
                                elif b_6==True and b_4==None: g.block4 = C
                                else:
                                    if b_1==None: g.block1 = C
                                    elif b_3==None: g.block3 = C
                                    elif b_7==None: g.block7 = C
                                    elif b_9==None: g.block9 = C
                                    else:
                                        if b_2==None: g.block2 = C
                                        elif b_4==None: g.block4 = C
                                        elif b_6==None: g.block6 = C
                                        elif b_8==None: g.block8 = C
                                        else: pass
            else:
                if b_1==True and b_5==True and b_9==None: g.block9 = C
                elif b_9==True and b_5==True and b_1==None: g.block1 = C
                elif b_3==True and b_5==True and b_7==None: g.block7 = C
                elif b_7==True and b_5==True and b_3==None: g.block3 = C
                elif b_2==True and b_5==True and b_8==None: g.block8 = C
                elif b_8==True and b_5==True and b_2==None: g.block2 = C
                elif b_4==True and b_5==True and b_6==None: g.block6 = C
                elif b_6==True and b_5==True and b_4==None: g.block4 = C
                else:
                    if b_1==None: g.block1 = C
                    elif b_3==None: g.block3 = C
                    elif b_7==None: g.block7 = C
                    elif b_9==None: g.block9 = C
                    else:
                        if b_2==None: g.block2 = C
                        elif b_4==None: g.block4 = C
                        elif b_6==None: g.block6 = C
                        elif b_8==None: g.block8 = C
                        else: pass
        elif chance==7:
            if b_5==False:
                if b_1==False and b_9==None: g.block9 = C
                elif b_2==False and b_8==None: g.block8 = C
                elif b_3==False and b_7==None: g.block7 = C
                elif b_4==False and b_6==None: g.block6 = C
                elif b_6==False and b_4==None: g.block4 = C
                elif b_7==False and b_3==None: g.block3 = C
                elif b_8==False and b_2==None: g.block2 = C
                elif b_9==False and b_1==None: g.block1 = C
                else:
                    if b_1==False and b_2==False and b_3==None: g.block3 = C
                    elif b_1==False and b_3==False and b_2==None: g.block2 = C
                    elif b_2==False and b_3==False and b_1==None: g.block1 = C
                    elif b_1==False and b_4==False and b_7==None: g.block7 = C
                    elif b_1==False and b_7==False and b_4==None: g.block4 = C
                    elif b_4==False and b_7==False and b_1==None: g.block1 = C
                    elif b_9==False and b_8==False and b_7==None: g.block7 = C
                    elif b_9==False and b_7==False and b_8==None: g.block8 = C
                    elif b_7==False and b_8==False and b_9==None: g.block9 = C
                    elif b_9==False and b_6==False and b_3==None: g.block3 = C
                    elif b_9==False and b_3==False and b_6==None: g.block6 = C
                    elif b_3==False and b_6==False and b_9==None: g.block9 = C
                    else:
                        if b_1==True and b_2==True and b_3==None: g.block3 = C
                        elif b_1==True and b_3==True and b_2==None: g.block2 = C
                        elif b_2==True and b_3==True and b_1==None: g.block1 = C
                        elif b_1==True and b_4==True and b_7==None: g.block7 = C
                        elif b_1==True and b_7==True and b_4==None: g.block4 = C
                        elif b_4==True and b_7==True and b_1==None: g.block1 = C
                        elif b_9==True and b_8==True and b_7==None: g.block7 = C
                        elif b_9==True and b_7==True and b_8==None: g.block8 = C
                        elif b_7==True and b_8==True and b_9==None: g.block9 = C
                        elif b_9==True and b_6==True and b_3==None: g.block3 = C
                        elif b_9==True and b_3==True and b_6==None: g.block6 = C
                        elif b_3==True and b_6==True and b_9==None: g.block9 = C
                        else:
                            if b_1==None: g.block1 = C
                            elif b_3==None: g.block3 = C
                            elif b_7==None: g.block7 = C
                            elif b_9==None: g.block9 = C
                            else:
                                if b_2==None: g.block2 = C
                                elif b_4==None: g.block4 = C
                                elif b_6==None: g.block6 = C
                                elif b_8==None: g.block8 = C
                                else: pass
            else:
                    if b_1==False:
                        if b_2==False and b_3==None: g.block3 = C
                        elif b_3==False and b_2==None: g.block2 = C
                        elif b_5==False and b_9==None: g.block9 = C
                        elif b_4==False and b_7==None: g.block7 = C
                        elif b_7==False and b_4==None: g.block4 = C
                    elif b_3==False:
                        if b_2==False and b_1==None: g.block3 = C
                        elif b_1==False and b_2==None: g.block2 = C
                        elif b_5==False and b_7==None: g.block9 = C
                        elif b_6==False and b_9==None: g.block7 = C
                        elif b_9==False and b_6==None: g.block4 = C
                    elif b_7==False:
                        if b_1==False and b_4==None: g.block4 = C
                        elif b_4==False and b_1==None: g.block1 = C
                        elif b_5==False and b_3==None: g.block3 = C
                        elif b_8==False and b_9==None: g.block9 = C
                        elif b_9==False and b_8==None: g.block8 = C
                    elif b_9==False:
                        if b_3==False and b_6==None: g.block6 = C
                        elif b_6==False and b_3==None: g.block3 = C
                        elif b_5==False and b_1==None: g.block1 = C
                        elif b_8==False and b_7==None: g.block7 = C
                        elif b_7==False and b_8==None: g.block8 = C
                    elif b_5==False:
                        if b_2==False and b_8==None: g.block8 = C
                        elif b_8==False and b_2==None: g.block2 = C
                        elif b_4==False and b_6==None: g.block6 = C
                        elif b_6==False and b_4==None: g.block4 = C
                    elif b_1==True:
                        if b_2==True and b_3==None: g.block3 = C
                        elif b_3==True and b_2==None: g.block2 = C
                        elif b_5==True and b_9==None: g.block9 = C
                        elif b_4==True and b_7==None: g.block7 = C
                        elif b_7==True and b_4==None: g.block4 = C
                    elif b_3==True:
                        if b_2==True and b_1==None: g.block3 = C
                        elif b_1==True and b_2==None: g.block2 = C
                        elif b_5==True and b_7==None: g.block9 = C
                        elif b_6==True and b_9==None: g.block7 = C
                        elif b_9==True and b_6==None: g.block4 = C
                    elif b_7==True:
                        if b_1==True and b_4==None: g.block4 = C
                        elif b_4==True and b_1==None: g.block1 = C
                        elif b_5==True and b_3==None: g.block3 = C
                        elif b_8==True and b_9==None: g.block9 = C
                        elif b_9==True and b_8==None: g.block8 = C
                    elif b_9==True:
                        if b_3==True and b_6==None: g.block6 = C
                        elif b_6==True and b_3==None: g.block3 = C
                        elif b_5==True and b_1==None: g.block1 = C
                        elif b_8==True and b_7==None: g.block7 = C
                        elif b_7==True and b_8==None: g.block8 = C
                    elif b_5==True:
                        if b_2==True and b_8==None: g.block8 = C
                        elif b_8==True and b_2==None: g.block2 = C
                        elif b_4==True and b_6==None: g.block6 = C
                        elif b_6==True and b_4==None: g.block4 = C
                    else:
                        if b_1==True and b_5==True and b_9==None: g.block9 = C
                        elif b_9==True and b_5==True and b_1==None: g.block1 = C
                        elif b_3==True and b_5==True and b_7==None: g.block7 = C
                        elif b_7==True and b_5==True and b_3==None: g.block3 = C
                        elif b_2==True and b_5==True and b_8==None: g.block8 = C
                        elif b_8==True and b_5==True and b_2==None: g.block2 = C
                        elif b_4==True and b_5==True and b_6==None: g.block6 = C
                        elif b_6==True and b_5==True and b_4==None: g.block4 = C
                        else:
                            if b_1==None: g.block1 = C
                            elif b_3==None: g.block3 = C
                            elif b_7==None: g.block7 = C
                            elif b_9==None: g.block9 = C
                            else:
                                if b_2==None: g.block2 = C
                                elif b_4==None: g.block4 = C
                                elif b_6==None: g.block6 = C
                                elif b_8==None: g.block8 = C
                                else: pass
        elif chance==8:
            if b_1==True and b_5==True and b_9==None: g.block9 = C
            elif b_9==True and b_5==True and b_1==None: g.block1 = C
            elif b_3==True and b_5==True and b_7==None: g.block7 = C
            elif b_7==True and b_5==True and b_3==None: g.block3 = C
            elif b_2==True and b_5==True and b_8==None: g.block8 = C
            elif b_8==True and b_5==True and b_2==None: g.block2 = C
            elif b_4==True and b_5==True and b_6==None: g.block6 = C
            elif b_6==True and b_5==True and b_4==None: g.block4 = C
            else:
                if b_1==False and b_9==None: g.block9 = C
                elif b_2==False and b_8==None: g.block8 = C
                elif b_3==False and b_7==None: g.block7 = C
                elif b_4==False and b_6==None: g.block6 = C
                elif b_6==False and b_4==None: g.block4 = C
                elif b_7==False and b_3==None: g.block3 = C
                elif b_8==False and b_2==None: g.block2 = C
                elif b_9==False and b_1==None: g.block1 = C
                else:
                    if b_1==None: g.block1 = C
                    elif b_3==None: g.block3 = C
                    elif b_7==None: g.block7 = C
                    elif b_9==None: g.block9 = C
                    else:
                        if b_2==None: g.block2 = C
                        elif b_4==None: g.block4 = C
                        elif b_6==None: g.block6 = C
                        elif b_8==None: g.block8 = C
                        else: pass
        elif chance==9:
            if b_1==True and b_5==True and b_9==None: g.block9 = C
            elif b_9==True and b_5==True and b_1==None: g.block1 = C
            elif b_3==True and b_5==True and b_7==None: g.block7 = C
            elif b_7==True and b_5==True and b_3==None: g.block3 = C
            elif b_2==True and b_5==True and b_8==None: g.block8 = C
            elif b_8==True and b_5==True and b_2==None: g.block2 = C
            elif b_4==True and b_5==True and b_6==None: g.block6 = C
            elif b_6==True and b_5==True and b_4==None: g.block4 = C
            else:
                if b_1==False and b_9==None: g.block9 = C
                elif b_2==False and b_8==None: g.block8 = C
                elif b_3==False and b_7==None: g.block7 = C
                elif b_4==False and b_6==None: g.block6 = C
                elif b_6==False and b_4==None: g.block4 = C
                elif b_7==False and b_3==None: g.block3 = C
                elif b_8==False and b_2==None: g.block2 = C
                elif b_9==False and b_1==None: g.block1 = C
                else:
                    if b_1==None: g.block1 = C
                    elif b_3==None: g.block3 = C
                    elif b_7==None: g.block7 = C
                    elif b_9==None: g.block9 = C
                    else:
                        if b_2==None: g.block2 = C
                        elif b_4==None: g.block4 = C
                        elif b_6==None: g.block6 = C
                        elif b_8==None: g.block8 = C
                        else: pass
    def mode_assigner():
        '''Assigns The Game Mode Via Human Readable Input.'''
        g = game
        while 1==1:
            print("Which type of player you want ?")
            g.one_second_delay()
            print("Type 'human' for 2-Player Mode and 'computer' for 1-Player Mode.")
            g.one_second_delay()
            undecided_game_mode_ = input("Type : ")
            undecided_game_mode = undecided_game_mode_.lower()
            if undecided_game_mode=="exit" or undecided_game_mode=="q": g.game_closer()
            else: pass
            computer_player_deciding_1 = undecided_game_mode.find("c")
            computer_player_deciding_2 = undecided_game_mode.find("o")
            computer_player_deciding_3 = undecided_game_mode.find("p")
            computer_player_deciding_4 = undecided_game_mode.find("r")
            human_player_deciding_1 = undecided_game_mode.find("h")
            human_player_deciding_2 = undecided_game_mode.find("u")
            human_player_deciding_3 = undecided_game_mode.find("m")
            human_player_deciding_4 = undecided_game_mode.find("a")
            human_player_deciding_5 = undecided_game_mode.find("n")
            cpd1 = True  if computer_player_deciding_1!=-1 else False
            cpd2 = True if computer_player_deciding_2!=-1 else False
            cpd3 = True if computer_player_deciding_3!=-1 else False
            cpd4 = True if computer_player_deciding_4!=-1 else False
            hpd1 = True if human_player_deciding_1!=-1 else False
            hpd2 = True if human_player_deciding_2!=-1 else False
            hpd3 = True if human_player_deciding_3!=-1 else False
            hpd4 = True if human_player_deciding_4!=-1 else False
            hpd5 = True if human_player_deciding_5!=-1 else False
            if cpd1:
                if cpd2: g.decided_game_mode = 'computer'
                elif cpd3: g.decided_game_mode = 'computer'
                elif cpd4: g.decided_game_mode = 'computer'
                else: pass
            elif cpd2:
                if cpd3: g.decided_game_mode = 'computer'
                elif cpd4: g.decided_game_mode = 'computer'
                else: pass
            elif cpd3:
                if cpd4: g.decided_game_mode = 'computer'
            elif hpd1:
                if hpd2:
                    if hpd3: g.decided_game_mode = 'human'
                    elif hpd4: g.decided_game_mode = 'human'
                    elif hpd5: g.decided_game_mode = 'human'
                    else: pass
                elif hpd3:
                    if hpd4: g.decided_game_mode = 'human'
                    elif hpd5: g.decided_game_mode = 'human'
                    else: pass
                elif hpd4 and hpd5: g.decided_game_mode = 'human'
                else: pass
            elif hpd2:
                if hpd3:
                    if hpd4: g.decided_game_mode = 'human'
                    elif hpd5: g.decided_game_mode = 'human'
                    else: pass
                elif hpd4 and hpd5: g.decided_game_mode = 'human'
                else: pass
            elif hpd3 and hpd4 and hpd5: 'human'
            else: pass
            print("Understanding and deciding your oppponent...")
            g.one_second_delay()
            print(g.blank)
            if g.decided_game_mode=="human":
                print("You have chosen human as your opponent and game mode is 2-Player mode.")
                g.one_second_delay()
                g.one_second_delay()
                print("Hope you will have the best game play :)")
                g.one_second_delay()
                print("ENJOY...")
                g.one_second_delay()
                g.game_mode = "2-Player"
                print(g.blank)
                break
            elif g.decided_game_mode=="computer":
                print("You have chosen computer as your opponent and game mode is 1-Player mode.")
                g.one_second_delay()
                g.one_second_delay()
                print("Hope you will win in the game :)")
                g.one_second_delay()
                print("ALL THE BEST...")
                g.one_second_delay()
                g.game_mode = "1-Player"
                print(g.blank)
                break
            else:
                print("Sorry, computer can't understand which type of opponent you want.")
                g.one_second_delay()
                print("Please try again :(")
                g.one_second_delay()
                print("You can type 'Computer' for 1-Player mode and 'Human' for 2-Player mode...")
                g.one_second_delay()
                g.one_second_delay()
                g.one_second_delay()
                g.decided_game_mode = ""
                print(g.blank)
    def main_game_starter():
        "Starts the game."
        g = game
        print("About   : A very small game of OX.")
        print("Version : 3.0")
        print(''' " I am myself the development team, support me. :) "\n''')
        boss_input = input("Press ENTER[RETURN] to start the game. ")
        boss = boss_input.lower()
        if boss=="boss": g.AI_assistance = False
        elif boss=="exit": exit()
        else: pass
        print(g.blank)
        print("STARTING GAME...")
        g.one_second_delay()
        g.one_second_delay()
        while 1==1:
            g = g
            print(g.blank)
            print("This is the game of 'OX', (OX trainer is better to call.)")
            g.one_second_delay()
            g.one_second_delay()
            print("Play more and more with computer or in 2 player mode")
            g.one_second_delay()
            g.one_second_delay()
            g.mode_assigner()
            if g.game_mode=="1-Player": g.Computer_player_game()
            elif g.game_mode=="2-Player": g.Human_player_game()
            else: print("Please try again :(")
    def name_assigner(Value):
        '''Assigns The Name Of The Players.'''
        g = game
        name_1 = "C.P.U.   (1) "
        name_2 = "A.I.     (2) "
        name_3 = "Defeater (3) "
        name_4 = "Computer (4) "
        name_5 = "Opponent (5) "
        result = False
        while result==False:
            assistance = Value
            mode = g.game_mode
            if g.P1_name!="": p1_name = True
            else: p1_name = False
            if g.P2_name!="": p2_name = True
            else: p2_name = False
            if g.Player_name!="": Player_name = True
            else: Player_name = False
            if g.Computer_name!="": Computer_name = True
            else: Computer_name = False
            if mode=="2-Player":
                if p1_name==False and p2_name==False:
                    while 1==1:
                        if assistance==True:
                            print(g.blank)
                            print("Tell me the name of first player.")
                            g.one_second_delay()
                            g.one_second_delay()
                        else: print(g.blank)
                        temp_1 = input("Player-1 name : ")
                        if temp_1=="exit" or temp_1=="q": g.game_closer()
                        else: pass
                        if assistance==True: print("Checking whether the name is in the limits told before.")
                        else: pass
                        error = g.name_error_finder(temp_1)
                        if error=="True":
                            print(g.blank)
                            print("Name you entered exceeds one or more limits.")
                            g.one_second_delay()
                            g.one_second_delay()
                            print(g.blank)
                            print("Please remember that,")
                            g.one_second_delay()
                            print("Name should be in limit of 3 to 20 characters.")
                            print("No special character is allowed (like '@', '#' etc.)")
                            g.one_second_delay()
                            g.one_second_delay()
                            input("Press ENTER[RETURN] to continue...")
                        else:
                            print(g.blank)
                            print(f"Player-1 name : {temp_1}")
                            ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                            ask1 = ask_1.lower()
                            if ask1=="exit" or ask1=="q": g.game_closer()
                            else: pass
                            y1 = ask1.find('y')
                            if ask_1=="":
                                g.P1_name = temp_1
                                print(g.blank)
                                break
                            elif y1!=-1:
                                g.P1_name = temp_1
                                print(g.blank)
                                break
                            else:
                                print("Type the name again.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                    while 1==1:
                        if assistance==True:
                            print("Tell me the name of second player.")
                            g.one_second_delay()
                            g.one_second_delay()
                        else: pass
                        temp_2 = input("Player-2 name : ")
                        if assistance==True: print("Checking whether the name is in the limits told before.")
                        else: pass
                        error = g.name_error_finder(temp_2)
                        if error=="True":
                            print(g.blank)
                            print("Name you entered exceeds one or more limits.")
                            g.one_second_delay()
                            g.one_second_delay()
                            print(g.blank)
                            print("Please remember that,")
                            g.one_second_delay()
                            print("Name should be in limit of 3 to 20 characters.")
                            print("No special character is allowed (like '@', '#' etc.)")
                            g.one_second_delay()
                            g.one_second_delay()
                            input("Press ENTER[RETURN] to continue...")
                        else:
                            print(g.blank)
                            print(f"Player-2 name : {temp_2}")
                            ask_2 = input("confirm ? [Yes or RETURN / No] : ")
                            ask2 = ask_2.lower()
                            if ask2=="exit" or ask2=="q": g.game_closer()
                            else: pass
                            y2 = ask2.find('y')
                            if ask_2=="": g.P2_name = temp_2; break
                            elif y2!=-1: g.P2_name = temp_2; break
                            else:
                                print("Type the name again.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                    result = True
                elif p1_name==True and p2_name==True:
                    print("Name of both players were given before.")
                    g.one_second_delay()
                    print(f"Player-1 name : {g.P1_name}")
                    print(f"Player-2 name : {g.P2_name}")
                    g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        print("Do you want to reset any of these names ?")
                        g.one_second_delay()
                        ask_1 = input("[Yes/No] : ")
                        ask1 = ask_1.lower()
                        if ask1=="exit" or ask1=="q": g.game_closer()
                        else: pass
                        y1 = ask1.find('y')
                        if y1!=-1: y1 = True; break
                        else: y1 = False; break
                    if y1==True:
                        print(g.blank)
                        print(f"Player-1 name : {g.P1_name}")
                        g.one_second_delay()
                        while 1==1:
                            print("Enter new name of Player-1.")
                            print("Or leave blank[ENTER/RETURN] to use the old name.")
                            g.one_second_delay()
                            temp_1 = input("Player-1 name : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if temp_1=="": pass
                            else:
                                if assistance==True: print("Checking whether the name is in the limits told before.")
                                else: pass
                                error = g.name_error_finder(temp_1)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limits.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Player-1 name : {temp_1}")
                                    ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask1 = ask_1.lower()
                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                    else: pass
                                    y1 = ask1.find('y')
                                    if ask_1=="":
                                        g.P1_name = temp_1
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.P1_name = temp_1
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                        print(f"Player-2 name : {g.P2_name}")
                        g.one_second_delay()
                        while 1==1:
                            print("Enter new name of Player-2.")
                            print("Or leave blank[ENTER/RETURN] to use the old name.")
                            g.one_second_delay()
                            temp_2 = input("Player-2 name : ")
                            if temp_2=="exit" or temp_2=="q": g.game_closer()
                            else: pass
                            if temp_2=="": pass
                            else:
                                if assistance==True: print("Checking whether the name is in the limits told before.")
                                else: pass
                                error = g.name_error_finder(temp_2)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limits.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Player-2 name : {temp_2}")
                                    ask_2 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask2 = ask_2.lower()
                                    if ask2=="exit" or ask2=="q": g.game_closer()
                                    else: pass
                                    y2 = ask2.find('y')
                                    if ask_2=="":
                                        g.P2_name = temp_2
                                        print(g.blank)
                                        break
                                    elif y2!=-1:
                                        g.P2_name = temp_2
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                    else: pass
                    result = True
                elif p1_name==True and p2_name==False:
                    print("Name of Player-1 is once used before.")
                    g.one_second_delay()
                    print(f"Player-1 name : {g.P1_name}")
                    g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        reset_1 = input("Do you want to reset it ? \n[Yes/No] : ")
                        if reset_1=="exit" or reset_1=="q": g.game_closer()
                        else: pass
                        y1 = reset_1.find('y')
                        n1 = reset_1.find('n')
                        if y1!=-1:  y1 = True
                        else: y1 = False
                        if n1!=-1: n1 = True
                        else: n1 = False
                        if y1==False and n1==False: print("Please type again."); print(g.blank)
                        else: break
                    if n1==True:
                        if assistance==True: print("Then tell me the name of another player.")
                        else: pass
                        g.one_second_delay()
                        while 1==1:
                            temp_2 = input("Player-2 name : ")
                            if temp_2=="exit" or temp_2=="q": g.game_closer()
                            else: pass
                            if assistance==True: print("Checking whether the name is in the limits told before.")
                            else: pass
                            g.one_second_delay()
                            g.one_second_delay()
                            error = g.name_error_finder(temp_2)
                            if error=="True":
                                print(g.blank)
                                print("Name you entered exceeds one or more limits.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                                print("Please remember that,")
                                g.one_second_delay()
                                print("Name should be in limit of 3 to 20 characters.")
                                print("No special character is allowed (like '@', '#' etc.)")
                                g.one_second_delay()
                                g.one_second_delay()
                                input("Press ENTER[RETURN] to continue...")
                            else:
                                print(g.blank)
                                print(f"Player-2 name : {temp_2}")
                                ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y2 = ask1.find('y')
                                if ask_1=="": g.P2_name = temp_2; break
                                elif y2!=-1: g.P2_name = temp_2; break
                                else:
                                    print("Type the name again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                    else: pass
                    result = True
                elif p1_name==False and p2_name==True:
                    print("Name of Player-2 is once used before.")
                    g.one_second_delay()
                    print(f"Player-2 name : {g.P2_name}")
                    g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        reset_1 = input("Do you want to reset it ? \n[Yes/No] : ")
                        if reset_1=="exit" or reset_1=="q": g.game_closer()
                        else: pass
                        y1 = reset_1.find('y')
                        n1 = reset_1.find('n')
                        if y1!=-1: y1 = True
                        else: y1 = False
                        if n1!=-1: n1 = True
                        else: n1 = False
                        if y1==False and n1==False: print("Please type again."); print(g.blank)
                        else: break
                    if n1==True:
                        if assistance==True: print("Then tell me the name of another player.")
                        else: pass
                        g.one_second_delay()
                        while 1==1:
                            temp_1 = input("Player-1 name : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if assistance==True: print("Checking whether the name is in the limits told before.")
                            else: pass
                            g.one_second_delay()
                            g.one_second_delay()
                            error = g.name_error_finder(temp_1)
                            if error=="True":
                                print(g.blank)
                                print("Name you entered exceeds one or more limits.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                                print("Please remember that,")
                                g.one_second_delay()
                                print("Name should be in limit of 3 to 20 characters.")
                                print("No special character is allowed (like '@', '#' etc.)")
                                g.one_second_delay()
                                g.one_second_delay()
                                input("Press ENTER[RETURN] to continue...")
                            else:
                                print(g.blank)
                                print(f"Player-1 name : {temp_1}")
                                ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y2 = ask1.find('y')
                                if ask_1=="": g.P1_name = temp_1; break
                                elif y2!=-1: g.P1_name = temp_1; break
                                else:
                                    print("Type the name again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                    else: pass
                    result = True
                else:
                    print("CRASH..!!")
                    g.one_second_delay()
                    exit()
                print(g.blank)
                print(f"Player-1 : {g.P1_name}")
                print("         V/S           ")
                print(f"Player-2 : {g.P2_name}")
                g.one_second_delay()
                g.one_second_delay()
                print(g.blank)
            elif mode=="1-Player":
                if Player_name==False and Computer_name==False:
                    print(g.blank)
                    if assistance==True:
                        print("You will be given some names for computer to choose.")
                        g.one_second_delay()
                        print("Type the number in the parenthesis (Brackets) to choose the names,")
                        g.one_second_delay()
                        print("Type '0' to choose a random name from the names given,")
                        g.one_second_delay()
                        print("Or type a name for computer.")
                        g.one_second_delay()
                    else:
                        print("Type or choose a name for computer.")
                        g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        print(g.blank)
                        print("Some names for computer.")
                        g.one_second_delay()
                        print(name_1); print(name_2); print(name_3); print(name_4); print(name_5)
                        g.one_second_delay()
                        temp_1 = input("Type : ")
                        if temp_1=="exit" or temp_1=="q": g.game_closer()
                        else: pass
                        if len(temp_1)==1:
                            if temp_1=="1": g.Computer_name = "C.P.U."; break
                            elif temp_1=="2": g.Computer_name = "A.I."; break
                            elif temp_1=="3": g.Computer_name = "Defeater"; break
                            elif temp_1=="4": g.Computer_name = "Computer"; break
                            elif temp_1=="5": g.Computer_name = "Opponent"; break
                            elif temp_1=="0":
                                number = random.randint(1, 5)
                                if number==1: g.Computer_name = "C.P.U."; break
                                elif number==2: g.Computer_name = "A.I."; break
                                elif number==3: g.Computer_name = "Defeater"; break
                                elif number==4: g.Computer_name = "Computer"; break
                                elif number==5: g.Computer_name = "Opponent"; break
                                else: print("Type again."); g.one_second_delay()
                            else: print("Type again."); g.one_second_delay()
                        else:
                            if assistance==True:
                                print("Checking whether the name is in the limits told before")
                                g.one_second_delay()
                            else: pass
                            error = g.name_error_finder(temp_1)
                            if error=="True":
                                print(g.blank)
                                print("Name you entered exceeds one or more limit.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                                print("Please remember that,")
                                g.one_second_delay()
                                print("Name should be in limit of 3 to 20 characters.")
                                print("No special character is allowed (like '@', '#' etc.)")
                                g.one_second_delay()
                                g.one_second_delay()
                                input("Press ENTER[RETURN] to continue...")
                            else:
                                print(g.blank)
                                print(f"Computer's name : {temp_1}")
                                ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find('y')
                                if ask_1=="":
                                    g.Computer_name = temp_1
                                    print(g.blank)
                                    break
                                elif y1!=-1:
                                    g.Computer_name = temp_1
                                    print(g.blank)
                                    break
                                else:
                                    print("Type the name again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                    while 1==1:
                        print(g.blank)
                        print("Type a name for you.")
                        g.one_second_delay()
                        g.one_second_delay()
                        temp_2 = input("Type : ")
                        if temp_2=="exit" or temp_2=="q": g.game_closer()
                        else: pass
                        if assistance==True:
                            print("Checking whether the name is in the limits told before.")
                            g.one_second_delay()
                        else: pass
                        error = g.name_error_finder(temp_2)
                        if error=="True":
                            print(g.blank)
                            print("Name you entered exceeds one or more limits.")
                            g.one_second_delay()
                            g.one_second_delay()
                            print(g.blank)
                            print("Please remember that,")
                            g.one_second_delay()
                            print("Name should be in limit of 3 to 20 characters.")
                            print("No special character is allowed (like '@', '#' etc.)")
                            g.one_second_delay()
                            g.one_second_delay()
                            input("Press ENTER[RETURN] to continue...")
                        else:
                            print(g.blank)
                            print(f"Player's name : {temp_2}")
                            ask_2 = input("confirm ? [Yes or RETURN / No] : ")
                            ask2 = ask_2.lower()
                            if ask2=="exit" or ask2=="q": g.game_closer()
                            else: pass
                            y2 = ask2.find('y')
                            if ask_2=="":
                                g.Player_name = temp_2
                                print(g.blank)
                                break
                            elif y2!=-1:
                                g.Player_name = temp_2
                                print(g.blank)
                                break
                            else:
                                print("Type the name again.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                    result = True
                elif Player_name==True and Computer_name==True:
                    print(g.blank)
                    print("You entered the names before.")
                    g.one_second_delay()
                    print(f"Player's name   : {g.Player_name}")
                    print(f"Computer's name : {g.Computer_name}")
                    g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        print("Do you want to reset any of these names ?")
                        g.one_second_delay()
                        ask_1 = input("[Yes/No] : ")
                        ask1 = ask_1.lower()
                        if ask1=="exit" or ask1=="q": g.game_closer()
                        else: pass
                        y1 = ask1.find('y')
                        if y1!=-1: y1 = True; break
                        else: y1 = False; break
                    if y1==True:
                        print(g.blank)
                        print(f"Player's name : {g.Player_name}")
                        g.one_second_delay()
                        while 1==1:
                            print("Enter a new name.")
                            print("Or leave blank[ENTER/RETURN] to use old name.")
                            g.one_second_delay()
                            temp_1 = input("Player-1 name : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if temp_1=="": pass
                            else:
                                if assistance==True:
                                    print("Checking whether the name is in the limits told before.")
                                    g.one_second_delay()
                                else: pass
                                error = game.name_error_finder(temp_1)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limits.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Player's name : {g.Player_name}")
                                    ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask1 = ask_1.lower()
                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                    else: pass
                                    y1 = ask1.find('y')
                                    if ask_1=="":
                                        g.Player_name = temp_1
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.Player_name = temp_1
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                        print(g.blank)
                        print(f"Computer's name : {g.Computer_name}")
                        g.one_second_delay()
                        while 1==1:
                            print(g.blank)
                            print("Some names for computer.")
                            g.one_second_delay()
                            print(name_1); print(name_2); print(name_3); print(name_4); print(name_5)
                            g.one_second_delay()
                            temp_2 = input("Type : ")
                            if temp_2=="exit" or temp_2=="q": g.game_closer()
                            else: pass
                            if len(temp_2)==1:
                                if temp_2=="1": g.Computer_name = "C.P.U."; break
                                elif temp_2=="2": g.Computer_name = "A.I."; break
                                elif temp_2=="3": g.Computer_name = "Defeater"; break
                                elif temp_2=="4": g.Computer_name = "Computer"; break
                                elif temp_2=="5": g.Computer_name = "Opponent"; break
                                elif temp_2=="0":
                                    number = random.randint(1, 5)
                                    if number==1: g.Computer_name = "C.P.U."; break
                                    elif number==2: g.Computer_name = "A.I."; break
                                    elif number==3: g.Computer_name = "Defeater"; break
                                    elif number==4: g.Computer_name = "Computer"; break
                                    elif number==5: g.Computer_name = "Opponent"; break
                                    else: print("Type again."); g.one_second_delay()
                                else: print("Type again."); g.one_second_delay()
                            else:
                                if assistance==True:
                                    print("Checking whteher the name is in the limits told before.")
                                    g.one_second_delay()
                                else: pass
                                error = g.name_error_finder(temp_2)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limit.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Computer's name : {temp_2}")
                                    ask_2 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask2 = ask_2.lower()
                                    if ask2=="exit" or ask2=="q": g.game_closer()
                                    else: pass
                                    y2 = ask2.find('y')
                                    if ask_2=="":
                                        g.Computer_name = temp_2
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.Computer_name = temp_2
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                    else: pass
                    result = True
                elif Player_name==True and Computer_name==False:
                    print(g.blank)
                    print("You have given your name before.")
                    g.one_second_delay()
                    print(f"Player's name : {g.Player_name}")
                    g.one_second_delay()
                    g.one_second_delay()
                    while 1==1:
                        reset_1 = input("Do you want to reset it ? \n[Yes/No] : ")
                        if reset_1=="exit" or reset_1=="q": g.game_closer()
                        else: pass
                        y1 = reset_1.find('y')
                        n1 = reset_1.find('n')
                        if y1!=-1: y1 = True
                        else: y1 = False
                        if n1!=-1: n1 = True
                        else: n1 = False
                        if y1==False and n1==False: print("Please type again."); print(g.blank)
                        else: break
                    if n1==True:
                        if assistance==True: print("Then tell me the name of Computer.")
                        else: pass
                        g.one_second_delay()
                        while 1==1:
                            print(g.blank)
                            print("Some names for computer.")
                            g.one_second_delay()
                            print(name_1); print(name_2); print(name_3); print(name_4); print(name_5)
                            g.one_second_delay()
                            temp_1 = input("Type : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if len(temp_1)==1:
                                if temp_1=="1": g.Computer_name = "C.P.U."; break
                                elif temp_1=="2": g.Computer_name = "A.I."; break
                                elif temp_1=="3": g.Computer_name = "Defeater"; break
                                elif temp_1=="4": g.Computer_name = "Computer"; break
                                elif temp_1=="5": g.Computer_name = "Opponent"; break
                                elif temp_1=="0":
                                    number = random.randint(1, 5)
                                    if number==1: g.Computer_name = "C.P.U."; break
                                    elif number==2: g.Computer_name = "A.I."; break
                                    elif number==3: g.Computer_name = "Defeater"; break
                                    elif number==4: g.Computer_name = "Computer"; break
                                    elif number==5: g.Computer_name = "Opponent"; break
                                    else: print("Type again."); g.one_second_delay()
                                else: print("Type again."); g.one_second_delay()
                            else:
                                if assistance==True: print("Checking whether the name is in the limits told before."); pass
                                error = g.name_error_finder(temp_1)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limit.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Computer's name : {temp_1}")
                                    ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask1 = ask_1.lower()
                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                    else: pass
                                    y1 = ask1.find('y')
                                    if ask_1=="":
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                    elif y1==True:
                        print(g.blank)
                        print("Tell me the new name.")
                        g.one_second_delay()
                        g.one_second_delay()
                        while 1==1:
                            print(g.blank)
                            temp_2 = input("Player's name : ")
                            if temp_2=="exit" or temp_2=="q": g.game_closer()
                            else: pass
                            if assistance==True:
                                print("Checking whether the name is in the limits told before.")
                                g.one_second_delay()
                            else: pass
                            error = game.name_error_finder(temp_2)
                            if error=="True":
                                print(g.blank)
                                print("Name you entered exceeds one or more limits.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                                print("Please remember that,")
                                g.one_second_delay()
                                print("Name should be in limit of 3 to 20 characters.")
                                print("No special character is allowed (like '@', '#' etc.)")
                                g.one_second_delay()
                                g.one_second_delay()
                                input("Press ENTER[RETURN] to continue...")
                            else:
                                print(g.blank)
                                print(f"Player's name : {g.Player_name}")
                                ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                ask1 = ask_1.lower()
                                if ask1=="exit" or ask1=="q": g.game_closer()
                                else: pass
                                y1 = ask1.find('y')
                                if ask_1=="":
                                    g.Player_name = temp_2
                                    print(g.blank)
                                    break
                                elif y1!=-1:
                                    g.Player_name = temp_2
                                    print(g.blank)
                                    break
                                else:
                                    print("Type the name again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                        print(g.blank)
                        if assistance==True: print("Tell me the name of Computer.")
                        else: pass
                        g.one_second_delay()
                        while 1==1:
                            print(g.blank)
                            print("Some names for computer.")
                            g.one_second_delay()
                            print(name_1); print(name_2); print(name_3); print(name_4); print(name_5)
                            g.one_second_delay()
                            temp_1 = input("Type : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if len(temp_1)==1:
                                if temp_1=="1": g.Computer_name = "C.P.U."; break
                                elif temp_1=="2": g.Computer_name = "A.I."; break
                                elif temp_1=="3": g.Computer_name = "Defeater"; break
                                elif temp_1=="4": g.Computer_name = "Computer"; break
                                elif temp_1=="5": g.Computer_name = "Opponent"; break
                                elif temp_1=="0":
                                    number = random.randint(1, 5)
                                    if number==1: g.Computer_name = "C.P.U."; break
                                    elif number==2: g.Computer_name = "A.I."; break
                                    elif number==3: g.Computer_name = "Defeater"; break
                                    elif number==4: g.Computer_name = "Computer"; break
                                    elif number==5: g.Computer_name = "Opponent"; break
                                    else: print("Type again."); g.one_second_delay()
                                else: print("Type again."); g.one_second_delay()
                            else:
                                if assistance==True: print("Checking whether the name is in the limits told before.")
                                else: pass
                                error = g.name_error_finder(temp_1)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limit.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Computer's name : {temp_1}")
                                    ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask1 = ask_1.lower()
                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                    else: pass
                                    y1 = ask1.find('y')
                                    if ask_1=="":
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                    else: pass
                    result = True
                elif Player_name==False and Computer_name==True:
                    print("Name of computer was given before.")
                    g.one_second_delay()
                    print(f"Computer's name : {g.Computer_name}")
                    while 1==1:
                        reset_1 = input("Do you want to reset it ? \n[Yes/No] : ")
                        if reset_1=="exit" or reset_1=="q": g.game_closer()
                        else: pass
                        y1 = reset_1.find('y')
                        n1 = reset_1.find('n')
                        if y1!=-1: y1 = True
                        else: y1 = False
                        if n1!=-1: n1 = True
                        else: n1 = False
                        if y1==False and n1==False: print("Please type again."); print(g.blank)
                        else: break
                    if y1==True:
                        print(g.blank)
                        print("Tell the new name of computer.")
                        g.one_second_delay()
                        while 1==1:
                            print(g.blank)
                            print("Some names for computer.")
                            g.one_second_delay()
                            print(name_1); print(name_2); print(name_3); print(name_4); print(name_5)
                            g.one_second_delay()
                            temp_1 = input("Type : ")
                            if temp_1=="exit" or temp_1=="q": g.game_closer()
                            else: pass
                            if len(temp_1)==1:
                                if temp_1=="1": g.Computer_name = "C.P.U."; break
                                elif temp_1=="2": g.Computer_name = "A.I."; break
                                elif temp_1=="3": g.Computer_name = "Defeater"; break
                                elif temp_1=="4": g.Computer_name = "Computer"; break
                                elif temp_1=="5": g.Computer_name = "Opponent"; break
                                elif temp_1=="0":
                                    number = random.randint(1, 5)
                                    if number==1: g.Computer_name = "C.P.U."; break
                                    elif number==2: g.Computer_name = "A.I."; break
                                    elif number==3: g.Computer_name = "Defeater"; break
                                    elif number==4: g.Computer_name = "Computer"; break
                                    elif number==5: g.Computer_name = "Opponent"; break
                                    else:
                                        print("Type again.")
                                        g.one_second_delay()
                                else: print("Type again."); g.one_second_delay()
                            else:
                                if assistance==True:
                                    print("Checking whether the name is in the limits told before")
                                    g.one_second_delay()
                                else: pass
                                error = g.name_error_finder(temp_1)
                                if error=="True":
                                    print(g.blank)
                                    print("Name you entered exceeds one or more limit.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                                    print("Please remember that,")
                                    g.one_second_delay()
                                    print("Name should be in limit of 3 to 20 characters.")
                                    print("No special character is allowed (like '@', '#' etc.)")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    input("Press ENTER[RETURN] to continue...")
                                else:
                                    print(g.blank)
                                    print(f"Computer's name : {temp_1}")
                                    ask_1 = input("confirm ? [Yes or RETURN / No] : ")
                                    ask1 = ask_1.lower()
                                    if ask1=="exit" or ask1=="q": g.game_closer()
                                    else: pass
                                    y1 = ask1.find('y')
                                    if ask_1=="":
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    elif y1!=-1:
                                        g.Computer_name = temp_1
                                        print(g.blank)
                                        break
                                    else:
                                        print("Type the name again.")
                                        g.one_second_delay()
                                        g.one_second_delay()
                                        print(g.blank)
                        print(g.blank)
                        print("Type the name of player.")
                        g.one_second_delay()
                        while 1==1:
                            temp_2 = input("Player's name : ")
                            if assistance==True:
                                print("Checking whether the name is in the limits told before.")
                                g.one_second_delay()
                            else: pass
                            error = g.name_error_finder(temp_2)
                            if error=="True":
                                print(g.blank)
                                print("Name you entered exceeds one or more limits.")
                                g.one_second_delay()
                                g.one_second_delay()
                                print(g.blank)
                                print("Please remember that,")
                                g.one_second_delay()
                                print("Name should be in limit of 3 to 20 characters.")
                                print("No special character is allowed (like '@', '#' etc.)")
                                g.one_second_delay()
                                g.one_second_delay()
                                input("Press ENTER[RETURN] to continue...")
                            else:
                                print(g.blank)
                                print(f"Player's name : {temp_2}")
                                ask_2 = input("confirm ? [Yes or RETURN / No] : ")
                                ask2 = ask_2.lower()
                                if ask2=="exit" or ask2=="q": g.game_closer()
                                else: pass
                                y2 = ask2.find('y')
                                if ask_2=="":
                                    g.Player_name = temp_2
                                    print(g.blank)
                                    break
                                elif y1!=-1:
                                    g.Player_name = temp_2
                                    print(g.blank)
                                    break
                                else:
                                    print("Type the name again.")
                                    g.one_second_delay()
                                    g.one_second_delay()
                                    print(g.blank)
                    result = True
                else:
                    print("CRASH..!!")
                    g.one_second_delay()
                    exit()
                print(f"Player   : {g.Player_name}")
                print("         V/S           ")
                print(f"Computer : {g.Computer_name}")
                g.one_second_delay()
                g.one_second_delay()
                print(g.blank)
    def one_second_delay():
        '''Adds A Time Lap Of 1-Second.'''
        a = datetime.datetime.today()
        b = str(a)
        c = b[17:21]
        second_ = c[0:2]
        if second_=="59": second = "00"
        else:
            second__ = int(second_)
            second___ = second__+1
            second____ = str(second___)
            if len(second____)==1: second = f"0{second____}"
            else: second = second____
        miliseconds = c[2:4]
        upto_time = second+miliseconds
        while 1==1:
            d = datetime.datetime.today()
            e = str(d)
            f = e[17:21]
            if f==upto_time: break
            else: continue
    def chance_assigner(help_):
        '''Assigns The First Chance For A Player.'''
        g = game
        assistance = help_
        undecided_chance = random.randint(1, 2)
        if g.game_mode=="1-Player":
            if undecided_chance==1: return "Player"
            else: return "Computer"
        elif g.game_mode=="2-Player":
            if assistance==True:
                print("Will you decide who is going to play first [Method 1]")
                g.one_second_delay()
                print("Or let the computer decide [Method 2]")
                g.one_second_delay()
            else:
                print("[Method 1] or [Method 2] (For assigning chance)")
                g.one_second_delay()
            ask_1 = input("Method ")
            g.one_second_delay()
            ask1 = ask_1.lower()
            if ask1=="exit" or ask1=="q": g.game_closer()
            else: pass
            conformation_1 = ask1.find("1")
            confirmation_2 = ask1.find("f")
            if conformation_1!=-1: by_self = True
            else:
                if confirmation_2!=-1: by_self = True
                else: by_self = False
            if by_self==True:
                while 1==1:
                    print(g.blank)
                    print("Who is playing on first chance,")
                    g.one_second_delay()
                    print("Player-1 or Player-2 ?")
                    g.one_second_delay()
                    ask_2 = input("Player-")
                    ask2 = ask_2.lower()
                    if ask2=="exit" or ask2=="q": g.game_closer()
                    else: pass
                    if ask2=="1": return "Player-1"
                    elif ask2=="2": return "Player-2"
                    else:
                        number = random.randint(1, 2)
                        if number==1: return "Player-1"
                        else: return "Player-2"
            else:
                number = random.randint(1, 2)
                if number==1: return "Player-1"
                elif number==2: return "Player-2"
                else:
                    number = random.randint(1, 2)
                    if number==1: return "Player-1"
                    else: return "Player-2"
    def winner_block_reseter(winner):
        '''Edits The Game Sheet To Display The Blocks Of The Winner Only.'''
        g = game
        if winner=="Player-1": block = g.P1
        elif winner=="Player-2": block = g.P2
        elif winner=="Player": block = g.P
        else: block = g.C
        if g.block5==block and g.block1==block and g.block9==block:
            g.block2 = " "
            g.block3 = " "
            g.block4 = " "
            g.block6 = " "
            g.block7 = " "
            g.block8 = " "
        elif g.block5==block and g.block3==block and g.block7==block:
            g.block1 = " "
            g.block2 = " "
            g.block4 = " "
            g.block6 = " "
            g.block8 = " "
            g.block9 = " "
        elif g.block1==block and g.block2==block and g.block3==block:
            g.block4 = " "
            g.block5 = " "
            g.block6 = " "
            g.block7 = " "
            g.block8 = " "
            g.block9 = " "
        elif g.block1==block and g.block4==block and g.block7==block:
            g.block2 = " "
            g.block3 = " "
            g.block5 = " "
            g.block6 = " "
            g.block8 = " "
            g.block9 = " "
        elif g.block9==block and g.block8==block and g.block7==block:
            g.block1 = " "
            g.block2 = " "
            g.block3 = " "
            g.block4 = " "
            g.block5 = " "
            g.block6 = " "
        elif g.block9==block and g.block6==block and g.block3==block:
            g.block1 = " "
            g.block2 = " "
            g.block4 = " "
            g.block5 = " "
            g.block7 = " "
            g.block8 = " "
        else: return 1
    def temp_error_finder(temp: str):
        '''Verifies Whether The Block Input Is Correct Or Not.'''
        g = game
        temp = str(temp)
        length = len(temp)
        if length==1: error = False
        else: error = True
        if error==True: error = True
        else:
            if temp=="1": error = False
            elif temp=="2": error = False
            elif temp=="3": error = False
            elif temp=="4": error = False
            elif temp=="5": error = False
            elif temp=="6": error = False
            elif temp=="7": error = False
            elif temp=="8": error = False
            elif temp=="9": error = False
            else: error = True
        if error==True: error = True
        else:
            if temp=="1": error = False if g.block1=='1' else True
            elif temp=="2": error = False if g.block2=='2' else True
            elif temp=="3": error = False if g.block3=='3' else True
            elif temp=="4": error = False if g.block4=='4' else True
            elif temp=="5": error = False if g.block5=='5' else True
            elif temp=="6": error = False if g.block6=='6' else True
            elif temp=="7": error = False if g.block7=='7' else True
            elif temp=="8": error = False if g.block8=='8' else True
            elif temp=="9": error = False if g.block9=='9' else True
            else: error = True
        if error==True: return 1
        else: return 0
    def reset_1():
        '''Resets The Blocks To Play Again In The Same Mode.'''
        g = game
        g.block1 = "1"
        g.block2 = "2"
        g.block3 = "3"
        g.block4 = "4"
        g.block5 = "5"
        g.block6 = "6"
        g.block7 = "7"
        g.block8 = "8"
        g.block9 = "9"
        if g.game_mode=="1-Player": g.chance = 1
        else: pass
    def reset_2():
        '''Resets The Blocks Along With Statistics.'''
        g = game
        g.block1 = "1"
        g.block2 = "2"
        g.block3 = "3"
        g.block4 = "4"
        g.block5 = "5"
        g.block6 = "6"
        g.block7 = "7"
        g.block8 = "8"
        g.block9 = "9"
        if g.game_mode=="1-Player":
            g.chance = 1
            g.P1_score = 0
            g.P1_high_streak = 0
            g.P1_streak = 0
            g.P2_score = 0
            g.P1_high_streak = 0
            g.P2_streak = 0
            g.Chance_of_2 = ""
            g.Total_2_player_matches = 0
        else:
            g.P_score = 0
            g.P_high_streak = 0
            g.P_streak = 0
            g.C_score = 0
            g.C_high_streak = 0
            g.C_streak = 0
            g.Chance_of_1 = ""
            g.Total_1_player_matches = 0
    def game_closer():
        '''Shows Exit Message.'''
        g = game
        print("Thanks For Playing. Hope You Enjoyed :)")
        g.one_second_delay()
        g.one_second_delay()
        g.one_second_delay()
        exit()
game.main_game_starter()
