import turtle

s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("ivory4")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("turtle")  
t.pen(pencolor='dark violet')

def draw_star(t, size, n):
    t.pendown()
    for x in range(n):
        t.forward(size)
        s=144
        t.left(s+n)
def draw_poly(t, size, n):
    t.pendown()
    for x in range(n):
        t.forward(size)
        t.rt(360/n)


t.penup()        # move the pen to the right upper corner
t.goto(75, 100)
draw_star(t, 50, 10)

t.penup()
t.home()
draw_poly(t,10,10)