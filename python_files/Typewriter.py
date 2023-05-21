# Typewriter
import pyautogui
import time
import random
WELCOME_MESSAGE = {
1 : """
    ___        __   ___         __  ___ ___  ___  __  
     |   \  / |  \ |    |    | |  \  |   |  |    |  \ 
     |    \/  |__/ |__  |    | |__/  |   |  |__  |__/ 
     |    /   |    |    | /\ | | \   |   |  |    | \  
     |   /    |    |___ |/  \| |  \ _|_  |  |___ |  \ 

""",
2 : """
     ___   ___                         ___  __   
    |     |       /\    |\  /| |\  /| |    |  \  
    |___  |      /__\   | \/ | | \/ | |__  |__/  
        | |     /    \  |    | |    | |    | \   
     ___| |___ /      \ |    | |    | |___ |  \ 
 
""",
3 : """
     __   ___          __   ___  __    
    |  \ |   | |\  /| |  \ |    |  \   
    |__/ |   | | \/ | |__/ |__  |__/   
    |  \ |   | |    | |  \ |    | \    
    |__/ |___| |    | |__/ |___ |  \   

"""}
BOMBARDMENT = {
1 : """
           _           _           _       
          /-\         /-\         /-\      
         /___\       /___\       /___\     
        /|---|\     /|---|\     /|---|\    
         | M |       | M |       | M |     
         | E |       | E |       | E |     
         | S |       | S |       | S |     
         | S |       | S |       | S |     
         | A |       | A |       | A |     
         | G |       | G |       | G |     
         | E |       | E |       | E |     
        /|---|\     /|---|\     /|---|\    
       / |___| \   / |___| \   / |___| \   
       | |   | |   | |   | |   | |   | |   
    ---------------------------------------
    |   M I S S I L E   L A U N C H E R   |
    ---------------------------------------
    |   DETONATION TIMER : 20 SECONDS     |
    ---------------------------------------
    
""",
2 : """
     ________________
    |   _____________|
    |   |   _________________________________________    
    |   |      _   |                                 \   
    |   |----   |  |--------------------------------- \  
    |   |----   |--|          M E S S A G E           || 
    |   |----  _|  |--------------------------------- /  
    |   |   _______|_________________________________/   
    |   |____________
    |   _____________|_______________________
    |                                        |
    |  T O R P E D O   L A U N C H E R       |
    ------------------------------------------
    |   DETONATION TIMER : 20 SECONDS        |
    ------------------------------------------

""",
3 : """
     _________________________________________
    |  __        |     __  __                 |
    | |   __ |_| |     __||  |                |
    | |__      | |    |__ |__| S E C O N D S  |
    |____________|____________________________|
    |                    |                    |
    |   M E S S A G E    |                    |
    |                    |   M E S S A G E    |
    |____________________|____________________|
       
"""}
character_set = {
    0 : ' ',  
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd',
    5 : 'e',
    6 : 'f',
    7 : 'g',
    8 : 'h',
    9 : 'i',
    10 : 'j',
    11 : 'k',
    12 : 'l',
    13 : 'm',
    14 : 'n',
    15 : 'o',
    16 : 'p',
    17 : 'q',
    18 : 'r',
    19 : 's',
    20 : 't',
    21 : 'u',
    22 : 'v',
    23 : 'w',
    24 : 'x',
    25 : 'y',
    26 : 'z',
}
wait = time.sleep
blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print("Starting ...")
wait(1)
print(blank)
print(WELCOME_MESSAGE[random.randint(1, 3)])
input("A Scammer (Typewriter) Application [ENTER]")
print(blank)
def random_message_generator(limit: int):
    message = str()
    loop = 0
    while loop<limit:
        character = random.randint(0, 26)
        message = message+character_set[character]
        loop += 1
    return message
def scammer_random(message_limit: int, message_length_limit: int):
    print(blank)
    print(BOMBARDMENT[random.randint(1, 3)])
    print("Head towards the texting field of the application you want to send the message from."); wait(5)
    print("Message bombardment will start in 15 seconds."); wait(15)
    message_number = 0
    while message_number<message_limit:
        message: str = random_message_generator(message_length_limit)
        pyautogui.typewrite(message)
        pyautogui.press('Enter')
        message_number = message_number+1
def scammer_constant(message: str, message_limit: int):
    print(blank)
    print(BOMBARDMENT[random.randint(1, 3)])
    print("Head towards the texting field of the application you want to send the message from."); wait(5)
    print("Message bombardment will start in 15 seconds."); wait(15)
    message_number = 0
    while message_number<message_limit:
        pyautogui.typewrite(message)
        pyautogui.press('Enter')
        message_number = message_number+1
while (True):
    loop = False
    while 1==1:
        change1 = False
        print(blank)
        print("Which type of attack do you want ?")
        print("Single Message [1] / Random Message [2]")
        attack_type = input("Enter the number : ")
        wait(1)
        if attack_type=='1':
            change2 = False
            while (True):
                print(blank)
                print("You have chosen for a single message attack.")
                wait(1)
                while 1==1:
                    print("Want to change attack type?")
                    ask1 = input("Yes [Y] / No [N] : ")
                    if 'y' in ask1.lower(): change2 = True; break
                    else: break
                if change2==True: change1 = True; break
                else: pass
                message = input("Enter the message you wanna send : ")
                message_times = input("Enter how many times you wanna send the message : ")
                try: message_times = int(message_times)
                except Exception:
                    print("You have entered an invalid value. Try again.")
                    wait(2)
                    continue
                else:
                    break
            if change1==True:
                continue
            else: pass
            print("Ensure the message application you are using is open then continue.")
            input("Continue [ENTER]")
            print("Initiating Attack.")
            wait(1)
            scammer_constant(message, message_times)
        elif attack_type=='2':
            change2 = False
            while (True):
                print(blank)
                print("You have chosen for a random message attack.")
                wait(1)
                while 1==1:
                    print("Want to change attack type?")
                    ask1 = input("Yes [Y] / No [N]")
                    if 'y' in ask1.lower(): change2 = True; break
                    else: break
                if change2==True: change1 = True; break
                else: pass
                print(blank)
                wait(1)
                try:
                    message_times = int(input("Enter how many times you wanna send message : "))
                    message_limit = int(input("Enter the length of alphabets of random message : "))
                except Exception:
                    print("You have entered an invalid value. Try again.")
                    wait(2)
                    continue
                else:
                    break
            print("Ensure the message application you are using is open then continue.")
            input("Continue [ENTER]")
            print("Initiating Attack.")
            wait(1)
            scammer_random(message_times, message_limit)
        else:
            print("Try again :(")
            wait(1)
            print
            print(blank)
        print(blank)
        while 1==1:
            print("Want to attack again?")
            ask2 = input("Yes [Y] / No [N] : ")
            if 'y' in ask2.lower():
                loop = True
                break
            elif 'n' in ask2.lower():
                loop = False
                break
            else:
                print("Try Again.")
                wait(1)
                print(blank)
        if loop==True: continue
        elif loop==False: break
        else: print("Close  This Window, Code Has Crashed :(")
    print("Thanks For Using This Application.")
    wait(1)
    print("We Will Meet Soon.")
    wait(3)
    break