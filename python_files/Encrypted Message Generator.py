# Encrypted Message Generator
import time
import random
import os
blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
character_set = {
    't' : 0, 'E' : 1, 'J' : 2, '0' : 3, 'Y' : 4, '1' : 5, ' ' : 6, '5' : 7, 'q' : 8, 'r' : 9, 'T' : 10, 
    'S' : 11, 'K' : 12, 'Q' : 13, 'v' : 14, 'D' : 15, 'X' : 16, 'F' : 17, 'h' : 18, 'H' : 19, 'f' : 20, 
    'G' : 21, 'a' : 22, 'R' : 23, '2' : 24, 'B' : 25, '6' : 26, 'U' : 27, 'l' : 28, 's' : 29, '4' : 30, 
    'A' : 31, '9' : 32, 'd' : 33, 'j' : 34, 'x' : 35, 'k' : 36, 'N' : 37, 'i' : 38, 'Z' : 39, 'c' : 40, 
    'W' : 41, 'P' : 42, 'e' : 43, 'I' : 44, '3' : 45, 'm' : 46, 'b' : 47, 'u' : 48, 'o' : 49, 'p' : 50, 
    'g' : 51, 'V' : 52, 'C' : 53, 'L' : 54, 'y' : 55, 'w' : 56, '7' : 57, 'O' : 58, 'M' : 59, 'z' : 60, 
    '8' : 61, 'n' : 62, 
}
reverse_character_set = """character_set = {
    0 : 't', 1 : 'E', 2 : 'J', 3 : '0', 4 : 'Y', 5 : '1', 6 : ' ', 7 : '5', 8 : 'q', 9 : 'r', 10 : 'T',
    11 : 'S', 12 : 'K', 13 : 'Q', 14 : 'v', 15 : 'D', 16 : 'X', 17 : 'F', 18 : 'h', 19 : 'H', 20 : 'f',
    21 : 'G', 22 : 'a', 23 : 'R', 24 : '2', 25 : 'B', 26 : '6', 27 : 'U', 28 : 'l', 29 : 's', 30 : '4',
    31 : 'A', 32 : '9', 33 : 'd', 34 : 'j', 35 : 'x', 36 : 'k', 37 : 'N', 38 : 'i', 39 : 'Z', 40 : 'c',
    41 : 'W', 42 : 'P', 43 : 'e', 44 : 'I', 45 : '3', 46 : 'm', 47 : 'b', 48 : 'u', 49 : 'o', 50 : 'p',
    51 : 'g', 52 : 'V', 53 : 'C', 54 : 'L', 55 : 'y', 56 : 'w', 57 : '7', 58 : 'O', 59 : 'M', 60 : 'z',
    61 : '8', 62 : 'n',
}
"""
character_set_string = str(character_set)
message = []
encrypted_message = []
cipher_code = []
welcome_message = """
  ### ##### ####  ##  ####   ###  #####   \n ##   ##    ## ## ## ##     ## ## ##  ##  \n ##   ####  ## ## ##  ####  ## ## #####   \n ##   ##    ## ## ##     ## ## ## ##  ##  \n  ### ##### ##  ####  ####   ###  ##   ## 

"""
def static_cipher_generator() -> list:
    global cipher_code
    cipher_code_temp = []
    global restart_status
    cipher_index = 0
    help_message = "This is a numeric Cipher, so you have to enter just numbers (Max Digits : 10)\nTpe 'help' to display this message"
    print(blank); print(help_message)
    while cipher_index<10:
        if restart_status==True: break
        else: pass
        temp_cipher = input(f"Enter Cipher Number {cipher_index+1} : ")
        if len(str(temp_cipher))>10:
            print(blank); print("You have entered a number with digits count exceeding 10.")
            print(help_message); input("Press ENTER[RETURN] to continue..."); print(blank)
            continue
        elif temp_cipher=='help':
            print(blank); print(help_message); input("Press ENTER[RETURN] to continue..."); print(blank)
            continue
        else:
            try:
                int(temp_cipher)
            except Exception:
                print(blank); print("You have entered an invalid value, please try again.")
                print(help_message); input("Press ENTER[RETURN] to continue..."); print(blank)
                continue
            else:
                selector = random.randint(1, 2)
                if selector==1: cipher_temp = +(int(temp_cipher))
                elif selector==2: cipher_temp = -(int(temp_cipher))
                cipher_code_temp.append(cipher_temp)
                cipher_index += 1
    print("Generating Cipher Code"); time.sleep(1)
    cipher_code = cipher_code_temp.copy()
    print("Done."); time.sleep(0.5)
def random_cipher_generator() -> list:
    global cipher_code
    print("Generating Cipher Code...")
    time.sleep(1)
    code_index = 0
    while code_index<10:
        cipher = random.randint(-1000, 1000)
        cipher_code.append(cipher)
        code_index+=1
    print("Done."); time.sleep(0.5)
def message_encrypter() -> list:
    global cipher_code
    cipher_suite = cipher_code
    global message
    for character in range(len(message)):
        index = character % 10
        if index==0: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==1: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==2: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==3: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==4: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==5: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==6: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==7: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==8: encrypted_message.append(message[character]+(cipher_suite[index]))
        elif index==9: encrypted_message.append(message[character]+(cipher_suite[index]))
        else: print("This code failed."); time.sleep(5); exit()
decrypter = """decrypted_message = []
for character in range(len(message)):
    index = character % 10
"""
file_deleter = """self_destruction_status = False\ncwd = os.getcwd()\nfolders_and_files = os.listdir(cwd)\nfiles = []\nfor index in range(len(folders_and_files)):\n        name = folders_and_files[index]
        if ".py" in name: files.append(name)\n        else: pass\nif "Message.py" in files: os.remove(cwd+"\\\\Message.py"); self_destruction_status = True;  print("File Self Destructed.")\nelse:\n    for index in range(len(files)):
        file_name = cwd+"\\\\"+files[index]\n        with open(file_name, "r") as file:comment = file.read()\n        if "# Encrypted Message Decrypter".lower() in comment.lower():\n            if "# Encrypted Message Generator" in comment: pass\n            else: os.remove(file_name); self_destruction_status = True
        elif "(message[character]+(cipher_code[index]))" in comment:\n            if "# Encrypted Message Generator" in comment: pass\n            else:  os.remove(file_name); self_destruction_status = True\n        else: pass
    else:\n        if self_destruction_status==False: print("Self Destruction Failed.")\n        else: print("File Self Destructed.")\ntime.sleep(1)
"""
def reverse_cipher_code_generator(cipher_code_suite: list) -> str:
    index = 0
    reverse_cipher_suite = []
    while index<10:
        reverse_cipher_suite.append(int(str(-(cipher_code_suite[index]))))
        index += 1
    return str(reverse_cipher_suite)+"\n"
while 1==1:
    exit_status = False
    restart_status = False
    print(blank)
    print(welcome_message)
    print("Welcome To Encrypted Message Generator.")
    input("Press ENTER[RETURN]...")
    print(blank)
    print("You will be asked for your message and a numeric code to encrypt your message.")
    print("Type 'restart' to restart the application.")
    input("ENTER[RETURN] to continue...")
    print(blank)
    while True:
        print(blank)
        print("Message should consist only of alphabets and numbers")
        temp_message = input("Enter Your Message : ")
        if temp_message=='restart': restart_status = True; break
        elif temp_message=="": print("Please Type A Message."); time.sleep(3); print(blank); continue
        else: pass
        try:
            for character_index in range(len(temp_message)):
                message.append(character_set[temp_message[character_index]])
        except KeyError:
            print("There was a character in the message other than alphabets and numbers.")
            print("Try Again")
            time.sleep(5)
            continue
        else:
            break
    if restart_status==True: continue
    else: pass
    print("Now its time to encrypt your message")
    time.sleep(2)
    while True:
        cipher_mode = 0
        while 1==1:
            print(blank)
            print("Want to give a cipher code or build random?")
            ask1 = input("Give A Code [1] / Random Code [2] : ")
            if ask1=='restart': restart_status = True; break
            elif ask1=='1': cipher_mode = 1; break
            elif ask1=='2': cipher_mode = 2; break
            else: print("Try again")
        if restart_status==True: break
        else: pass
        if cipher_mode==1: static_cipher_generator(); break
        elif cipher_mode==2: random_cipher_generator(); break
        else: print("Code Crashed!"); time.sleep(1); exit()
    print(blank)
    if restart_status==True: continue
    else: pass
    print("Encrypting Your Message."); time.sleep(1); message_encrypter(); print("Done."); time.sleep(0.5); print(blank)
    print("Starting File Generator..."); time.sleep(1)
    print("Creating file 'Message.py' ..."); time.sleep(1)
    current_working_directory = os.getcwd()
    with open(f"{current_working_directory}\\Message.py", "w") as file:
        print("You can't restart this application here.")
        input("Press ENTER[RETURN] to continue...")
        print(blank)
        file.write("# Encrypted Message Decrypter\n")
        file.write("import os\nimport time\n")
        file.write(reverse_character_set)
        self_deletion = False
        while 1==1:
            print(blank)
            print("Want to Enable Self Destruction ?")
            ask2 = input("Yes [1] / No [2] : ")
            if ask2=='1':
                self_deletion = True; break
            elif ask2=='2':
                self_deletion = False; break
            else:
                print("Try Again.")
                time.sleep(1)
        while 11==11:
            print(blank)
            print("How many seconds do you want the message to appear ?")
            print("(Leave blank and hit ENTER[RETURN] to set the default value i.e. 5 seconds.)")
            ask3 = input("Enter the number of seconds : ")
            if ask3=="": time_value = 5.0; break
            else:
                try: float(ask3)
                except Exception:
                    print(blank)
                    print("You can only type number (can be a decimal number).")
                    print("Try again")
                    input("Press ENTER[RETURN] to continue...")
                    continue
                else: time_value = float(ask3); break
        print(blank)
        reverse_cipher = f"cipher_code = {reverse_cipher_code_generator(cipher_code)}"; file.write(reverse_cipher)
        message_decrypt = f"message = {encrypted_message}\n"; file.write(message_decrypt); file.write(decrypter)
        for index in range(10):
            start = f"if index=={index}: " if index==0 else "else: " if index==10 else f"elif index=={index}: "
            main = "print('This code failed.'); " if index==10 else "decrypted_message.append"
            end = "exit()" if index==10 else "(message[character]+(cipher_code[index]))"
            string = "    "+start+main+end+"\n"
            file.write(string)
        message_list = "message_list = []\n"; file.write(message_list)
        decrypted_message_convertor = "for index in range(len(decrypted_message)):\n    message_list.append(character_set[decrypted_message[index]])\n"; file.write(decrypted_message_convertor)
        message_string_maker = 'message_string = "".join(message_list)\n'; file.write(message_string_maker)
        if self_deletion==True: file.write(file_deleter)
        else: pass
        viewer_and_timer = f"print(message_string); time.sleep({time_value})\n"; file.write(viewer_and_timer)
    print("Finishing File..."); time.sleep(1); print("Done!"); time.sleep(1)
    while True:
        print("Want to restart application ?")
        ask4 = input("Yes [1] / No [2] : ")
        if ask4=='1':
            print(blank)
            message_for_file = "If you want to send that file named 'Message.py', send it,\nIf you want to save that file, rename it or place the file in a new folder or other folder,\nIf that file is required no more,\nDelete it or keep as it is because a new file with same file name will be created"
            print(message_for_file)
            input("Press ENTER[RETURN] to continue...")
            print(blank)
            restart_status = True
            break
        elif ask4=='2': restart_status = False; print(blank); break
        else: print("Try again."); time.sleep(2); print(blank)
    if restart_status==True: continue
    elif restart_status==False: print(blank); print("Thanks For Using This Application :)"); time.sleep(3); break
    else: print(blank); print("Repair the code"); time.sleep(3)