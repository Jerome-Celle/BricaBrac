import turtle

turtle.hideturtle()
screen = turtle.getscreen()
turtle.width(2)
pad = 36
turtle.begin_fill()
turtle.circle(-10)
turtle.end_fill()
decimales = [3,1,4,1,5,9,2,6,5,4]
cpt = 2
for decimale in decimales:
	turtle.left(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.circle(-10*cpt,decimale*pad)
	cpt += 1

turtle.exitonclick()