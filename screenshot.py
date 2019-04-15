from pathlib import Path
import os, pyautogui, keyboard
from datetime import datetime as dt

pictures = str(Path.home()) + "\Pictures"
file = "{0}/{1}.png".format(pictures, dt.now().strftime("[%A]"))

keyboard.wait('f12')
screenshot = pyautogui.screenshot(file)

