import datetime
from os import getcwd
import playsound
import time
print("A small alarm (Ensure volume and directories).")
print("It can use a fix time or a time duration to work.")
time.sleep(1)
print("What do you want to use?\nAn Alarm [1]\n     OR     \nA Timer  [2]")
t_or_a = input("Enter the number only : ")
h = '0' ; m = '0' ; s = '0'
while True:
    print("Enter time of 24-hour format for alarm (Ensure two digit number).")
    h = input("Hours   : ")
    m = input("Minutes : ")
    s = input("Seconds : ")
    if len(h)==2 and len(m)==2 and len(s)==2:
        break
    else:
        print("Try again."); time.sleep(1); print("\n\n")
def alarm(h : str, m : str ,s : str):
    print("Alarm Activated for time : {}:{}:{}".format(h, m, s))
    cwd = getcwd()
    while True:
        time_ = datetime.datetime.today()
        time__ = str(time_)
        c_time = time__[11:19]
        g_time = "{}:{}:{}".format(h, m, s)
        if c_time==g_time:
            print("Time to wake up!")
            while 1==1:
                playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
                playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
                playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
                print("Repeating sound in 10 seconds. (Use CTRL+C to stop alarm)")
                time.sleep(10)
        else:
            continue
def timer(h : str, m : str ,s : str):
    h_s = int(h)*60*60
    m_s = int(m)*60
    s_s = int(s)
    t_s = h_s + m_s + s_s
    t_s_ = int(t_s)
    print("Alarm activated for {} hours, {} minutes and {} seconds from now.".format(h, m, s))
    cwd = getcwd()
    time.sleep(t_s_)
    print("Time to wake up!")
    while 1==1:
        playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
        playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
        playsound.playsound(f"{cwd}/Alarm_audio/alarm.mp3")
        print("Repeating sound in 10 seconds. (Use CTRL+C to stop alarm)")
        time.sleep(10)
alarm(h, m, s) if t_or_a=='1' else timer(h, m, s) if t_or_a=='2' else print("Try again.")