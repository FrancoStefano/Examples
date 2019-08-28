# -*-coding:utf-8 -*-
from datetime import datetime
ahora = datetime.now()
mm = str(ahora.month)
dd = str(ahora.day)
yyyy = str(ahora.year)

hora = str(ahora.hour)
minuto = str(ahora.minute)
segundo = str(ahora.second)
print(dd + "/" + mm + "/" + yyyy + "  " + hora + ":" + minuto + ":" + segundo)
