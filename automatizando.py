import pyautogui 
import time

pyautogui.PAUSE = 3

pyautogui.press("win")
pyautogui.write("Brave")
pyautogui.press("enter")

pyautogui.write("linkedin.com")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "n")
pyautogui.write("gmail.com")
pyautogui.press("enter")

pyautogui.hotkey("win", "right")
time.sleep(2)
pyautogui.press("enter")



