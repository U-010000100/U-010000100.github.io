# Short code to download any video from YouTube or YouTube Music
try:
    from pytube import YouTube
except ModuleNotFoundError:
    print("Pytube is not installed on your computer.\nOpen a command window and copy the following command in it:-")
    print("python -m pip install pytube")
else:
    try: import delay
    except ModuleNotFoundError:
        import datetime
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
        delay_ = one_second_delay
    else:
        delay_ = delay.one_second_delay
    blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    while 1==1:
        exit_status = 0
        links = []
        print("Welcome To The Downloader!"); delay_()
        print("Enter the link or path of the file")
        print("Links must start with 'https' or 'youtube'")
        print("if the file is given, it must be named as 'links.txt' (case-sensitive) and in the same folder containing the python file.")
        print("(Hit enter when you are done.)")
        input("ENTER[RETURN] To Continue...")
        print(blank)
        while True:
            ask2 = input("Enter : ")
            if ask2.startswith('e')==True or ask2.startswith('q')==True:
                exit_status = 1
                break
            elif ask2.startswith('http'): links.append(ask2)
            elif ask2.startswith('youtube')==True: links.append("https://www."+ask2)
            elif ask2.startswith('music'): ask2.removeprefix('music'); links.append("https://www.youtube"+ask2)
            elif ask2.startswith('www'): links.append("https://"+ask2)
            elif ask2=="": break
            else:
                if ask2.find('links.txt')!=-1:
                    with open(ask2, 'r') as file:
                        content = 'content'
                        while True:
                            content = file.readline()
                            if content!=None and content!='': links.append(content)
                            else: break
                else: print("There was no link or correct file name provided.\nEither check the file name or the folders.\nEnsure this file is in the same folder containing your 'links.txt' file"); input("Press ENTER[RETURN] To Continue..."); print(blank)
        if exit_status==1: break
        else: pass
        total_items = len(links)
        resolution = ''
        while 1==1:
            print("Which resolution do you want?")
            ask3 = input("(Highest [1] / Lowest [2]) : ").lower()
            if ask3=='1' or ask3.find('h')!=-1: resolution = 'highest'; break
            elif ask3=="2" or ask3.find('l')!=-1: resolution = 'lowest'; break
            elif ask3.startswith('e') or ask3.startswith('q'): exit_status = 1; break
            else: print("Try again.")
        if exit_status==1: break
        else: pass
        if resolution=='highest':
            print("Starting Download..."); delay_()
            for number, link in enumerate(links):
                number += 1
                print("Downloading item %s of %s" % (number, total_items)+'...')
                item = YouTube(link)
                item_ = item.streams.get_highest_resolution()
                activate = item_.download()
        elif resolution=='lowest':
            print("Starting Download..."); delay_()
            for number, link in enumerate(links):
                number += 1
                print("Downloading item %s of %s" % (number, total_items)+'...')
                item = YouTube(link)
                item_ = item.streams.get_lowest_resolution()
                activate = item_.download()
        else:
            print("There was some issue in your input, try again")
        print(blank,f"Downloaded {total_items} item(s).")
        delay_()
        break
print("Thanks for using this software."); delay_(); delay_(); delay_()