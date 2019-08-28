# -*-coding: utf-8-*
import datetime
import time

def tiempo():
    dt = datetime.datetime.now()
    if dt.time() < datetime.time():
        return "dias"
    else:
        return "tardes"
