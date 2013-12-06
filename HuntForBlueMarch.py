#!/usr/bin/env python
# encoding: utf-8
"""
HuntForBlueMarch.py

Created by Andreas Wassmer on 2013-12-05.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import helpSystem
#import sysCheck
import numpy

BOARDWIDTH = 20
BOARDHEIGHT = 20

theSubmarine = []
theVessel = []

def main():
	print("in main()")
   	initGame()

	key = 'a'
	while key != 'q':
	   	print("Your orders, sir:"),
   		key = raw_input()
		if key == 'm':
			print("moving vessel")
			moveShip()
			print(theVessel)
		elif key == 'd':
			print("dropping water bomb")
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
	# drawBoard()
	

def setSubmarine():
   global theSubmarine

   xpos = numpy.random.randint(0,BOARDWIDTH)
   ypos = numpy.random.randint(0, BOARDHEIGHT)
   theSubmarine = [xpos, ypos]
   print(theSubmarine)

def setVessel():
   global theVessel

   xpos = numpy.random.randint(0,BOARDWIDTH)
   ypos = numpy.random.randint(0, BOARDHEIGHT)
   
   if xpos == theSubmarine[0] and ypos == theSubmarine[1]:
      xpos = numpy.random.randint(1,BOARDWIDTH)
      ypos = numpy.random.randint(1, BOARDHEIGHT)
   
   theVessel = [xpos, ypos]

def initGame():
	setSubmarine()
	setVessel()


def readSonar():
	base_msg = "Sonar reports: "
	
	dx = theVessel[0] - theSubmarine[0]
	if dx < 0:
		dx = -dx
	dy = theVessel[1] - theSubmarine[1]
	if dy < 0:
		dy = -dy
	
	if dx+dy <= 5:
		print(base_msg + "submarine detected, sir!")
	elif dx+dy > 5:
		print(base_msg + "nothing nearby, sir!")
	
def moveShip():
	global theVessel
	directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
	
	direction_ok = False
	
	print("Direction (N,NE,E,SE,S,SW,W,NW): "),
	while direction_ok == False:
		direction = raw_input()
		
		if direction == "N" or direction == "n":
			theVessel[1] = theVessel[1]-1;
			direction_ok = True
		elif direction == "S" or direction == "s":
			theVessel[1] = theVessel[1]+1;
			direction_ok = True
		elif direction == "E" or direction == "e":
			theVessel[0] = theVessel[0]+1;
			direction_ok = True
		elif direction == "W" or direction == "w":
			theVessel[0] = theVessel[0]-1;
			direction_ok = True
	
	
	

if __name__ == '__main__':
   main()


