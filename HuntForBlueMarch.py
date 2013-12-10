#!/usr/bin/env python
# encoding: utf-8
"""
HuntForBlueMarch.py

Created by Andreas Wassmer on 2013-12-05.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import numpy
import helpSystem

BOARDWIDTH  = 20
BOARDHEIGHT = 20
SONARRADIUS = 5
BOMBRADUIS  = SONARRADIUS - 1

theSubmarine = []
theVessel = []
directHits = 2

gameOver = False

def main():
	"""
	This is the main game loop. It reads the keyboard and calls
	the connected actions.
	"""
	initGame()

	key = 'a'
	while key != 'q' and gameOver == False:
		print("Your orders, sir:"),
		key = raw_input()
		if key == 'm':
			print("moving vessel")
			moveShip()
			print(theVessel)
		elif key == 'd':
			dropBomb()
		elif key == 's':
			print("reading sonar")
			readSonar()
		elif key == 'a':
			print("!! ABANDON SHIP !!")
			key = 'q'
		elif key == 'h':
			helpSystem.short_help()
		elif key == 'q':
			print("quit game")
		else:
			print("Sorry, sir, I don't understand!")
	
	if gameOver:
		print("Congratulation, sir! You completed the mission successfully!")
	
	
	# drawBoard()
	

def setSubmarine():
	"""
	Sets the initial position of the submarine on the grid. 
	"""
	global theSubmarine

	xpos = numpy.random.randint(0,BOARDWIDTH)
	ypos = numpy.random.randint(0, BOARDHEIGHT)
	theSubmarine = [xpos, ypos]
	print("theSubmarine = %d, %d" % (theSubmarine[0], theSubmarine[1]))

def setVessel():
	"""
	Sets the initial position of the vessel on the grid.
	"""
	
	global theVessel

	xpos = numpy.random.randint(0,BOARDWIDTH)
	ypos = numpy.random.randint(0, BOARDHEIGHT)
   
	if xpos == theSubmarine[0] and ypos == theSubmarine[1]:
		xpos = numpy.random.randint(0,BOARDWIDTH)
		ypos = numpy.random.randint(0, BOARDHEIGHT)
   
	theVessel = [xpos, ypos]


def initGame():
	"""
	Initializes the game, i.e. sets the vessel and the
	submarine randomly on the board.
	"""
	setSubmarine()
	setVessel()


def readSonar():
	"""
	Checks if a submarine is in the vincinity of the vessel.
	The distance that the sonar can detect submarines is given by
	the global constant SONARRADUIS.
	"""
	base_msg = "Sonar reports: "
	
	distance = calculateDistance()
	if distance <= SONARRADIUS:
		print(base_msg + "submarine detected, sir!")
	else:
		print(base_msg + "nothing nearby, sir!")


def moveShip():
	"""
	Moves the vessel one grid cell. Possible directions are
	N (up), S (down), E (right) and W (left).
	"""

	global theVessel
	direction_ok = False
	
	print("Direction (N,E,S,W): "),
	while direction_ok == False:
		direction = raw_input()
		
		if direction.upper() == "N":
			theVessel[1] = theVessel[1]-1
			direction_ok = True
		elif direction.upper() == "S":
			theVessel[1] = theVessel[1]+1
			direction_ok = True
		elif direction.upper() == "E":
			theVessel[0] = theVessel[0]+1
			direction_ok = True
		elif direction.upper() == "W":
			theVessel[0] = theVessel[0]-1
			direction_ok = True
	
	print("New position: %d, %d" % (theVessel[0], theVessel[1]))

	
def dropBomb():
	"""
	Drops a water bomb and detects if the submarine was hit.
	It takes 2 direct hints to sink the it. The bomb can hit a 
	submarines within a range given by the global constant BOMBRADIUS.
	"""
	global directHits, gameOver
	
	print("Dropping bomb at %d, %d" % (theVessel[0], theVessel[1]))
	distance = calculateDistance()
	
	if distance <= BOMBRADUIS:
		print("Direct hit, sir!")
		directHits = directHits - 1
	
	if directHits == 0:
		print("We sunk her, sir!")
		gameOver = True
		 		

def calculateDistance():
	"""
	Calculates the Manhattan distance between the vessel and
	the submarine. Returns this distance.
	"""
	
	dx = theVessel[0] - theSubmarine[0]
	if dx < 0:
		dx = -dx
	
	dy = theVessel[1] - theSubmarine[1]
	if dy < 0:
		dy = -dy
		
	print("distance = %d" % (dx+dy))
	return dx+dy
	

if __name__ == '__main__':
   main()


