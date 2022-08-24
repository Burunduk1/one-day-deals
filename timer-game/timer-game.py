import time, random, os
from playsound import playsound
from termcolor import colored

def strBegins(x, t):
	res = t[:len(x)] == x
	if res == False: return res, []
	return res, [(x, 'red'), (t[len(x):], 'white')]
def strEnds(x, t):
	res = t[-len(x):] == x
	if res == False: return res, []
	return res, [(t[:-len(x)], 'white'), (x, 'red')]
def strContains(x, t):
	i = t.find(x)
	res = i != -1
	if res == False: return res, []
	return res, [(t[:i], 'white'), (x, 'red'), (t[(i+len(x)):], 'white')]

words = list(map(lambda x : x.strip(), open('russian_nouns.txt').readlines()))

cnt = 0
while True:
	cnt += 1
	input(f'Press Enter to continue (move #{cnt})')
	time.sleep(random.randint(10, 90))
	playsound('laugh_short.mp3')
	while True:
		s = input('Show answers? [N|L|R|X]: ')
		if s == 'L': f = strBegins
		if s == 'R': f = strEnds
		if s == 'X': f = strContains
		if len(s) == 1 and s in 'NLRX': break
	if s != 'N':
		x = input('Word: ')
		for word in words:
			res, parts = f(x, word)
			if res:
				for part, color in parts:
					print(colored(part, color), end='')
				print()
	# print(i)
