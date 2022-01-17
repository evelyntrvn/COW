import time
import pyautogui

time.sleep(3)

while True:
    pyautogui.moveTo(1080, 380)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(917, 564, 1)
    time.sleep(10)