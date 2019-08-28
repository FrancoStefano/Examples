# -*- coding:utf-8-*-
import pyautogui

from Programa import Funciones


def aa():
    pyautogui.press("enter")

def repeat_fun(times, f, *args):
    for i in range(times): f(*args)



Funciones.Repetir(3, Funciones.Salto)



