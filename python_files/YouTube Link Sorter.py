# Short Code to sort out all the links from a saved YouTube or YouTube Music Webpage
import time
FILE = input("Enter the main file name (*.html) : ")
PLAYLIST = input("Enter the playlist from URL i.e. links=<Playlist ID Here> : ")
OUT_FILE = input("Enter the name of the output file (*.txt) : ")
mode = None
blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
while 1==1:
    print(blank)
    print("Are you sorting a YouTube Webpage or YouTube Music Webpage ?")
    confirmation = input("YouTube Webpage [1] / YouTube Music Webpage [2] : ")
    if confirmation=='1': mode = 'YouTube'; break
    elif confirmation=='2': mode = 'YouTube Music'; break
    else: print("Try Again."); time.sleep(1)
print(blank)
time.sleep(1)
if mode=='YouTube': link_prefix = "https://www.youtube.com/watch?v="
elif mode=='YouTube Music': link_prefix = "https://music.youtube.com/watch?v="
else: print("Repair the code."); time.sleep(1); exit()
with open(f"./{FILE}.html", "r") as file:
    content = "good"
    initial = 1
    line_number = 1
    while content!="":
        try:
            content = file.readline()
        except UnicodeDecodeError as error:
            print(f"Error in Decoding at line {line_number}")
            print("Detail :-")
            print(error)
        line_number += 1
        initial_number = content.find(link_prefix)
        if initial_number==-1:
            continue
        else:
            final_number = content.find(f"list={PLAYLIST}")
            if final_number==-1:
                continue
            else:
                content_write = content[initial_number:final_number+len(PLAYLIST)+5]
                link_length = len(content_write)
                link_limit_length = len(link_prefix)+len(PLAYLIST)+30
                if link_length>link_limit_length:
                    continue
                else:
                    if initial==1: initial = 0; mode = "w"
                    else: mode = "a"
                    with open(F"./{OUT_FILE}.txt", f"{mode}") as link_file:
                        write_content = content_write+"\n"
                        link_file.write(write_content)
    else:
        time.sleep(1)
        print(blank)
        print("Done Finding Links")
time.sleep(1)
print("Modifying Links.")
time.sleep(1)
content = "good"
with open(f"./{OUT_FILE}.txt", "r") as file:
    content = file.read()
while (True):
    content = content.replace("&amp;", "&")
    if "&amp;" in content:
        continue
    else:
        break
with open(f"./{OUT_FILE}.txt", "w") as file:
    file.write(content)
print("Done"); time.sleep(1)
print("Checking For Duplicate Links."); time.sleep(1)
duplicate_link_count = 0
links_list = []
content = 'something'
with open(f"./{OUT_FILE}.txt", "r") as file:
    while content!="":
        content = file.readline()
        links_list.append(content)
for main_index in range(len(links_list)):
    main_link = links_list[main_index]
    for clone_index in range(len(links_list)):
        clone_link = links_list[clone_index]
        if clone_link==main_link:
            if main_index==clone_index: pass
            else: duplicate_link_count += 1
if duplicate_link_count==0:
    print("There Were No Duplicate Links."); time.sleep(1)
else:
    print(f"{duplicate_link_count} Duplicate Links Found, Modifying File."); time.sleep(1)
    links_set = set()
    content = 'file'
    with open(f"./{OUT_FILE}.txt", "r") as file:
        while content!="":
            content = file.readline()
            links_set.add(content)
    links_list = list(links_set)
    for index in range(len(links_list)):
        if index==0: mode = "w"
        else: mode = "a"
        with open(f"./{OUT_FILE}.txt", f"{mode}") as file:
            file.write(links_list[index])
    print("Removed Duplicate Links From The File."); time.sleep(1)
print(blank)
print("All Done."); time.sleep(1)
print("Links were written to file : %s.txt" % (OUT_FILE)); time.sleep(3)