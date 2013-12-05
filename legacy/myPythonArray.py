import sys
"import sysCheck"
import numpy

BOARDWIDTH = 20
BOARDHEIGHT = 20

theSea = []
theSubmarine = []
theVessel = []

def main():
   print("in main()")
   initGame()
   drawBoard()


def clearTheSea():
   print("in clearTheSea()")
   for x in range(BOARDWIDTH):
      column = []
      for y in range(BOARDHEIGHT):
         column.append(0)
      theSea.append(column)

def initGame():
   clearTheSea()
   xpos = numpy.random.randint(1,BOARDWIDTH)
   ypos = numpy.random.randint(1, BOARDHEIGHT)

   theSea[xpos][ypos] = 'U'
   theSea[xpos+3][ypos-1] = 'S'

def drawBoard():
   for x in range(1, BOARDWIDTH):
      for y in range(1, BOARDHEIGHT):
         print(theSea[x][y]),
      print()


if __name__ == '__main__':
   main()


