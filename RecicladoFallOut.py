# -*- coding:utf-8-*-

import pyautogui
import time


def recliclado():
    def seleccionarma():
        pyautogui.moveTo(x=1054, y=670)  # mover hasta el menu principal
        pyautogui.click(), time.sleep(0.3)
        pyautogui.click(), time.sleep(0.3)
        pyautogui.moveTo(x=958, y=667)
        pyautogui.click(), time.sleep(0.3)

    seleccionarma()

    def reciclar():
        pyautogui.moveTo(x=1360, y=758)
        pyautogui.click(), time.sleep(0.3)
        pyautogui.click(), time.sleep(0.3)
        pyautogui.click(), time.sleep(0.3)

    reciclar()


recliclado()

i = 0
p = 10
if i <= p:
    recliclado(), time.sleep(1)
    i = i + 1
    print(i)
