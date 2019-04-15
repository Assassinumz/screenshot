from pathlib import Path
import os, pyautogui, keyboard
from datetime import datetime as dt

pictures = str(Path.home()) + "\Pictures/" # Screenshot PATH

while True:
    file = "{0}{1}.png".format(pictures, dt.now().strftime("[%Y-%m-%d %H-%M-%S]")) #Filename

    keyboard.wait('f9') # Key to take the screenshot
    screenshot = pyautogui.screenshot(file)