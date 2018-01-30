#fivestar.py
'''
turtle
forward(distance)
left(angel) right(angel)
penup()pendown()
goto(x, y)
home()
circle(radius)
speed()
'''
from turtle import Turtle
p = Turtle()
p.speed(3)
p.pensize(5)
p.color("black", 'yellow')
#p.fillcolor("red")
p.begin_fill()
for i in range(5):
	p.forward(200)
	p.right(144)
p.end_fill()