import datetime as dt
import time

while True:
    now = dt.datetime.now()
    seconds = now.second
    if seconds < 10:
        seconds = '0' + str(seconds)
    print(chr(16), ' ' * 4, now.hour, ':', now.minute, ':', seconds, ' ' * 4, chr(17), end='\r', sep='')
    time.sleep(0.5)