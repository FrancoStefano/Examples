import webbrowser
import time
time.ctime()
print("este programa comienza a las: "+time.ctime())
totalBreaks = 3
breakCount = 0
while breakCount < totalBreaks:
    time.sleep(5)
    webbrowser.open("https://youtu.be/zOefHqSunvA?t=1m10s")
    breakCount = breakCount + 1
