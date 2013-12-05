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


def drawBoard():
	z = 0
	for x in range(0, BOARDWIDTH):
		print(z, end=' ')
		z += 1
		if z == 10:
			z = 0
			
	print()
	for x in range(0, BOARDWIDTH):
		for y in range(0, BOARDHEIGHT):
			if x == theVessel[0] and y == theVessel[1]:
				print("V", end=' ');
			elif x == theSubmarine[0] and y == theSubmarine[1]:
				print("S", end=' ');
			else:
				print(".", end=' ');
		print(" %d" % x)
				


if __name__ == '__main__':
   main()


