import pyautogui as gui
import pytesseract
import time
from coordinates import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
# change the location the the exe file of tesseract.exe accordingly

Typing_Bolt = (19, 209, 1300, 40)  #for ex. (x, y, a, b)
# where x an y is the coordinate of the top left most part of the text area and a and b are the width and length distanch from that point.

def capture(region):
    img = gui.screenshot(region=region)
    img.save('screenshot.png')
    return img 

def predict(img):
    text = str(pytesseract.image_to_string(img))
    #print(text,  file=open('log.txt', 'w'))
    return text

def write_text(text):
    gui.write(text, interval=.05) # interval = the time seperation between each letter in seconds


time.sleep(1)

gui.click(CHROME)
time.sleep(1)

gui.click(TYPING_WINDOW)
time.sleep(1)

for _ in range(RUN_N_TIMES):
    
    gui.click(PRACTICE_BUTTON)
    time.sleep(PRAC_LOAD_TIME)

    img = capture(Typing_Bolt)
    text = predict(img)

    write_text(text)
    time.sleep(.25)
    
gui.alert(f'Automation was done {RUN_N_TIMES} times!!')
