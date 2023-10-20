from time import sleep
import math

lenght = input()
lenght = int(lenght)

div = 100 / lenght
progress = 0
percent = 0
for i in range(1, 102):
    print('|', '=' * progress, '-' * int(lenght - progress), '|', ' ', percent, '%', sep='', end='\r', flush=True)
    progress = math.ceil(i / div)
    percent += 1
    sleep(0.2)
print()