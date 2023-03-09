from time import sleep
import random
import pyautogui

def moveMouse():
  pyautogui.FAILSAFE = False

  randomX = random.randint(0, 1000)
  randomY = random.randint(0, 1000)
  sleep(1)
  randomBackX = random.randint(0, 1000)
  randomBackY = random.randint(0, 1000)

  pyautogui.moveTo(randomX, randomY)
  pyautogui.moveRel(randomBackX, randomBackY)