# # print numbers iteratively
# def print_numbers(n):
#     for i in range(1, n+1):
#         print(i)
# # main program
# print_numbers(10)

# #``````````````````````

# #print numbers recursively
# def print_numbers(n):
#     if n == 1:           # the base case
#         print(n)
#     else:
#       print(n)
#       print_numbers(n-1) # recursive call
      
# # main program
# print_numbers(10)

# #``````````````````````

# # using a generator
# def all_perms(elements):
#     if len(elements) <=1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 yield perm[:i]+elements[0:1] + perm[i:]
# if __name__ == '__main__':
#     data = [1,2,3,4]
#     count = 0
#     for i in all_perms(data):
#         print(i)
#         count +=1
#         print(count)

#``````````````````````

#Function to create combinations
# def all_combs(list_, n):
#     if n == 0:
#         return [[]]
#     l =[]
#     for i in range(0, len(list_)):
#         m = list_[ i]
#         r = list_[i+1:]
        
#         for p in all_combs(r, n-1):
#             l.append([ m] + p)            
#     return l

# # Driver code
# if __name__=="__main__":
#     items ="abcd"
#     print(all_combs([x for x in items], 3))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from timeit import Timer, timeit
# from functools import lru_cache

# # naive implementation of the Fibonacci function
# def fib1(n) :
#     if n<=1 :
#         return n
#     else :
#         return fib1(n-1) + fib1(n-2)

# # using a cache for the Fibonacci function
# def fib2(n) :
#     if n in cache :
#         return cache[ n]
#     if n<=1 :
#         cache[ n] = n
#         return n
#     else :
#         cache[ n] = fib2(n-1) + fib2(n-2)
#         return cache[ n]


# @lru_cache()                 
# # using the caching system in Python for the Fibonacci function
# def fib3(n) :
#     if n<=1 :
#         return n
#     else :
#         return fib3(n-1) + fib3(n-2)

# # calls Fibonacci function
# print(fib1(4))
# cache = {}
# print(fib2(4))
# print(fib3(4))

# t1 = Timer("fib1(15)", "from __main__ import fib1")
# print("fib1 ",t1.timeit(number=1), "milliseconds")
# t2 = Timer("fib2(15)", "from __main__ import fib2")
# print("fib2 ",t2.timeit(number=1), "milliseconds")
# t3 = Timer("fib3(15)", "from __main__ import fib3")
# print("fib3 ",t2.timeit(number=1), "milliseconds")

# print(type)

#
#
# main program






# import turtle

# s = turtle.Screen()     # make a canvas window
# s.setup(400, 400)
# s.bgcolor("ivory4")
# s.title("Turtle Program")

# t = turtle.Turtle()     # make a pen
# t.shape("turtle")  
# t.pen(pencolor='dark violet')

# def draw_star(t, size, n):
#     t.pendown()
#     for x in range(n):
#         t.forward(size)
#         s=144
#         t.left(s+n)
# def draw_poly(t, size, n):
#     t.pendown()
#     for x in range(n):
#         t.forward(size)
#         t.rt(360/n)


# t.penup()        # move the pen to the right upper corner
# t.goto(75, 100)
# draw_star(t, 50, 10)

# t.penup()
# t.home()
# draw_poly(t,10,10)

# draws a Sierpinski triangle
import turtle

# set canvas
def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 450)
    turtle.bgcolor("ivory")
    turtle.title("Sierpinski Triangle")
    return s

# set a turtle (a pen)
def set_pen(color):
    t = turtle.Turtle()
    t.shape("turtle")  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=5)
    return t

# draw a triangle
def draw_triangle(vertices,color,my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0],vertices[1][1])
    my_turtle.goto(vertices[2][0],vertices[2][1])
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.end_fill()
    
# find the midpoint
def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
    
# draw Sierpinski triangle recursively
def draw_Sierpinski(vertices, level, my_turtle):
    global colors       
    if level > 0:   # recursive step
        draw_triangle(vertices,colors[level],my_turtle) # this is optional
        draw_Sierpinski([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)
        draw_Sierpinski([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                      level - 1, my_turtle)
        draw_Sierpinski([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)
    else:           # base case
        draw_triangle(vertices,colors[level],my_turtle)

# main program
s = set_canvas()
t = set_pen("black")
t.left(90)
colors = ["red","gold", "aqua", "navy", "cadet blue"]
vertices = [[-200, -100], [0, 200], [200, -100]]
draw_Sierpinski(vertices, 4, t)