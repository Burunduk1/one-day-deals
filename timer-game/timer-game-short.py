import time, random, os
from playsound import playsound

cnt = 0
while True:
	cnt += 1
	input(f'Press Enter to continue (move #{cnt})')
	time.sleep(random.randint(10, 90))
	playsound('laugh_short.mp3')
