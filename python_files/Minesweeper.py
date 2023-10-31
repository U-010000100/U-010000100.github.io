# MineSweeper
from time import sleep
from random import randint
grid_characters = {
    "v" : "│", "h" : "─", "m" : "┼", "rvh" : "┤",
    "lvh" : "├", "thv" : "┬", "bhv" : "┴",
    "lr" : "┘","ul" : "┌", "ll" : "└","ur" : "┐",
}
def flags_remaining() -> int:
    """Returns the value of remaining flags, this function subtracts the flag count from mine count"""
    global flagged_blocks; global mines_location
    return ((len(mines_location))-(len(flagged_blocks)))
main_grid = """"""
format_characters = list(); grid_size = tuple(); mined_blocks = list(); flagged_blocks = list(); mines_location = []; step = tuple()
def blank() -> None:
    """Gives a blank space to the screen"""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def mine_counter(number: int) -> int :
    """Returns the number of mines to be placed in grid according to grid size"""
    if number==100: return 15
    elif number==270: return 40
    elif number==500: return 80
    elif number==800: return 125
    else:
        count = number//7
        return count
def value_reassigner() -> None:
    """Clears the value of variables"""
    global grid_size; grid_size = ""; grid_size = tuple()
    global mined_blocks; mined_blocks.clear()
    global mines_location; mines_location.clear()
    global flagged_blocks; flagged_blocks.clear()
    global step; step = ""; step = tuple()
    global main_grid; main_grid = """"""
    global format_characters; format_characters.clear()
def exit_handler()-> None :
    """Shows the exit message and terminates the code"""
    blank(); print("Thanks for playing, hope we will meet soon."); sleep(3); blank(); exit()
def grid_blueprint() -> None :
    """Assigns the grid size and calls the grid maker function"""
    global grid_size
    while 1==1:
        blank(); print("Set your level of difficulty."); sleep(1)
        print("Easy    : 10*10 [1]")
        print("Medium  : 18*15 [2]")
        print("Hard    : 25*20 [3] (Enter Fullscreen window)")
        print("Extreme : 40*20 [4] (Enter Fullscreen Window)")
        print("Custom  : x*y   [5]")
        level = input("Enter the number for selection : ")
        if level.lower()=="exit": exit_handler()
        else: pass
        try: level = int(level)
        except ValueError: print("Enter the number only."); sleep(2); continue
        else:
            if level>0 and level<6: pass
            else: print("Enter the given number only."); sleep(2); continue
        con_val = False
        while (True):
            blank(); print("Your are choosing {} grid, continue?".format("Easy (10*10)" if level==1 else "Medium (18*15)" if level==2 else "Hard (25*20)" if level==3 else "Extreme (40*20)" if level==4 else "Custom (Value selection ahead)"))
            confirmation = input("[Y/N] : ")
            if confirmation.lower().find('n')!=-1:
                print("Change the difficulty."); sleep(1); blank()
                con_val = True; break
            elif confirmation.lower().find("y")!=-1: break
            elif confirmation.lower()=="exit": exit_handler()
            elif confirmation=="": print("Please enter a value."); sleep(2)
            else: pass
        if con_val==True: continue
        else: break
    if level==1: value1 = 10; value2 = 10
    elif level==2: value1 = 18; value2 = 15
    elif level==3: value1 = 25; value2 = 20
    elif level==4: value1 = 40; value2 = 20
    else:
        while 1==1:
            blank(); print("Enter the size of the grid you want. (In next step)"); sleep(2)
            while 1==1:
                blank(); value1 = input("Enter the number of columns [x-coordinate limit or x-value] (from 6 to 20) : ")
                try: value1 = int(value1)
                except ValueError: print("Enter only number."); sleep(2); continue
                else: 
                    if value1>=6 and value1<=20: break
                    elif value1=="": print("Please Enter a value."); sleep(2)
                    else: print("Remember the limit written along, try again."); sleep(2); continue
            while 1==1:
                blank(); value2 = input("Enter the number of rows [y-coordinate limit or y-range] (from 6 to 20) : ")
                try: value2 = int(value2)
                except ValueError: print("Enter only number"); sleep(2); continue
                else: 
                    if value2>=6 and value2<=20: break
                    elif value2=="": print("Please Enter a value."); sleep(2)
                    else: print("Remember the limit written along, try again."); sleep(2); continue
            blank(); print("The size of grid is {}*{}, correct?".format(value1, value2))
            confirmation = input("[Y/N] : ")
            if confirmation.lower().find("y")!=-1: break
            elif confirmation.lower().find("n")!=-1: print("Enter the correct size this time."); sleep(1);  continue
            elif confirmation.lower()=="exit": exit_handler()
            else: pass
    grid_size = (value1, value2); grid_maker(grid_size[0], grid_size[1])
    print("Be Carefull :)"); sleep(2); blank(); print("Enjoy"); sleep(1); blank()
def grid_maker(x: int, y: int) -> None :
    """Constructs the grid from its assigned size"""
    global grid_characters; global main_grid; global format_characters
    for row in range(y+1):
        mid_range_1 = 3 if row==y else 2
        for row_line in range(1, mid_range_1+1):
            for column in range(x+1):
                mid_range_2 = 2 if column==x else 1
                for column_line in range(1, mid_range_2+1):
                    if column_line==1:
                        if column==0 or (row_line==2 and row>0): left_character = " "
                        elif column >0 and (row_line==1 or row_line==3): left_character = grid_characters["h"]
                        elif row==0 and row_line==2:
                            if column>10: left_character = str(column-1)[1]
                            else: left_character = " "
                        else: pass
                        if row==0 and row_line==1 and column==0: middle_character = grid_characters["ul"]
                        elif column==0 and row_line==3 and row==y: middle_character = grid_characters["ll"]
                        elif column==0 and row>0 and row_line==1: middle_character = grid_characters["lvh"]
                        elif row==0 and row_line==1 and column>0: middle_character = grid_characters["thv"]
                        elif row==y and row_line==3 and column>0: middle_character = grid_characters["bhv"]
                        elif row>0 and row_line==1 and column>0: middle_character = grid_characters["m"]
                        elif row_line==2: middle_character = grid_characters["v"]
                        else: pass
                        if (row_line==1 or row_line==3): right_character = grid_characters["h"]
                        elif row_line==2 and column>0: right_character = " "
                        elif column==0 and row_line==2:
                            if row>=10: right_character = str(row)[0]
                            else: right_character = " "
                        else: right_character = " "
                        if row_line==1 or row_line==3: fill_character = grid_characters["h"]
                        else:
                            if row==0 and row_line==2:
                                if column==0: fill_character = " "
                                else: fill_character = str(column)[0]
                            elif row>0 and column==0 and row_line==2:
                                if row<10: fill_character = str(row)
                                elif row>=10: fill_character = str(row)[1]
                            elif row_line==2 and row>0 and column>0: fill_character = "%s"
                            else: pass
                    elif column_line==2:
                        fill_character = "\n"; right_character = " "
                        if row_line==1 or row_line==3:
                            left_character = grid_characters["h"]
                            if row==0 and row_line==1: middle_character = grid_characters["ur"]
                            elif row_line==3: middle_character = grid_characters["lr"]
                            else: middle_character = grid_characters["rvh"]
                        elif row_line==2:
                            if row==0 and column>=10: left_character = str(column)[1]
                            else: left_character = " "
                            middle_character = grid_characters["v"]
                        else: pass
                    else: pass
                    grid_building_block = left_character+middle_character+right_character+fill_character
                    main_grid = main_grid+grid_building_block
    format_characters_count = x*y; count = 0
    while count<format_characters_count:
        format_characters.insert(-1, " "); count += 1
def digger_extension(value: str) -> str :
    """Extenstion function of digger to differentiate all non-blank values"""
    values = list(); temp = str()
    for index in range(len(value)):
        if value=="": pass
        elif value[index]==" ": values.append(temp); temp = ""
        elif value[index]!=" ":
            temp += value[index]
            if index==(len(value)-1): values.append(temp)
            else: pass
        else: pass
    else:
        try:
            while True: values.remove("")
        except ValueError: pass
        return values
def digger(size: tuple) -> int :
    """Function to handle the grid blocks by user input"""
    global flagged_blocks; global mined_blocks; global step; global mines_location
    print(f"Flags remaining : {flags_remaining()}")
    temp = input("[F : Flag / M : Mine <Space> X-Value <Space> Y-Value] : ")
    if temp=="exit": exit_handler()
    else: values = digger_extension(temp)
    if len(values)!=3:
        if len(values)<3: return 1.25
        elif len(values)>3: return 1.75
        else: return 1
    else:
        action = values[0].lower(); x = values[1]; y = values[2]
        if action!="m":
            if action!="f": return 2
            else: pass
        else: pass
        try: x = int(x); y = int(y)
        except ValueError: return 2
        else:
            if x>size[0] or y>size[1]: return 3
            else:
                if x<1 or y<1: return 4
                else:
                    step = (x, y)
                    if action=="m" and mined_blocks==[]:
                        flagged_blocks = []
                        for index in range(len(format_characters)):
                            format_characters[index] = " "
                        mine_locator(step, "place"); mined_blocks.append(step); return 0
                    elif (step in flagged_blocks) and action=="m":
                        while (True):
                            print("The block is flagged, proceed to mine it?")
                            confirmation = input("[Y/N] : ")
                            if confirmation.lower().find("y")!=-1:
                                flagged_blocks.remove(step)
                                if (step in mines_location) and action=="m": return 7
                                else: mined_blocks.append(step); return 0
                            elif confirmation.lower().find("n")!=-1: return 5
                            else: return 5
                    elif (step in flagged_blocks) and action=="f":
                        while True:
                            print("The block is flagged, unflag it ?")
                            confirmation = input("[Y/N] : ")
                            if confirmation.lower().find("y")!=-1:
                                flagged_blocks.remove(step); return 0
                            elif confirmation.lower().find("n")!=-1: return 5
                            else: return 5
                    elif (step in mined_blocks) and action=="f": return 7
                    elif (step not in mined_blocks) and action=="f": flagged_blocks.append(step); return 0
                    elif (step in mines_location) and action=="m": return 8
                    elif (step in mined_blocks) and action=="m": return 9
                    elif (step not in mined_blocks) and action=="m": mined_blocks.append(step); return 0
                    else: return 10
def coordiante_handler(coordiante: tuple, block_location: int, limits: tuple) -> list :
    """Returns the coordinates of surrounding blocks of a particukar block"""
    if block_location==1: new_coordinate = (coordiante[0]-1, coordiante[1]-1)
    elif block_location==2: new_coordinate = (coordiante[0], coordiante[1]-1)
    elif block_location==3: new_coordinate = (coordiante[0]+1, coordiante[1]-1)
    elif block_location==4: new_coordinate = (coordiante[0]-1, coordiante[1])
    elif block_location==5: new_coordinate = (coordiante[0]+1, coordiante[1])
    elif block_location==6: new_coordinate = (coordiante[0]-1, coordiante[1]+1)
    elif block_location==7: new_coordinate = (coordiante[0], coordiante[1]+1)
    elif block_location==8: new_coordinate = (coordiante[0]+1, coordiante[1]+1)
    else: print("Unknown error, Error Code : coordinate_handler"); sleep(3); exit()
    x = new_coordinate[0]; y = new_coordinate[1]; return_value = []
    if x==0 or x>limits[0] or y==0 or y>limits[1]: return_value.append(1)
    else: return_value.append(0); return_value.append(new_coordinate)
    return return_value
def blocks_handler_extension(coordinate: tuple) -> list:
    """Extension of blocks handler
    Returns the number of mine surrounding a particular block and surrounding empty blocks"""
    global mines_location; global grid_size; empty_blocks = []
    x = coordinate[0]; y = coordinate[1]; mine_count = 0
    for count in range(1, 9):
        value = coordiante_handler((x, y), count, grid_size)
        if value[0]==1: continue
        elif value[0]==0: pass
        else: print("Unknown error, Error Code : coordinate_handler"); sleep(3); exit()
        block = value[1]
        if block in mines_location: mine_count += 1
        else: empty_blocks.append(block)
    else:
        if mine_count!=0: empty_blocks = []
        else: pass
        return [mine_count, empty_blocks]
def blocks_handler(coordinate: tuple, status: str, action_flag: int) -> None:
    """Handles the values of the grid blocks"""
    global mines_location; global mined_blocks; global format_characters; global grid_size
    number = 1 if len(mined_blocks)==1 else 0
    mining_list = []; coordinate_list = [coordinate]; blocks = set(); blocks_copy = set(); blocks_update = []
    if len(mined_blocks)==1: multiple_mining = True
    else: multiple_mining = False
    while len(coordinate_list)!=0:
        temp = coordinate_list[0]; coordinate_list.remove(temp); mining_list.append(temp)
        if status=="M":
            cache = blocks_handler_extension(temp)
            number = cache[0]
            if number==0: multiple_mining = True
            else: pass
            if multiple_mining==True:
                blocks_copy = blocks.copy()
                for index in range(len(cache[1])): blocks.add(cache[1][index])
                else:
                    if len(blocks)==len(blocks_copy): pass
                    else:
                        blocks = list(blocks); blocks_copy = list(blocks_copy)
                        for index in range(len(blocks)):
                            if blocks[index] not in blocks_copy: blocks_update.append(blocks[index])
                            else: pass
                        else:
                            blocks = set(blocks)
                            for index in range(len(blocks_update)): coordinate_list.append(blocks_update[index])
            else: pass
            if number==0: number = "-"
            else: number = str(number)
        elif status=="F":
            if action_flag==1: number = "?"
            elif action_flag==2: number = " "
            else: print("Code needs to be repaired, Error : Blocks Handler")
        else: pass
        x = temp[0]; y = temp[1]
        block = (((y-1)*grid_size[0])+x)-1
        format_characters[block] = number
    else:
        if len(mining_list)==1: pass
        else:
            mining_list.remove(coordinate); mining_set = set(mining_list); mining_list = list(mining_set)
            for index in range(len(mining_list)): mined_blocks.append(mining_list[index])
def mine_locator(mined_location: tuple, action: str) -> None:
    """Places the mines in random blocks"""
    global mines_location; global flagged_blocks; global grid_size; global format_characters
    size = grid_size; abscissa = size[0]; ordinate = size[1]
    if action=="place":
        flagged_blocks = []; mine_blocks = [mined_location]
        for index in range(1, 9):
            additional_block_cache = coordiante_handler(mined_location, index, grid_size)
            if additional_block_cache[0]==1: pass
            else: mine_blocks.append(additional_block_cache[1])
        blocks = abscissa*ordinate; mine_count = mine_counter(blocks); count = 0
        while count<mine_count:
            x = randint(1, abscissa); y = randint(1, ordinate)
            if (x, y) in mine_blocks or (x, y) in mines_location: continue
            else: mines_location.append((x, y)); count += 1
    elif action=="reveal":
        total_flags = len(flagged_blocks)
        correct_flags = 0
        incorrect_flags = 0
        mines_count = len(mines_location)
        for count in range(mines_count):
            coordinate = mines_location[count]
            if coordinate in flagged_blocks: correct_flags += 1; flagged_blocks.remove(coordinate)
            else: x = coordinate[0]-1; y = coordinate[1]-1; block = x+(y*size[0]); format_characters[block] = "*"
        else:
            count = len(flagged_blocks)
            if count==0: pass
            else:
                incorrect_flags = count
                for index in range(count):
                    coordinate = flagged_blocks[index]
                    x = coordinate[0]-1; y = coordinate[1]-1; block = x+(y*size[0])
                    format_characters[block] = "X"
                else: pass
            return [total_flags, correct_flags, incorrect_flags]
    else: pass
def game_over(coordinate: tuple, status: str) -> None:
    """Gameover function, 
    Called when player has lost or won"""
    global format_characters
    value = mine_locator(coordinate, "reveal")
    print(main_grid % tuple(format_characters))
    if status=="lost": print("Stepped on a mine *")
    elif status=="won": print("All Mines Found !")
    else: print("unknown error."); print("Error Code : game_over"); sleep(3); exit()
    print(f"Flags used : {value[0]}   Correct Flags : {value[1]}   Incorrect Flags : {value[2]}"); sleep(1)
    print("Game Over."); sleep(3)
    restart_value = False
    while True:
        blank(); ask = input("Play Again ? [Y/N] : ")
        if ask.lower().find('y')!=-1: restart_value = True; break
        elif ask.lower().find('n')!=-1: break
        else: print("Try Again."); sleep(2)
    if restart_value==False: exit_handler()
    elif restart_value==True: value_reassigner()
def verifier() -> int:
    """Verifies the blocks for victory of player"""
    global flagged_blocks; global format_characters; global mines_location; global grid_size
    mines_location_copy = mines_location.copy()
    flagged_locations = flagged_blocks.copy()
    return_value = 1
    if len(flagged_locations)==0: pass
    else:
        for count in flagged_blocks:
            if count in mines_location_copy: mines_location_copy.remove(count); flagged_locations.remove(count)
            else: break
        else:
            if len(flagged_locations)!=0: pass
            else:
                blocks_remaining = format_characters.count(" ")
                if mines_location_copy==0 and blocks_remaining==0: return_value = 0
                else:
                    mines_remaining = len(mines_location_copy)
                    if mines_remaining!=blocks_remaining: pass
                    else:
                        for coordinate in mines_location_copy:
                            x = coordinate[0]; y = coordinate[1]
                            block = (((y-1)*grid_size[0])+x)-1
                            if format_characters[block]==" ": pass
                            else: break
                        else: return_value = 0
    return return_value
first_time = True
while (True):
    # Main execution code
    if first_time==True:
        first_time = False
        blank(); print("Welcome To Classic Minesweeper."); sleep(2); blank()
        print("You have to flag the mines, but careful, one wrong step can take you blown away :)"); sleep(3)
        print("Get ready."); sleep(1)
    elif first_time==False:
        ask = input("Show intro ? [Y / N or ENTER] : ")
        if ask.lower().find('y')!=-1: first_time = True; continue
        elif ask.lower()=="exit": exit_handler()
        else: pass
    else: pass
    blank(); grid_blueprint()
    while 1==1:
        blank(); flagged_blocks_copy = flagged_blocks.copy(); mined_block_copy = mined_blocks.copy()
        print(main_grid % tuple(format_characters))
        error = digger(grid_size); blank()
        if error==1 or error==1.25: print("You have given an insufficient value to proceed, try again."); sleep(3); continue
        elif error==1.75: print("You have given more values than required, try agaib."); sleep(2); continue
        elif error==2: print("You have given an invalid value, try again."); sleep(2); continue
        elif error==3: print("You have given value(s) that exceeds grid size, try again."); sleep(2); continue
        elif error==4: print("You have entered value that are not in the grid, try again."); sleep(2); continue
        elif error==5: print("Try again"); sleep(1); continue
        elif error==6: print("The block is already flagged, try another one."); sleep(2); continue
        elif error==7: print("The block is mined already, try another one."); sleep(2); continue
        elif error==8: game_over(step, "lost"); break
        elif error==9: print("The block is already mined, try another one."); sleep(2); continue
        elif error==10: print("Unknown error, try again"); sleep(2); continue
        elif error!=0: print("Code needs to be repaired, Error : Digger"); sleep(2); exit()
        else:
            if len(flagged_blocks_copy)<len(flagged_blocks): action = "F"; flag_action = 1
            elif len(mined_block_copy)<len(mined_blocks): action = "M"; flag_action = 0
            elif len(flagged_blocks)<len(flagged_blocks_copy): action = "F"; flag_action = 2
            else: print("Code needs to be repaired, Error : Digger"); sleep(3); exit()
            value = step; blocks_handler(value, action, flag_action); value = verifier()
            if value==1: pass
            elif value==0: game_over(step, "won"); break
            else: print("Unknown Error, Error Code : verifier"); sleep(3); exit()
