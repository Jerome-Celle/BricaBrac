import turtle
import math

def drawAxe(padEcart):
	turtle.color(0.7,0.7,0.7)	
	turtle.width(1)
	padAngle = math.pi/5
	for idx in range(0,5):
		turtle.up()
		turtle.goto((math.sin(idx*padAngle)*padEcart*11.0),math.cos(idx*padAngle)*padEcart*11.0)
		turtle.down()
		turtle.goto(-math.sin(idx*padAngle)*padEcart*11.0,-math.cos(idx*padAngle)*padEcart*11.0)
	turtle.down()

def drawPI(padEcart,decimales):
	turtle.color(1,1,1)	
	padAngle = 36
	turtle.width(4)

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
padEcart = 40
turtle.screensize(2000,1500)
turtle.begin_fill()
turtle.color(0.4,0.4,0.4)
turtle.up()
turtle.goto(0,11*padEcart+10)
turtle.down()
turtle.circle(-(11*padEcart)-10)
turtle.end_fill()
drawAxe(padEcart)
drawPI(padEcart,decimales)
turtle.exitonclick()

