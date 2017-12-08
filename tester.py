#! /usr/bin/env python3

from Tile import Tile
from Area import Area
from Skeleton import Skeleton

	

def handleInput(area, cmd):
	if cmd == 'info' or cmd == ' i':
		print("info")
	if cmd == 'd' or cmd == 'D':
		a.movePlayer('e')

#sETUP
a = Area()

while 1 < 2:
	a.printMap()
	print("")
	key = input(">")
	handleInput(a, key)
	environmentTick()


