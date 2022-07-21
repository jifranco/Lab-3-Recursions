import turtle
from math import sin,pi

window = turtle.Screen()
dragon = turtle.Turtle()
dragon.ht()
dragon.speed(9999)
turtle.colormode(255)

#If the dragon goes off the screen, this can help
#dragon.up()
#dragon.right(90)
#dragon.forward(150)
#dragon.right(-90)
#dragon.down()

length = 1 #Increasing this will make lines
iterations = 15 #This will change how many chunks there are and it determins the size
turns = 2**iterations
for i in range(turns):
	red = max(min(int(256*1.5*sin((i/turns+1/4)*2*pi)+256/2),255),0)
	green = max(min(int(256*1.5*sin((i/turns+1/4+1/3)*2*pi)+256/2),255),0)
	blue = max(min(int(256*1.5*sin((i/turns+1/4+2/3)*2*pi)+256/2),255),0)
	dragon.color(red, green, blue)
	j=i+1
	while j%2 == 0:
		j=j/2
	dragon.right((j%4)*90)
	dragon.forward(length)

window.exitonclick()