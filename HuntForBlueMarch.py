import sys
"import sysCheck"
import numpy

BOARDWIDTH = 20
BOARDHEIGHT = 20

theSubmarine = []
theVessel = []

def main():
   print("in main()")
   initGame()
   drawBoard()


def setSubmarine():
   global theSubmarine

   xpos = numpy.random.randint(1,BOARDWIDTH)
   ypos = numpy.random.randint(1, BOARDHEIGHT)
   theSubmarine = [xpos, ypos]
   print(theSubmarine)

def setVessel():
   global theVessel

   xpos = numpy.random.randint(1,BOARDWIDTH)
   ypos = numpy.random.randint(1, BOARDHEIGHT)
   
   if xpos == theSubmarine[0] & ypos == theSubmarine[1]:
      xpos = numpy.random.randint(1,BOARDWIDTH)
      ypos = numpy.random.randint(1, BOARDHEIGHT)
   
   theVessel = [xpos, ypos]

def initGame():
	setSubmarine()
	setVessel()


def drawBoard():
	for x in range(1, BOARDWIDTH):
		for y in range(1, BOARDHEIGHT):
			print("0")
			if x == theVessel[0] & y == theVessel[1]:
				print("V")
			if x == theSubmarine[0] & y == theSubmarine[1]:
				print("S")
		print()
				


if __name__ == '__main__':
   main()


