# -*- coding:utf:8 -*-
import os
os.startfile("C://Users\Fbaciocco\Desktop\Pruebas python\sexy.jpg")
#tenemos dos tipos diferentes de ejemplos D:
#el de bajo es con definicion de FUNCION y el primero es de forma directa para ejecutarse
#en un archivo
import os
def openfile():
    os.startfile("C://Users\Fbaciocco\Music\mundtot-stammtisch_(mp3.cc) (1).mp3")

def closeFile():
    try:
        os.system("taskkill /f /im aimp.exe")
    finally: print("programa cerrado")