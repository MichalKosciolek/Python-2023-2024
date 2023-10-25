import os
import time

text = input()

height = 15
position = 0
direction = 1
while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('\n' * position + text) 
    position += direction
    if position == height or position == 0: 
        direction *= -1
 
    time.sleep(0.05)
    