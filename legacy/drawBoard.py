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
