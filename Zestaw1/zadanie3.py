import datetime as dt
import time

while True:
    now = dt.datetime.now()
    hours = now.hour
    if hours < 10:
        hours = '0' + str(hours)
    minutes = now.minute
    if minutes < 10:
        minutes = '0' + str(minutes)
    seconds = now.second
    if seconds < 10:
        seconds = '0' + str(seconds)
    print(chr(16), ' ' * 3, hours, ':', minutes, ':', seconds, ' ' * 3, chr(17), end='\r', sep='')
    time.sleep(0.5)