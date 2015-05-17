import turtle
import math

def drawAxe(padEcart):
	turtle.width(1)
	padAngle = math.pi/5
	for idx in range(0,5):
		turtle.up()
		turtle.goto((math.sin(idx*padAngle)*padEcart*11.0),math.cos(idx*padAngle)*padEcart*11.0)
		turtle.down()
		turtle.goto(-math.sin(idx*padAngle)*padEcart*11.0,-math.cos(idx*padAngle)*padEcart*11.0)
	turtle.down()

def drawPI(padEcart,decimales):	
	padAngle = 36
	turtle.width(2)

	turtle.up()
	turtle.goto(0,padEcart)
	turtle.down()

	turtle.begin_fill()
	turtle.circle(-padEcart)
	turtle.end_fill()

	turtle.up()
	turtle.goto(0,padEcart)
	turtle.down()

	cpt = 2
	for decimale in decimales:
		turtle.left(90)
		turtle.forward(padEcart)
		turtle.right(90)
		turtle.circle(-padEcart*cpt,decimale*padAngle)
		cpt += 1


decimales = [3,1,4,1,5,9,2,6,5,4]
padEcart = 20
drawAxe(padEcart)
drawPI(padEcart,decimales)
turtle.exitonclick()

